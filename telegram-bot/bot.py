"""
Telegram bot for studying Lithuanian B2 grammar.
Uses python-telegram-bot >= 21.0 (async API).
"""

import json
import logging
import os
import sys
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from data import MODULES, get_exercises, get_module, get_theory

# ── Logging ──────────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO,
)
log = logging.getLogger(__name__)

# ── Progress persistence ─────────────────────────────────────────

PROGRESS_FILE = Path(__file__).with_name("progress.json")


def _load_progress() -> dict:
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            log.warning("Corrupted progress file, starting fresh")
    return {}


def _save_progress(data: dict) -> None:
    try:
        PROGRESS_FILE.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except OSError:
        log.exception("Failed to save progress")


progress: dict = _load_progress()

# ── In-memory sessions ───────────────────────────────────────────

sessions: dict[int, dict] = {}

# ── Subtopic display names (for žinynas) ─────────────────────────

SUBTOPIC_NAMES: dict[str, str] = {
    "nuosakos": "Nuosakos (наклонения)",
    "pasyvas": "Pasyvas (пассив)",
    "budvardziai": "Būdvardžiai (прилагательные)",
    "valdymas": "Valdymas (управление)",
    "prielinksniai": "Prielinksniai (предлоги)",
    "ivardis": "Įvardis (местоимения)",
}

# ── Helpers ───────────────────────────────────────────────────────


def uid(update: Update) -> int:
    """Extract user id from Update (works for both messages and callbacks)."""
    if update.callback_query:
        return update.callback_query.from_user.id
    return update.effective_user.id


def pkey(user_id: int) -> str:
    return str(user_id)


def clear_session(user_id: int) -> None:
    sessions.pop(user_id, None)


def _chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# ── Keyboard builders ────────────────────────────────────────────


def main_menu_kb() -> InlineKeyboardMarkup:
    buttons = []
    for m in MODULES:
        buttons.append(
            [InlineKeyboardButton(m["name"], callback_data=f"mod_{m['id']}")]
        )
    return InlineKeyboardMarkup(buttons)


def module_kb(mod: dict) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []

    if mod.get("has_theory"):
        if mod["id"] == "zinynas" and mod.get("subtopics"):
            for st in mod["subtopics"]:
                label = SUBTOPIC_NAMES.get(st, st)
                rows.append(
                    [InlineKeyboardButton(f"📖 {label}", callback_data=f"theory_{st}")]
                )
        else:
            rows.append(
                [
                    InlineKeyboardButton(
                        "📖 Теория", callback_data=f"theory_{mod['id']}"
                    )
                ]
            )

    if mod["id"] == "zinynas" and mod.get("subtopics"):
        for idx, st in enumerate(mod["subtopics"], 1):
            label = SUBTOPIC_NAMES.get(st, st)
            rows.append(
                [
                    InlineKeyboardButton(
                        f"✏️ Drill {idx}: {label}",
                        callback_data=f"drill_{mod['id']}_{idx}",
                    )
                ]
            )
    else:
        drill_btns = [
            InlineKeyboardButton(
                f"✏️ Drill {i}", callback_data=f"drill_{mod['id']}_{i}"
            )
            for i in range(1, mod["drills"] + 1)
        ]
        for chunk in _chunks(drill_btns, 3):
            rows.append(chunk)

    rows.append([InlineKeyboardButton("« Главное меню", callback_data="main")])
    return InlineKeyboardMarkup(rows)


def theory_kb(topic_id: str, page: int, total: int) -> InlineKeyboardMarkup:
    nav = []
    if page > 0:
        nav.append(
            InlineKeyboardButton("⬅️", callback_data=f"theory_{topic_id}_{page - 1}")
        )
    nav.append(InlineKeyboardButton(f"{page + 1}/{total}", callback_data="noop"))
    if page < total - 1:
        nav.append(
            InlineKeyboardButton("➡️", callback_data=f"theory_{topic_id}_{page + 1}")
        )
    rows = [nav]

    mod = _topic_to_module(topic_id)
    if mod:
        rows.append(
            [InlineKeyboardButton("« Назад к модулю", callback_data=f"mod_{mod}")]
        )
    else:
        rows.append([InlineKeyboardButton("« Главное меню", callback_data="main")])
    return InlineKeyboardMarkup(rows)


def _topic_to_module(topic_id: str):
    """Map a theory topic_id back to its parent module id."""
    for m in MODULES:
        if m["id"] == topic_id:
            return m["id"]
        if topic_id in (m.get("subtopics") or []):
            return m["id"]
    return None


def exercise_choice_kb(ex: dict, ex_index: int) -> InlineKeyboardMarkup:
    rows = []
    for i, opt in enumerate(ex["options"]):
        rows.append(
            [InlineKeyboardButton(opt, callback_data=f"ans_{ex_index}_{i}")]
        )
    rows.append([InlineKeyboardButton("💡 Подсказка", callback_data="hint")])
    return InlineKeyboardMarkup(rows)


def exercise_input_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("💡 Подсказка", callback_data="hint")]]
    )


def after_answer_kb(module_id: str, has_next: bool) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    if has_next:
        rows.append([InlineKeyboardButton("Следующий вопрос ➡️", callback_data="next")])
    rows.append(
        [InlineKeyboardButton("« Назад к модулю", callback_data=f"mod_{module_id}")]
    )
    return InlineKeyboardMarkup(rows)


def end_drill_kb(module_id: str, drill_num: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔄 Пройти заново",
                    callback_data=f"drill_{module_id}_{drill_num}",
                )
            ],
            [
                InlineKeyboardButton(
                    "« Назад к модулю", callback_data=f"mod_{module_id}"
                )
            ],
            [InlineKeyboardButton("« Главное меню", callback_data="main")],
        ]
    )


# ── Exercise display ─────────────────────────────────────────────


async def _send_exercise(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    user_id: int,
) -> None:
    sess = sessions.get(user_id)
    if not sess:
        return

    pos = sess["pos"]
    exercises = sess["exercises"]

    if pos >= len(exercises):
        await _finish_drill(update, context, user_id)
        return

    ex = exercises[pos]
    total = len(exercises)
    header = f"<b>Вопрос {pos + 1}/{total}</b>\n\n"

    if ex["type"] == "choice":
        text = header + ex["q"]
        kb = exercise_choice_kb(ex, pos)
    else:
        text = header + ex["q"] + "\n\n<i>Введите ответ текстом:</i>"
        kb = exercise_input_kb()
        sess["awaiting_input"] = True

    target = update.callback_query.message if update.callback_query else update.effective_message
    await target.reply_text(text, parse_mode=ParseMode.HTML, reply_markup=kb)


async def _finish_drill(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    user_id: int,
) -> None:
    sess = sessions.get(user_id)
    if not sess:
        return

    score = sess["score"]
    total = len(sess["exercises"])
    pct = round(score / total * 100) if total else 0
    module_id = sess["module"]
    drill_num = sess["drill"]

    # Persist progress
    uk = pkey(user_id)
    progress.setdefault(uk, {})
    drill_key = f"{module_id}_{drill_num}"
    prev = progress[uk].get(drill_key, {})
    if score > prev.get("score", -1):
        progress[uk][drill_key] = {"score": score, "total": total}
        _save_progress(progress)

    medal = "🏆" if pct == 100 else ("🎉" if pct >= 70 else "📊")
    text = (
        f"{medal} <b>Результат:</b> {score}/{total} = {pct}%\n\n"
        + ("Отлично! Всё правильно!" if pct == 100 else "")
        + ("Хороший результат!" if 70 <= pct < 100 else "")
        + ("Попробуйте ещё раз!" if pct < 70 else "")
    )

    target = update.callback_query.message if update.callback_query else update.effective_message
    await target.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=end_drill_kb(module_id, drill_num),
    )
    clear_session(user_id)


# ── Command handlers ─────────────────────────────────────────────


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    clear_session(uid(update))
    text = (
        "🇱🇹 <b>Литовский B2 — Грамматический тренажёр</b>\n\n"
        "Выберите тему для изучения:"
    )
    await update.message.reply_text(
        text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb()
    )


async def cmd_progress(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = uid(update)
    uk = pkey(user_id)
    data = progress.get(uk, {})

    if not data:
        await update.message.reply_text(
            "📊 У вас пока нет результатов.\nНачните с /start и выберите тему!",
            parse_mode=ParseMode.HTML,
        )
        return

    lines = ["📊 <b>Ваш прогресс:</b>\n"]
    for m in MODULES:
        mod_lines = []
        for d in range(1, m["drills"] + 1):
            key = f"{m['id']}_{d}"
            if key in data:
                s = data[key]["score"]
                t = data[key]["total"]
                pct = round(s / t * 100) if t else 0
                icon = "✅" if pct == 100 else ("🟡" if pct >= 70 else "🔴")
                if m["id"] == "zinynas" and m.get("subtopics") and d <= len(m["subtopics"]):
                    drill_label = SUBTOPIC_NAMES.get(m["subtopics"][d - 1], f"Drill {d}")
                else:
                    drill_label = f"Drill {d}"
                mod_lines.append(f"  {icon} {drill_label}: {s}/{t} ({pct}%)")
        if mod_lines:
            lines.append(f"\n<b>{m['name']}</b>")
            lines.extend(mod_lines)

    await update.message.reply_text(
        "\n".join(lines), parse_mode=ParseMode.HTML
    )


async def cmd_reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = uid(update)
    uk = pkey(user_id)
    progress.pop(uk, None)
    _save_progress(progress)
    clear_session(user_id)
    await update.message.reply_text(
        "🗑 Весь прогресс сброшен. Начните заново с /start",
        parse_mode=ParseMode.HTML,
    )


# ── Callback query handler ───────────────────────────────────────


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    if data == "noop":
        return

    # ── Main menu ──
    if data == "main":
        clear_session(user_id)
        text = (
            "🇱🇹 <b>Литовский B2 — Грамматический тренажёр</b>\n\n"
            "Выберите тему для изучения:"
        )
        await query.message.edit_text(
            text, parse_mode=ParseMode.HTML, reply_markup=main_menu_kb()
        )
        return

    # ── Module view ──
    if data.startswith("mod_"):
        clear_session(user_id)
        mod_id = data[4:]
        mod = get_module(mod_id)
        if not mod:
            await query.message.edit_text("Модуль не найден.")
            return
        text = f"📚 <b>{mod['name']}</b>\n\n{mod['desc']}"
        await query.message.edit_text(
            text, parse_mode=ParseMode.HTML, reply_markup=module_kb(mod)
        )
        return

    # ── Theory pages ──
    if data.startswith("theory_"):
        parts = data.split("_", 2)
        # "theory_{topic}" or "theory_{topic}_{page}"
        if len(parts) == 2:
            topic_id = parts[1]
            page = 0
        else:
            topic_id = parts[1]
            try:
                page = int(parts[2])
            except ValueError:
                page = 0

        pages = get_theory(topic_id)
        if not pages:
            await query.message.edit_text(
                "Теория ещё не добавлена для этой темы.",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("« Назад", callback_data="main")]]
                ),
            )
            return

        page = max(0, min(page, len(pages) - 1))
        content = pages[page]
        if isinstance(content, tuple):
            content = content[0] if content else ""
        await query.message.edit_text(
            content,
            parse_mode=ParseMode.HTML,
            reply_markup=theory_kb(topic_id, page, len(pages)),
        )
        return

    # ── Start drill ──
    if data.startswith("drill_"):
        parts = data.split("_", 2)
        if len(parts) < 3:
            return
        mod_id = parts[1]
        try:
            drill_num = int(parts[2])
        except ValueError:
            return

        exercises = get_exercises(mod_id, drill_num)
        if not exercises:
            await query.message.edit_text(
                "В этом упражнении пока нет вопросов.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "« Назад", callback_data=f"mod_{mod_id}"
                            )
                        ]
                    ]
                ),
            )
            return

        sessions[user_id] = {
            "module": mod_id,
            "drill": drill_num,
            "exercises": exercises,
            "pos": 0,
            "score": 0,
            "awaiting_input": False,
            "answered": False,
        }

        header = f"✏️ <b>{_drill_label(mod_id, drill_num)}</b> — {len(exercises)} вопросов\n"
        await query.message.edit_text(header, parse_mode=ParseMode.HTML)
        await _send_exercise(update, context, user_id)
        return

    # ── Answer (choice) ──
    if data.startswith("ans_"):
        sess = sessions.get(user_id)
        if not sess or sess.get("answered"):
            return
        parts = data.split("_")
        if len(parts) < 3:
            return
        try:
            ex_index = int(parts[1])
            chosen = int(parts[2])
        except ValueError:
            return

        if ex_index != sess["pos"]:
            await query.answer("Этот вопрос уже неактуален.")
            return

        ex = sess["exercises"][sess["pos"]]
        correct = ex["correct"]
        sess["answered"] = True

        if chosen == correct:
            sess["score"] += 1
            feedback = "✅ <b>Правильно!</b>"
        else:
            right_text = ex["options"][correct]
            feedback = f"❌ <b>Неправильно.</b> Правильный ответ: <b>{right_text}</b>"

        if ex.get("explanation"):
            feedback += f"\n\n📝 {ex['explanation']}"
        if ex.get("ru"):
            feedback += f"\n🇷🇺 {ex['ru']}"

        has_next = sess["pos"] < len(sess["exercises"]) - 1
        await query.message.reply_text(
            feedback,
            parse_mode=ParseMode.HTML,
            reply_markup=after_answer_kb(sess["module"], has_next),
        )
        return

    # ── Hint ──
    if data == "hint":
        sess = sessions.get(user_id)
        if not sess:
            return
        ex = sess["exercises"][sess["pos"]]
        hint = ex.get("hint", "")
        text = f"💡 {hint}" if hint else "Подсказка недоступна."
        await query.answer(text, show_alert=True)
        return

    # ── Next exercise ──
    if data == "next":
        sess = sessions.get(user_id)
        if not sess:
            return
        sess["pos"] += 1
        sess["awaiting_input"] = False
        sess["answered"] = False
        await _send_exercise(update, context, user_id)
        return


def _drill_label(mod_id: str, drill_num: int) -> str:
    mod = get_module(mod_id)
    if mod and mod.get("subtopics") and drill_num <= len(mod["subtopics"]):
        st = mod["subtopics"][drill_num - 1]
        return f"{mod['name']} — {SUBTOPIC_NAMES.get(st, st)}"
    mod_name = mod["name"] if mod else mod_id
    return f"{mod_name} — Drill {drill_num}"


# ── Text message handler (for input exercises) ───────────────────


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = uid(update)
    sess = sessions.get(user_id)

    if not sess or not sess.get("awaiting_input") or sess.get("answered"):
        await update.message.reply_text(
            "Выберите тему или упражнение через меню: /start",
            parse_mode=ParseMode.HTML,
        )
        return

    ex = sess["exercises"][sess["pos"]]
    user_answer = update.message.text.strip()
    accepted = [a.strip().lower() for a in ex.get("answer", [])]

    sess["awaiting_input"] = False
    sess["answered"] = True

    if user_answer.lower() in accepted:
        sess["score"] += 1
        feedback = "✅ <b>Правильно!</b>"
    else:
        right = ex["answer"][0] if ex.get("answer") else "?"
        feedback = f"❌ <b>Неправильно.</b> Правильный ответ: <b>{right}</b>"

    if ex.get("explanation"):
        feedback += f"\n\n📝 {ex['explanation']}"
    if ex.get("ru"):
        feedback += f"\n🇷🇺 {ex['ru']}"

    has_next = sess["pos"] < len(sess["exercises"]) - 1
    await update.message.reply_text(
        feedback,
        parse_mode=ParseMode.HTML,
        reply_markup=after_answer_kb(sess["module"], has_next),
    )


# ── Main ─────────────────────────────────────────────────────────


def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print(
            "ERROR: BOT_TOKEN environment variable is not set.\n"
            "  export BOT_TOKEN='your-telegram-bot-token'\n"
            "  python bot.py"
        )
        sys.exit(1)

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("progress", cmd_progress))
    app.add_handler(CommandHandler("reset", cmd_reset))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))

    log.info("Bot started — polling…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
