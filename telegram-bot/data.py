"""
Lithuanian B2 course content for the Telegram bot.
All content ported from index.html.
"""

# ---------------------------------------------------------------------------
# Module definitions
# ---------------------------------------------------------------------------
MODULES = [
    {
        "id": "dalyviai",
        "name": "Dalyviai (причастия)",
        "desc": "Самая сложная тема B2: все типы причастий",
        "drills": 3,
        "has_theory": True,
    },
    {
        "id": "linksniai",
        "name": "Linksniai (падежи)",
        "desc": "7 падежей \u2014 таблицы склонений и упражнения",
        "drills": 3,
        "has_theory": True,
    },
    {
        "id": "veiksmazodziai",
        "name": "Veiksma\u017eod\u017eiai (глаголы)",
        "desc": "Спряжения, времена, возвратные глаголы",
        "drills": 3,
        "has_theory": True,
    },
    {
        "id": "kalbos_vartojimas",
        "name": "Kalbos vartojimas",
        "desc": "Формат экзамена: выбор правильной формы слова",
        "drills": 3,
        "has_theory": False,
    },
    {
        "id": "jungtukai",
        "name": "Jungtukai (союзы)",
        "desc": "Союзы и сложные предложения \u2014 ключ к B2 письму",
        "drills": 2,
        "has_theory": True,
    },
    {
        "id": "zodziu_daryba",
        "name": "\u017dod\u017ei\u0173 daryba (словообразование)",
        "desc": "Приставки, суффиксы и производные слова",
        "drills": 2,
        "has_theory": True,
    },
    {
        "id": "skyryba",
        "name": "Skyryba (пунктуация)",
        "desc": "Правила пунктуации \u2014 запятые, тире, двоеточия",
        "drills": 1,
        "has_theory": True,
    },
    {
        "id": "zinynas",
        "name": "Gramatikos \u017einynas (справочник)",
        "desc": "Полный справочник: наклонения, пассив, прилагательные, управление",
        "drills": 0,
        "has_theory": True,
        "subtopics": [
            "nuosakos",
            "pasyvas",
            "budvardziai",
            "valdymas",
            "prielinksniai",
            "ivardis",
        ],
    },
]

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _c(q, options, correct, hint="", explanation="", ru="", topic=""):
    return {
        "type": "choice",
        "q": q,
        "options": options,
        "correct": correct,
        "hint": hint,
        "explanation": explanation,
        "ru": ru,
        "topic": topic,
    }


def _i(q, answer, hint="", explanation="", ru=""):
    return {
        "type": "input",
        "q": q,
        "answer": answer if isinstance(answer, list) else [answer],
        "hint": hint,
        "explanation": explanation,
        "ru": ru,
    }


# ===================================================================
# THEORY
# ===================================================================
THEORY = {}

# -------------------------------------------------------------------
# DALYVIAI (причастия) - 5 pages
# -------------------------------------------------------------------
THEORY["dalyviai"] = [
    # Page 1 - introduction + active participles
    (
        "<b>Dalyviai / Причастия</b>\n\n"
        "Литовский язык имеет одну из самых богатых систем причастий в Европе. "
        "В B2 экзамене они проверяются очень активно.\n\n"
        "<b>Сравнение с русским</b>\n"
        "В русском: читающий, читавший, читаемый, прочитанный \u2014 4 формы.\n"
        "В литовском: <b>13+ форм</b> причастий от каждого глагола!\n\n"
        "<i>Главная трудность: в литовском причастия используются там, "
        "где русский использует придаточные предложения с \u201eкоторый\u201c.</i>\n\n"
        "<b>Veikiamieji dalyviai / Действительные причастия</b>\n"
        "Образуются от активного залога \u2014 \u201eтот, кто делает\u201c\n\n"
        "<b>Esamasis</b> (наст.): skaitANTIS / skaitANTI\n"
        "<b>B\u016bt. kartinis</b> (прош.однокр.): skait\u0118S / skai\u010dIUSI\n"
        "<b>B\u016bt. da\u017eninis</b> (прош.многокр.): skaitYDAV\u0118S / skaitYDAVUSI\n"
        "<b>B\u016bsimasis</b> (буд.): skaitYSIANTIS / skaitYSIANTI\n\n"
        "<b>Как образовать?</b>\n"
        "<b>Esamasis:</b> 3-е лицо наст.вр. + -antis/-anti (I спр.) "
        "или -intis/-inti (II спр.)\n"
        "skaito \u2192 skaitANTIS | myli \u2192 mylINTIS\n\n"
        "<b>B\u016bt. kartinis:</b> основа прош. вр. + -\u0119s/-usi\n"
        "skai\u010d\u0117 \u2192 skait\u0118S / skai\u010dIUSI"
    ),
    # Page 2 - passive participles + half-participle + gerund
    (
        "<b>Neveikiamieji dalyviai / Страдательные причастия</b>\n\n"
        "<b>Esamasis</b> (наст.): skaitOMAS / skaitOMA\n"
        "<b>B\u016btasis</b> (прош.): skaitYTAS / skaitYTA\n"
        "<b>B\u016bsimasis</b> (буд.): skaitYSIMAS / skaitYSIMA\n\n"
        "<i>Страдательные прич. прош. вр. (-tas/-ta) используются повсеместно:</i>\n"
        "Para\u0161ytas lai\u0161kas = написанное письмо\n"
        "I\u0161spr\u0119sta problema = решённая проблема\n"
        "Nustatytas laikas = установленное время\n\n"
        "<i>На экзамене часто нужно выбрать между -amas (наст.) и -ytas (прош.) \u2014 "
        "разница как между \u201eрешаемый\u201c и \u201eрешённый\u201c.</i>\n\n"
        "<b>Pusdalyvis ir padalyvis / Полупричастие и деепричастие</b>\n\n"
        "<b>Pusdalyvis</b>: skaitYDAMAS / skaitYDAMA\n"
        "\u2192 одновременное действие (= \u201eчитая\u201c)\n"
        "Eidamas namo, jis galvojo apie darb\u0105.\n"
        "= Идя домой, он думал о работе.\n\n"
        "<b>Padalyvis</b>: perskai\u010dIUS\n"
        "\u2192 предшествующее действие (= \u201eпрочитав\u201c)\n\n"
        "<i>Pusdalyvis согласуется с подлежащим по роду! "
        "Если женщина: Eidama namo, ji galvojo...</i>"
    ),
    # Page 3 - declension of participles
    (
        "<b>Склонение причастий (dalyvi\u0173 linksniavimas)</b>\n\n"
        "<i>Причастия склоняются как прилагательные! На экзамене нужно "
        "согласовать причастие по роду, числу и падежу.</i>\n\n"
        "<b>Veik. esamojo (действ. наст.): skaitantis</b>\n"
        "V. skaitantIS / skaitantI / skaitantYS / skaitant\u010dIOS\n"
        "K. skaitant\u010dIO / skaitant\u010dIOS / skaitant\u010dI\u0172\n"
        "N. skaitant\u010dIAM / skaitant\u010dIAI / skaitantIEMS\n"
        "G. skaitant\u012e / skaitant\u010dI\u0104 / skaitant\u010dIUS\n"
        "\u012en. skaitant\u010dIU / skaitant\u010dIA / skaitant\u010dIAIS\n"
        "Vt. skaitant\u010dIAME / skaitant\u010dIOJE\n\n"
        "<b>Neveik. b\u016btojo (страд. прош.): skaitytas</b>\n"
        "V. skaitytAS / skaitytA / skaitytI / skaitytOS\n"
        "K. skaitytO / skaitytOS / skaityt\u0172\n"
        "N. skaitytAM / skaitytAI / skaitytIEMS\n"
        "G. skaityt\u0104 / skaitytUS / skaitytAS\n"
        "\u012en. skaitytU / skaitytA / skaitytAIS\n"
        "Vt. skaitytAME / skaitytOJE"
    ),
    # Page 4 - full table of forms for 5 verbs
    (
        "<b>Все формы причастий от 5 основных глаголов</b>\n\n"
        "Выучите эти формы \u2014 они покрывают 80% экзамена.\n\n"
        "<b>Veik. esam.</b>\n"
        "dirbANTIS | ra\u0161ANTIS | mylINTIS | skaitANTIS | einANTIS\n\n"
        "<b>Veik. b\u016bt.kart.</b>\n"
        "dirb\u0118S | ra\u0161\u0118S | myl\u0117j\u0118S | skai\u010d\u0118S | \u0117j\u0118S\n"
        "(ж.р.: dirbUSI | ra\u0161IUSI | myl\u0117jUSI | skai\u010dIUSI | \u0117jUSI)\n\n"
        "<b>Veik. b\u016bs.</b>\n"
        "dirbSIANTIS | ra\u0161ySIANTIS | myl\u0117SIANTIS | skaitySIANTIS\n\n"
        "<b>Neveik. esam.</b>\n"
        "dirbAMAS | ra\u0161OMAS | mylIMAS | skaitOMAS | einAMAS\n\n"
        "<b>Neveik. b\u016bt.</b>\n"
        "dirbTAS | ra\u0161yTAS | myl\u0117TAS | skaityTAS | eiTAS\n\n"
        "<b>Pusdalyvis</b>\n"
        "dirbDAMAS | ra\u0161yDAMAS | myl\u0117DAMAS | skaityDAMAS | eiDAMAS\n\n"
        "<b>Padalyvis</b>\n"
        "dirb\u0118S* | para\u0161IUS | pamyl\u0117j\u0118S | perskai\u010dIUS | nu\u0117j\u0118S"
    ),
    # Page 5 - mnemonics
    (
        "<b>Как запомнить типы причастий?</b>\n\n"
        "<b>Veikiamasis</b> (действительный) \u2014 КТО делает:\n"
        "dirbantis = работающий\n\n"
        "<b>Neveikiamasis</b> (страдательный) \u2014 ЧТО делается:\n"
        "dirbamas = выполняемый\n\n"
        "<b>Pusdalyvis</b> \u2014 одновременное действие:\n"
        "dirbdamas = работая (в то время как)\n\n"
        "<b>Padalyvis</b> \u2014 предшествующее действие:\n"
        "padirb\u0119s = поработав (и потом...)\n\n"
        "<b>Мнемоника окончаний:</b>\n"
        "-antis = \u201e-ающий\u201c\n"
        "-amas = \u201e-аемый\u201c\n"
        "-tas = \u201e-анный\u201c\n"
        "-damas = \u201e-ая\u201c (деепричастие)\n"
        "-\u0119s (padalyvis) = \u201e-ав\u201c"
    ),
]

# -------------------------------------------------------------------
# LINKSNIAI (падежи) - 5 pages
# -------------------------------------------------------------------
THEORY["linksniai"] = [
    # Page 1 - 7 cases overview
    (
        "<b>Linksniai / 7 падежей литовского языка</b>\n\n"
        "<b>Vardininkas</b> (V.) \u2014 Kas? \u2014 Именительный \u2014 namas, kat\u0117\n"
        "<b>Kilmininkas</b> (K.) \u2014 Ko? \u2014 Родительный \u2014 namo, kat\u0117s\n"
        "<b>Naudininkas</b> (N.) \u2014 Kam? \u2014 Дательный \u2014 namui, katei\n"
        "<b>Galininkas</b> (G.) \u2014 K\u0105? \u2014 Винительный \u2014 nam\u0105, kat\u0119\n"
        "<b>\u012enagininkas</b> (\u012en.) \u2014 Kuo? \u2014 Творительный \u2014 namu, kate\n"
        "<b>Vietininkas</b> (Vt.) \u2014 Kur? \u2014 Предложный* \u2014 name, kat\u0117je\n"
        "<b>\u0160auksmininkas</b> (\u0160.) \u2014 \u2014 Звательный \u2014 name!, kate!\n\n"
        "<b>Главное отличие от русского</b>\n"
        "<b>Vietininkas</b> (местный падеж) \u2014 в русском его функции разделены "
        "между предложным падежом и предлогами. В литовском он показывает "
        "местонахождение <i>без предлога</i>:\n"
        "Vilniuje = в Вильнюсе | namuose = дома | mokykloje = в школе\n\n"
        "<i>В русском: \u201eв школе\u201c (предлог + предложный). "
        "В литовском: \u201emokykloje\u201c (только падеж, без предлога!).</i>"
    ),
    # Page 2 - I declension
    (
        "<b>I linksniuot\u0117 (1-е склонение): vyr. -as, -is, -ys</b>\n\n"
        "       -as(namas)  -is(brolis)  -ys(arklys)\n"
        "V.  namAS       brolIS       arklYS\n"
        "K.  namO        brolIO       arklIO\n"
        "N.  namUI       brolIUI      arklIUI\n"
        "G.  nam\u0104        brol\u012e        arkl\u012e\n"
        "\u012en. namU        brolIU       arklIU\n"
        "Vt. namE        brolYJE      arklYJE\n"
        "\u0160.  namE!       brolI!       arklY!\n\n"
        "<b>Daugiskaita (мн.ч.) I linksniuot\u0117</b>\n"
        "V.  namAI       brolIAI      arklIAI\n"
        "K.  nam\u0172        brolI\u0172       arklI\u0172\n"
        "N.  namAMS      brolIAMS     arklIAMS\n"
        "G.  namUS       brolIUS      arklIUS\n"
        "\u012en. namAIS      brolIAIS     arklIAIS\n"
        "Vt. namUOSE     brolIUOSE    arklIUOSE"
    ),
    # Page 3 - III and IV declensions (feminine)
    (
        "<b>III linksniuot\u0117 (3-е скл.): mot. -a</b>\n\n"
        "    Vns.(mokykla)  Dgs.(mokyklos)\n"
        "V.  mokyklA       mokyklOS\n"
        "K.  mokyklOS      mokykl\u0172\n"
        "N.  mokyklAI      mokyklOMS\n"
        "G.  mokykl\u0104       mokyklAS\n"
        "\u012en. mokyklA       mokyklOMIS\n"
        "Vt. mokyklOJE     mokyklOSE\n\n"
        "<b>IV linksniuot\u0117 (4-е скл.): mot. -\u0117</b>\n\n"
        "    Vns.(kat\u0117)  Dgs.(kat\u0117s)\n"
        "V.  kat\u0116       kat\u0116S\n"
        "K.  kat\u0116S      ka\u010dI\u0172\n"
        "N.  katEI      kat\u0116MS\n"
        "G.  kat\u0118       katES\n"
        "\u012en. katE       kat\u0116MIS\n"
        "Vt. kat\u0116JE     kat\u0116SE"
    ),
    # Page 4 - II and V declensions
    (
        "<b>II linksniuot\u0117 (2-е скл.): vyr. -us, -ius</b>\n\n"
        "    -us(s\u016bnus)  -ius(profesorius)\n"
        "V.  s\u016bnUS       profesorIUS\n"
        "K.  s\u016bnAUS      profesorIAUS\n"
        "N.  s\u016bnUI       profesorIUI\n"
        "G.  s\u016bn\u0172        profesorI\u0172\n"
        "\u012en. s\u016bnUMI      profesorIUMI\n"
        "Vt. s\u016bnUJE      profesorIUJE\n\n"
        "<i>II склонение \u2014 самое редкое. Но \u201e\u017emogus\u201c \u2014 одно из самых частых!</i>\n\n"
        "<b>V linksniuot\u0117 (5-е скл.): особые слова</b>\n\n"
        "    -uo(sesuo)   -uo(vanduo)   -\u0117(dukt\u0117)\n"
        "V.  sesUO        vandUO        dukt\u0116\n"
        "K.  sesERS       vandENS       dukterS\n"
        "N.  sesERIAI     vandENIUI     dukterIAI\n"
        "G.  sesER\u012e       vandEN\u012e       dukter\u012e\n"
        "\u012en. sesERIMI     vandENIU      dukterIMI\n\n"
        "<i>V скл. \u2014 слова с изменяющейся основой. "
        "Похоже на рус. \u201eмать \u2192 матери\u201c, \u201eдочь \u2192 дочери\u201c.</i>"
    ),
    # Page 5 - adjective declension + comparison
    (
        "<b>Склонение прилагательных</b>\n\n"
        "<b>geras/gera (хороший)</b>\n"
        "V.  gerAS / gerA   | gerI / gerOS\n"
        "K.  gerO / gerOS   | ger\u0172\n"
        "N.  gerAM / gerAI  | gerIEMS / gerOMS\n"
        "G.  ger\u0104            | gerUS / gerAS\n"
        "\u012en. gerU / gerA    | gerAIS / gerOMIS\n"
        "Vt. gerAME / gerOJE | gerUOSE / gerOSE\n\n"
        "<b>gra\u017eus/gra\u017ei (красивый, тип -us)</b>\n"
        "V.  gra\u017eUS / gra\u017eI | gra\u017e\u016aS / gra\u017eIOS\n"
        "K.  gra\u017eAUS / gra\u017eIOS | gra\u017eI\u0172\n"
        "G.  gra\u017e\u0172 / gra\u017eI\u0104 | gra\u017eIUS / gra\u017eIAS\n\n"
        "<b>Степени сравнения</b>\n"
        "<b>Сравнительная:</b> корень + -esnis/-esn\u0117\n"
        "geras \u2192 gerESNIS | gra\u017eus \u2192 gra\u017eESNIS\n\n"
        "<b>Превосходная:</b> корень + -iausias/-iausia\n"
        "geras \u2192 gerIAUSIAS | gra\u017eus \u2192 gra\u017eIAUSIAS\n\n"
        "<b>Сравнение:</b> -esnis + <b>u\u017e + G.</b> или <b>nei</b>\n"
        "Didesnis <b>u\u017e</b> t\u0105 = больше, чем тот\n"
        "Didesnis <b>nei</b> tas = больше, чем тот"
    ),
]

# -------------------------------------------------------------------
# VEIKSMA\u017dOD\u017dIAI (глаголы) - 4 pages
# -------------------------------------------------------------------
THEORY["veiksmazodziai"] = [
    # Page 1 - three conjugations
    (
        "<b>3 спряжения литовских глаголов</b>\n\n"
        "<b>Как определить спряжение?</b>\n"
        "По форме 3-го лица настоящего времени:\n\n"
        "<b>I asmenuot\u0117:</b> 3 л. наст.вр. = -a (dirba, skaito, ra\u0161o)\n"
        "<b>II asmenuot\u0117:</b> 3 л. наст.вр. = -i (myli, turi, nori)\n"
        "<b>III asmenuot\u0117:</b> 3 л. наст.вр. = -o (от -oti) \u2014 <i>редкое</i>\n\n"
        "<b>I asmenuot\u0117: dirbti (работать)</b>\n\n"
        "         Esam.    B\u016bt.kart.  B\u016bsim.\n"
        "a\u0161      dirbU    dirbAU     dirbSIU\n"
        "tu      dirbI    dirbAI     dirbSI\n"
        "jis/ji  dirbA    dirbO      dirbS\n"
        "mes     dirbAME  dirbOME    dirbSIME\n"
        "j\u016bs     dirbATE  dirbOTE    dirbSITE\n"
        "jie/jos dirbA    dirbO      dirbS"
    ),
    # Page 2 - II conjugation
    (
        "<b>II asmenuot\u0117: myl\u0117ti (любить)</b>\n\n"
        "         Esam.    B\u016bt.kart.    B\u016bsim.\n"
        "a\u0161      mylIU    myl\u0117jAU      myl\u0117SIU\n"
        "tu      mylI     myl\u0117jAI      myl\u0117SI\n"
        "jis/ji  mylI     myl\u0117jO       myl\u0117S\n"
        "mes     mylIME   myl\u0117jOME     myl\u0117SIME\n"
        "j\u016bs     mylITE   myl\u0117jOTE     myl\u0117SITE\n"
        "jie/jos mylI     myl\u0117jO       myl\u0117S"
    ),
    # Page 3 - reflexive verbs
    (
        "<b>Sangr\u0105\u017einiai veiksma\u017eod\u017eiai / Возвратные глаголы</b>\n\n"
        "В русском -ся всегда в конце. В литовском -si- вставляется "
        "<b>перед окончанием</b> или после приставки!\n\n"
        "praustis = мыться \u2192 a\u0161 prausIUOsi\n"
        "mokytis = учиться \u2192 a\u0161 mokAUsi\n"
        "С приставкой: nuSIprausti \u2192 a\u0161 nuSIprausiu\n\n"
        "<i>Приставка + SI + корень. Без приставки: корень + окончание + SI.</i>\n\n"
        "<b>Спряжение: mokytis (учиться)</b>\n\n"
        "         Esam.     B\u016bt.      B\u016bs.         Tariam.\n"
        "a\u0161      mokAUsi   moktAUsi   mokySIUOsi    moky\u010cIAUsi\n"
        "tu      mokAIsi   mok\u0117AIsi  mokySIEsi     mokyTUMeisi\n"
        "jis/ji  mokOsi    mok\u0117si    mokyS\u012es       mokyT\u0172si\n"
        "mes     mokOM\u0116s   mok\u0117M\u0116s   mokySIM\u0116s     mokyTUM\u0116M\u0116s\n"
        "j\u016bs     mokOT\u0116s   mok\u0117T\u0116s   mokySIT\u0116s     mokyTUM\u0116T\u0116s\n"
        "jie/jos mokOsi    mok\u0117si    mokySis       mokyT\u0172si"
    ),
    # Page 4 - conditional mood (brief)
    (
        "<b>Tariamoji nuosaka / Сослагательное (кратко)</b>\n\n"
        "<b>Самое важное для формальных писем!</b>\n\n"
        "<b>Образование:</b> основа инфинитива + "
        "-\u010diau, -tum, -t\u0173, -tum\u0117me, -tum\u0117te, -t\u0173\n\n"
        "Nor\u0117<b>\u010diau</b> papra\u0161yti... \u2014 Хотел бы попросить...\n"
        "Ar gal\u0117<b>tum\u0117te</b> atsi\u0173sti? \u2014 Не могли бы вы прислать?\n"
        "B\u016b<b>\u010diau</b> d\u0117kingas... \u2014 Был бы благодарен...\n\n"
        "<i>Полную таблицу смотрите в разделе \u201e\u017dinynas \u2192 Nuosakos\u201c</i>"
    ),
]

# -------------------------------------------------------------------
# JUNGTUKAI (союзы) - 3 pages
# -------------------------------------------------------------------
THEORY["jungtukai"] = [
    # Page 1 - coordinating
    (
        "<b>Jungtukai / Союзы</b>\n\n"
        "На экзамене B2 союзы проверяются в заданиях "
        "\u201ekalbos vartojimas\u201c и особенно в \u201era\u0161ymas\u201c.\n\n"
        "<b>Sujungiamieji / Сочинительные</b>\n\n"
        "<b>ir</b> \u2014 и \u2014 Jis dirba <b>ir</b> mokosi.\n"
        "<b>bei</b> \u2014 и, а также \u2014 \u0160iluma <b>bei</b> d\u0117mesys.\n"
        "<b>ar / arba</b> \u2014 или \u2014 Kava <b>ar</b> arbata?\n"
        "<b>bet / ta\u010diau</b> \u2014 но / однако \u2014 Noriu, <b>bet</b> negaliu.\n"
        "<b>o</b> \u2014 а (противопост.) \u2014 Jis dirba, <b>o</b> ji ilsisi.\n"
        "<b>ne tik... bet ir</b> \u2014 не только... но и\n"
        "<b>tiek... tiek</b> \u2014 как... так и"
    ),
    # Page 2 - subordinating
    (
        "<b>Prijungiamieji / Подчинительные союзы</b>\n\n"
        "<b>kad</b> \u2014 что / чтобы \u2014 \u017dinau, <b>kad</b> jis ateis.\n"
        "<b>nes / kadangi</b> \u2014 потому что \u2014 Neat\u0117jau, <b>nes</b> sirgau.\n"
        "<b>nors</b> \u2014 хотя \u2014 <b>Nors</b> lyja, eisime.\n"
        "<b>jeigu / jei</b> \u2014 если \u2014 <b>Jei</b> nor\u0117si, ateik.\n"
        "<b>kai</b> \u2014 когда \u2014 <b>Kai</b> baigsi, paskambink.\n"
        "<b>kol</b> \u2014 пока \u2014 <b>Kol</b> lauki, paskaityk.\n"
        "<b>tod\u0117l / d\u0117l to</b> \u2014 поэтому \u2014 Sirgau, <b>tod\u0117l</b> neat\u0117jau.\n"
        "<b>kuris / kuri</b> \u2014 который \u2014 \u017dmogus, <b>kuris</b> at\u0117jo..."
    ),
    # Page 3 - punctuation rule
    (
        "<b>Главное правило пунктуации с союзами</b>\n\n"
        "Перед подчинительными союзами <b>ВСЕГДА</b> ставится запятая:\n"
        "kad, nes, nors, jei, kai, kol, kuris\n\n"
        "\u017dinau<b>,</b> kad jis ateis.\n"
        "Neat\u0117jau<b>,</b> nes sirgau.\n"
        "\u017dmogus<b>,</b> kuris \u010dia gyvena<b>,</b> yra mano draugas.\n\n"
        "<i>В русском то же правило: перед \u201eчто, потому что, хотя, "
        "если, когда, который\u201c \u2014 запятая.</i>"
    ),
]

# -------------------------------------------------------------------
# \u017dOD\u017dI\u0172 DARYBA (словообразование) - 3 pages
# -------------------------------------------------------------------
THEORY["zodziu_daryba"] = [
    # Page 1 - prefixes
    (
        "<b>\u017dod\u017ei\u0173 daryba / Словообразование</b>\n\n"
        "В заданиях экзамена часто нужно выбрать из слов с одним корнем, "
        "но разными суффиксами/приставками.\n\n"
        "<b>Основные приставки (prie\u0161d\u0117liai)</b>\n\n"
        "<b>ne-</b> \u2014 не (отрицание): geras \u2192 NEgeras\n"
        "<b>per-</b> \u2014 через, пере-: PERskaityti (прочитать)\n"
        "<b>i\u0161-</b> \u2014 из, вы-: I\u0160eiti (выйти)\n"
        "<b>su-</b> \u2014 с, со-: SUrinkti (собрать)\n"
        "<b>pa-</b> \u2014 по- (немного): PAskaityti (почитать)\n"
        "<b>at-</b> \u2014 от-, обратно: ATeiti (прийти)\n"
        "<b>pra-</b> \u2014 про-: PRAeiti (пройти)\n"
        "<b>nu-</b> \u2014 с-, у-: NUeiti (уйти)\n"
        "<b>pri-</b> \u2014 при-: PRIeiti (подойти)\n"
        "<b>u\u017e-</b> \u2014 за-: U\u017ddaryti (закрыть)"
    ),
    # Page 2 - suffixes for nouns
    (
        "<b>Основные суффиксы для существительных</b>\n\n"
        "<b>-umas</b> \u2014 абстрактное качество (от прилаг.):\n"
        "  gra\u017eus \u2192 gra\u017eUMAS (красота)\n"
        "  sveikas \u2192 sveikUMAS\n\n"
        "<b>-imas</b> \u2014 процесс / действие (от глаг.):\n"
        "  mokyti \u2192 mokyMAS (обучение)\n"
        "  skaityti \u2192 skaityMAS (чтение)\n\n"
        "<b>-tojas/-toja</b> \u2014 деятель (от глаг.):\n"
        "  mokyti \u2192 mokyTOJAS (учитель)\n"
        "  skaityti \u2192 skaityTOJAS (читатель)\n\n"
        "<b>-\u0117jas/-\u0117ja</b> \u2014 деятель (разновидность):\n"
        "  si\u0173sti \u2192 siunt\u0116JAS (отправитель)\n"
        "  pirkti \u2192 pirk\u0116JAS (покупатель)"
    ),
    # Page 3 - adjective suffixes
    (
        "<b>Суффиксы для прилагательных</b>\n\n"
        "<b>-inis/-in\u0117</b> \u2014 относительное прилаг.:\n"
        "  medicina \u2192 medicinINIS (медицинский)\n"
        "  sportas \u2192 sportINIS (спортивный)\n\n"
        "<b>-ingas/-inga</b> \u2014 обладающий качеством:\n"
        "  r\u016bpestis \u2192 r\u016bpestINGAS (заботливый)\n"
        "  d\u0117mesys \u2192 d\u0117mesINGAS (внимательный)\n\n"
        "<b>Наречия от прилагательных:</b>\n"
        "  -as/-us \u2192 -ai: greitas \u2192 greitAI (быстро)\n"
        "  profesionalus \u2192 profesionalIAI"
    ),
]

# -------------------------------------------------------------------
# SKYRYBA (пунктуация) - 3 pages
# -------------------------------------------------------------------
THEORY["skyryba"] = [
    # Page 1
    (
        "<b>Skyryba / Пунктуация</b>\n\n"
        "<b>1. Запятая перед подчинительными союзами \u2014 ВСЕГДА</b>\n\n"
        "Перед <b>kad, nes, nors, jei/jeigu, kai, kol, kuris/kuri, kur, kaip</b> "
        "всегда ставится запятая:\n\n"
        "\u017dinau<b>,</b> kad jis ateis.\n"
        "Neat\u0117jau<b>,</b> nes sirgau.\n"
        "\u017dmogus<b>,</b> kuris \u010dia gyvena<b>,</b> yra mano draugas.\n\n"
        "<i>Совпадает с русским!</i>"
    ),
    # Page 2
    (
        "<b>2. Причастные обороты (dalyvini\u0173 aplinkybi\u0173)</b>\n\n"
        "Причастный оборот <b>ПОСЛЕ</b> определяемого слова \u2014 запятые:\n"
        "\u017dmogus<b>,</b> skaitantis knyg\u0105<b>,</b> s\u0117d\u0117jo ant suolo.\n\n"
        "Причастный оборот <b>ПЕРЕД</b> определяемым словом \u2014 <b>БЕЗ</b> запятой:\n"
        "Skaitantis knyg\u0105 \u017emogus s\u0117d\u0117jo ant suolo.\n\n"
        "<b>3. Pusdalyvis и padalyvis</b>\n\n"
        "Обороты с pusdalyvis (-damas/-dama) и padalyvis выделяются запятыми:\n"
        "<b>Gr\u012f\u017edamas namo,</b> jis pamat\u0117 kaimyn\u0105.\n"
        "<b>Baigusi darb\u0105,</b> ji i\u0161\u0117jo namo.\n\n"
        "<i>Как в русском: деепричастные обороты всегда выделяются запятыми.</i>"
    ),
    # Page 3
    (
        "<b>4. Однородные члены</b>\n\n"
        "Запятая между однородными членами без союза:\n"
        "Jis pirko duonos<b>,</b> pieno<b>,</b> sviesto ir kiau\u0161ini\u0173.\n\n"
        "Перед одиночным <b>ir/bei</b> запятая <b>НЕ</b> ставится.\n"
        "Но перед повторяющимся <b>ir... ir</b> \u2014 ставится:\n"
        "<b>Ir</b> vaikai<b>,</b> <b>ir</b> suaugusieji dalyvavo.\n\n"
        "<b>5. Прямая речь</b>\n\n"
        "Jis pasak\u0117: \u201eA\u0161 ateisiu rytoj.\u201c\n"
        "\u201eA\u0161 ateisiu rytoj\u201c, \u2013 pasak\u0117 jis.\n\n"
        "<i>Кавычки в литовском \u201e \u201c (внизу-вверху), а не \u00ab \u00bb как в русском.</i>"
    ),
]

# -------------------------------------------------------------------
# NUOSAKOS (наклонения) - 3 pages
# -------------------------------------------------------------------
THEORY["nuosakos"] = [
    # Page 1 - conditional
    (
        "<b>Tariamoji nuosaka / Сослагательное наклонение</b>\n\n"
        "<b>Критически важно для B2!</b> Используется в формальных письмах, "
        "просьбах, условных предложениях.\n\n"
        "<b>Образование:</b> основа инф. + "
        "-\u010diau, -tum, -t\u0173, -tum\u0117me, -tum\u0117te, -t\u0173\n\n"
        "          dirbti    ra\u0161yti    myl\u0117ti\n"
        "a\u0161       dirb\u010cIAU  ra\u0161y\u010cIAU  myl\u0117\u010cIAU\n"
        "tu       dirbTUM   ra\u0161yTUM   myl\u0117TUM\n"
        "jis/ji   dirbT\u0172    ra\u0161yT\u0172    myl\u0117T\u0172\n"
        "mes      dirbTUM\u0116ME ra\u0161yTUM\u0116ME myl\u0117TUM\u0116ME\n"
        "j\u016bs      dirbTUM\u0116TE ra\u0161yTUM\u0116TE myl\u0117TUM\u0116TE\n"
        "jie/jos  dirbT\u0172    ra\u0161yT\u0172    myl\u0117T\u0172"
    ),
    # Page 2 - usage + conditional sentences
    (
        "<b>Использование в формальных письмах</b>\n\n"
        "Nor\u0117<b>\u010diau</b> papra\u0161yti informacijos.\n"
        "\u2014 Хотел бы попросить информацию.\n\n"
        "B\u016b<b>\u010diau</b> d\u0117kingas, jei gal\u0117<b>tum\u0117te</b> atsi\u0173sti.\n"
        "\u2014 Был бы благодарен, если бы вы могли прислать.\n\n"
        "Ar gal\u0117<b>tum\u0117te</b> man pad\u0117ti?\n"
        "\u2014 Не могли бы вы мне помочь?\n\n"
        "<b>Условные предложения:</b>\n"
        "<b>Реальное</b> (буд.): Jei <b>tur\u0117siu</b> laiko, <b>ateisiu</b>.\n"
        "<b>Нереальное</b> (бы): Jei <b>tur\u0117\u010diau</b> laiko, <b>atei\u010diau</b>.\n"
        "<b>Нереальное в прош.</b>: Jei <b>b\u016b\u010diau tur\u0117j\u0119s</b>, <b>b\u016b\u010diau at\u0117j\u0119s</b>."
    ),
    # Page 3 - imperative + indirect
    (
        "<b>Liepiamoji nuosaka / Повелительное наклонение</b>\n\n"
        "          dirbti  ra\u0161yti  eiti   skaityti\n"
        "tu       dirbK   ra\u0161yK   eiK    skaityK\n"
        "j\u016bs      dirbKITE ra\u0161yKITE eiKITE skaityKITE\n"
        "mes      dirbKIME ra\u0161yKIME eiKIME skaityKIME\n\n"
        "Вежливая просьба: Pra\u0161au, <b>ra\u0161ykite</b> ai\u0161kiai.\n"
        "Ещё вежливее: Ar <b>gal\u0117tum\u0117te</b> para\u0161yti?\n\n"
        "<b>Netiesiogin\u0117 nuosaka / Косвенное (пересказательное)</b>\n\n"
        "Используется для передачи чужих слов (в рус. нет аналога).\n\n"
        "Jis <b>dirb\u0105s</b> \u0161ioje \u012fmon\u0117je. \u2014 (Говорят,) он работает...\n"
        "Ji <b>buvusi</b> gera mokin\u0117. \u2014 (Говорят,) она была...\n"
        "Jie <b>atvyksi\u0105</b> rytoj. \u2014 (Говорят,) они приедут...\n\n"
        "<i>Формы: esam. \u2192 -\u0105s/-anti, b\u016bt. \u2192 -\u0119s/-usi, "
        "b\u016bs. \u2192 -si\u0105s/-sianti.</i>"
    ),
]

# -------------------------------------------------------------------
# PASYVAS (пассивный залог) - 2 pages
# -------------------------------------------------------------------
THEORY["pasyvas"] = [
    # Page 1
    (
        "<b>Neveikiamoji r\u016b\u0161is / Пассивный залог</b>\n\n"
        "Пассив очень распространён в формальных и публицистических "
        "текстах \u2014 именно тех, что на экзамене.\n\n"
        "<b>1. Neveikiamasis dalyvis + b\u016bti</b>\n"
        "<b>Наст.:</b> Lai\u0161kas <b>yra ra\u0161omas</b>. \u2014 Письмо пишется.\n"
        "<b>Прош.:</b> Lai\u0161kas <b>buvo para\u0161ytas</b>. \u2014 Письмо было написано.\n"
        "<b>Буд.:</b> Lai\u0161kas <b>bus para\u0161ytas</b>. \u2014 Письмо будет написано.\n\n"
        "Причастие согласуется с подлежащим:\n"
        "Knyga <b>buvo para\u0161yta</b>. (ж.р.)\n"
        "Dokumentai <b>buvo paruo\u0161ti</b>. (мн.ч.)\n\n"
        "<b>2. Безличный пассив (самый частый!)</b>\n"
        "\u010cia <b>kalbama</b> lietuvi\u0161kai. \u2014 Здесь говорят по-литовски.\n"
        "<b>Buvo nuspr\u0119sta</b> atid\u0117ti pos\u0117d\u012f. \u2014 Было решено отложить.\n"
        "<b>Planuojama</b> statyti nauj\u0105 mokykl\u0105. \u2014 Планируется построить.\n\n"
        "<i>Безличное причастие ср. рода на -ma (наст.) или -ta (прош.).</i>"
    ),
    # Page 2
    (
        "<b>Пассив с деятелем + безличные конструкции</b>\n\n"
        "<b>3. Деятель \u2014 через Kilmininkas!</b>\n"
        "\u0160i knyga <b>para\u0161yta mokslininko</b>. \u2014 Написана учёным.\n"
        "<b>Gyventoj\u0173</b> buvo surinkti para\u0161ai. \u2014 Жителями собраны подписи.\n\n"
        "<i>В русском деятель в тв. п. (написана КЕМ?). "
        "В литовском \u2014 в родительном (KO?)! Частая ошибка!</i>\n\n"
        "<b>Конструкция galima / reikia / b\u016btina</b>\n\n"
        "<b>galima</b> + инф. = можно\n"
        "<b>negalima</b> + инф. = нельзя\n"
        "<b>reikia</b> + инф. = нужно, надо\n"
        "<b>b\u016btina</b> + инф. = необходимо\n"
        "<b>verta</b> + инф. = стоит\n"
        "<b>draud\u017eiama</b> + инф. = запрещается\n\n"
        "<b>Galima</b> u\u017esiregistruoti internetu. \u2014 Можно зарегистрироваться.\n"
        "<b>Reikia</b> pateikti dokumentus. \u2014 Нужно предоставить.\n"
        "<b>Draud\u017eiama</b> r\u016bkyti. \u2014 Запрещается курить."
    ),
]

# -------------------------------------------------------------------
# B\u016aDVARD\u017dIAI (прилагательные - степени сравнения) - 2 pages
# -------------------------------------------------------------------
THEORY["budvardziai"] = [
    # Page 1 - comparative
    (
        "<b>B\u016bdvard\u017ei\u0173 laipsniai / Степени сравнения</b>\n\n"
        "<b>Auk\u0161tesnysis laipsnis (сравнительная): -esnis/-esn\u0117</b>\n\n"
        "didelis (большой) \u2192 didESNIS / didESN\u0116\n"
        "ma\u017eas (маленький) \u2192 ma\u017eESNIS\n"
        "geras (хороший) \u2192 gerESNIS\n"
        "blogas (плохой) \u2192 blogESNIS\n"
        "senas (старый) \u2192 senESNIS\n"
        "gra\u017eus (красивый) \u2192 gra\u017eESNIS\n"
        "svarbus (важный) \u2192 svarbESNIS\n"
        "ilgas (длинный) \u2192 ilgESNIS\n\n"
        "<b>Конструкции сравнения:</b>\n"
        "<b>u\u017e + G.:</b> Jis <b>vyresnis u\u017e</b> mane.\n"
        "<b>nei / negu:</b> Jis vyresnis <b>nei</b> a\u0161.\n"
        "<b>kuo... tuo...:</b> <b>Kuo</b> daugiau mokosi, <b>tuo</b> geriau supranta.\n"
        "\u2014 Чем больше учится, тем лучше понимает."
    ),
    # Page 2 - superlative + adverbs
    (
        "<b>Auk\u0161\u010diausiasis laipsnis (превосходная): -iausias/-iausia</b>\n\n"
        "didelis \u2192 did\u017dIAUSIAS / did\u017dIAUSIA\n"
        "geras \u2192 gerIAUSIAS / gerIAUSIA\n"
        "gra\u017eus \u2192 gra\u017eIAUSIAS\n"
        "svarbus \u2192 svarbIAUSIAS\n"
        "blogas \u2192 blogIAUSIAS\n\n"
        "<i>Превосходная степень склоняется! "
        "Geriausiam draugui (лучшему другу, N.).</i>\n\n"
        "<b>Наречия: степени сравнения</b>\n\n"
        "gerai (хорошо) \u2192 gerIAU \u2192 gerIAUSIAI\n"
        "blogai (плохо) \u2192 blogIAU \u2192 blogIAUSIAI\n"
        "greitai (быстро) \u2192 greitIAU \u2192 greitIAUSIAI\n"
        "daug (много) \u2192 daugIAU \u2192 daugIAUSIAI\n"
        "ma\u017eai (мало) \u2192 ma\u017eIAU \u2192 ma\u017eIAUSIAI\n\n"
        "<i>Наречия: сравн. на -iau, превосх. на -iausiai. Не склоняются!</i>"
    ),
]

# -------------------------------------------------------------------
# VALDYMAS (управление глаголов) - 2 pages
# -------------------------------------------------------------------
THEORY["valdymas"] = [
    # Page 1
    (
        "<b>Veiksma\u017eod\u017ei\u0173 valdymas / Управление глаголов</b>\n\n"
        "Многие литовские глаголы требуют других падежей, "
        "чем аналогичные русские! Это самый частый источник ошибок.\n\n"
        "<b>+ Kilmininkas (род.):</b>\n"
        "mokytis (учить что) + K.: mokytis <b>kalbos</b>\n"
        "klausyti (слушать) + K.: klausyti <b>muzikos</b>\n"
        "ie\u0161koti (искать) + K.: ie\u0161koti <b>darbo</b>\n"
        "laukti (ждать) + K.: laukti <b>autobuso</b>\n"
        "pra\u0161yti (просить) + K.: pra\u0161yti <b>pagalbos</b>\n"
        "link\u0117ti (желать) + K.: link\u0117ti <b>s\u0117km\u0117s</b>\n"
        "vengti (избегать) + K.: vengti <b>klaid\u0173</b>\n"
        "tik\u0117tis (надеяться) + K.: tik\u0117tis <b>pagalbos</b>\n\n"
        "<i>В русском многие из этих глаголов + ЧТО/КОГО (вин.), "
        "а в литовском \u2014 Kilmininkas!</i>"
    ),
    # Page 2
    (
        "<b>Управление глаголов (продолжение)</b>\n\n"
        "<b>+ \u012enagininkas (тв.):</b>\n"
        "d\u017eiaugtis (радоваться): d\u017eiaugtis <b>gyvenimu</b>\n"
        "naudotis (пользоваться): naudotis <b>internetu</b>\n"
        "dom\u0117tis (интересоваться): dom\u0117tis <b>menu</b>\n"
        "r\u016bpintis (заботиться): r\u016bpintis <b>vaikais</b>\n\n"
        "<b>+ Galininkas (вин.):</b>\n"
        "skatinti (побуждать): skatinti <b>pl\u0117tr\u0105</b>\n"
        "mokyti (учить кого): mokyti <b>vaikus</b>\n"
        "myl\u0117ti (любить): myl\u0117ti <b>t\u0117vyn\u0119</b>\n\n"
        "<b>+ Naudininkas (дат.):</b>\n"
        "pad\u0117koti (поблагодарить): pad\u0117koti <b>draugui</b>\n"
        "pad\u0117ti (помочь): pad\u0117ti <b>draugui</b>\n"
        "skambinti (звонить): skambinti <b>mamai</b>\n\n"
        "<i>Правило: если в русском глагол + ЧТО/КОГО (вин.), "
        "в литовском часто Kilmininkas (род.)!</i>"
    ),
]

# -------------------------------------------------------------------
# PRIELINKSNIAI (предлоги) - 2 pages
# -------------------------------------------------------------------
THEORY["prielinksniai"] = [
    # Page 1 - K. and G.
    (
        "<b>Prielinksniai / Предлоги и их управление</b>\n\n"
        "<b>+ Kilmininkas (родительный) \u2014 большинство!</b>\n\n"
        "<b>ant</b> (на поверхности): ant <b>stalo</b>\n"
        "<b>i\u0161</b> (из): i\u0161 <b>miesto</b>\n"
        "<b>nuo</b> (от, с): nuo <b>ryto</b>\n"
        "<b>iki</b> (до): iki <b>vakaro</b>\n"
        "<b>prie</b> (у, около): prie <b>namo</b>\n"
        "<b>be</b> (без): be <b>vandens</b>\n"
        "<b>d\u0117l</b> (из-за): d\u0117l <b>ligos</b>\n"
        "<b>po</b> (после): po <b>darbo</b>\n"
        "<b>tarp</b> (между): tarp <b>nam\u0173</b>\n"
        "<b>\u0161alia</b> (рядом): \u0161alia <b>mokyklos</b>\n"
        "<b>vietoj</b> (вместо): vietoj <b>man\u0119s</b>\n"
        "<b>anot</b> (по мнению): anot <b>mokslininko</b>\n\n"
        "<b>+ Galininkas (винительный)</b>\n\n"
        "<b>\u012f</b> (в, куда): \u012f <b>miest\u0105</b>\n"
        "<b>per</b> (через, за): per <b>savait\u0119</b>\n"
        "<b>apie</b> (о, про): apie <b>darb\u0105</b>\n"
        "<b>prie\u0161</b> (перед, против): prie\u0161 <b>metus</b>\n"
        "<b>u\u017e</b> (за, чем): u\u017e <b>namo</b>\n"
        "<b>pas</b> (у/к человеку): pas <b>draug\u0105</b>\n"
        "<b>pro</b> (мимо): pro <b>lang\u0105</b>"
    ),
    # Page 2 - In. + critical differences
    (
        "<b>+ \u012enagininkas (творительный)</b>\n\n"
        "<b>su</b> (с): su <b>draugu</b>\n"
        "<b>po</b> (под): po <b>stalu</b>\n"
        "<b>ties</b> (у, напротив): ties <b>namu</b>\n\n"
        "<b>Критические отличия от русского!</b>\n\n"
        "<b>apie</b> (о, про) + <b>Galininkas</b>\n"
        "\u2014 в русском \u201eо\u201c + предложный!\n\n"
        "<b>pas</b> (у/к человеку) + <b>Galininkas</b>\n"
        "\u2014 в русском \u201eк\u201c + дательный!\n\n"
        "<b>po</b> = 2 значения: \u201eпосле\u201c + K., \u201eпод\u201c + \u012en. (омоним!)\n\n"
        "<b>tarp</b> (между) + <b>Kilmininkas</b>\n"
        "\u2014 в русском \u201eмежду\u201c + творительный!\n\n"
        "<i>Запомните: большинство предлогов \u2192 Kilmininkas! "
        "Только \u012f, per, apie, prie\u0161, u\u017e, pas, pro \u2192 Galininkas. "
        "Su, po (под), ties \u2192 \u012enagininkas.</i>"
    ),
]

# -------------------------------------------------------------------
# \u012eVARDIS (местоимения) - 2 pages
# -------------------------------------------------------------------
THEORY["ivardis"] = [
    # Page 1 - personal pronouns
    (
        "<b>Asmeniniai \u012fvard\u017eiai / Личные местоимения</b>\n\n"
        "     a\u0161   tu    jis   ji    mes   j\u016bs   jie   jos\n"
        "V.  a\u0161   tu    jis   ji    mes   j\u016bs   jie   jos\n"
        "K.  man\u0119s tav\u0119s jo    jos   m\u016bs\u0173  j\u016bs\u0173  j\u0173    j\u0173\n"
        "N.  man   tau   jam   jai   mums  jums  jiems joms\n"
        "G.  mane  tave  j\u012f    j\u0105    mus   jus   juos  jas\n"
        "\u012en. manimi tavimi juo  ja    mumis jumis jais  jomis\n"
        "Vt. manyje tavyje jame joje  mumyse jumyse juose jose"
    ),
    # Page 2 - possessive + relative
    (
        "<b>Savybiniai \u012fvard\u017eiai / Притяжательные</b>\n\n"
        "a\u0161 \u2192 <b>mano</b> (мой)\n"
        "tu \u2192 <b>tavo</b> (твой)\n"
        "jis \u2192 <b>jo</b> (его)\n"
        "ji \u2192 <b>jos</b> (её)\n"
        "mes \u2192 <b>m\u016bs\u0173</b> (наш)\n"
        "j\u016bs \u2192 <b>j\u016bs\u0173</b> (ваш)\n"
        "jie/jos \u2192 <b>j\u0173</b> (их)\n"
        "<b>savo</b> \u2014 свой (принадлежит подлежащему)\n\n"
        "<b>Важно: savo vs jo/jos</b>\n"
        "Jis myli <b>savo</b> mam\u0105. \u2014 свою маму (собственную)\n"
        "Jis myli <b>jo</b> mam\u0105. \u2014 его маму (чужую!)\n\n"
        "<b>Santykiniai: kuris/kuri = который</b>\n\n"
        "     Vyr.vns  Mot.vns  Vyr.dgs  Mot.dgs\n"
        "V.  kuris    kuri     kurie    kurios\n"
        "K.  kurio    kurios   kuri\u0173    kuri\u0173\n"
        "N.  kuriam   kuriai   kuriems  kurioms\n"
        "G.  kur\u012f     kuri\u0105    kuriuos  kurias\n"
        "\u012en. kuriuo   kuria    kuriais  kuriomis\n"
        "Vt. kuriame  kurioje  kuriuose kuriose"
    ),
]


# ===================================================================
# EXERCISES
# ===================================================================
EXERCISES = {}

# -------------------------------------------------------------------
# DALYVIAI Drill 1 - Formation (16 choice)
# -------------------------------------------------------------------
EXERCISES["dalyviai_1"] = [
    _c(
        "Образуйте <b>veikiam\u0105j\u012f esamojo laiko dalyv\u012f</b> "
        "(действ. прич. наст. вр.) от глагола <b>dirbti</b> (работать), м.р., ед.ч.:",
        ["dirbantis", "dirb\u0119s", "dirbamas", "dirbdamas"], 0,
        hint="3-е лицо наст. вр.: dirba \u2192 dirb + antis",
        explanation="dirba \u2192 dirb-antis. I спряжение, поэтому -antis.",
        ru="Работающий. Образование: от 3-го лица настоящего времени.",
        topic="Veik. esam.",
    ),
    _c(
        "Veikiamasis <b>b\u016btojo kartinio</b> laiko dalyvis от <b>ra\u0161yti</b> (писать), ж.р.:",
        ["ra\u0161iusi", "ra\u0161anti", "ra\u0161oma", "ra\u0161ydama"], 0,
        hint="Основа прош. вр.: ra\u0161\u0117 \u2192 ra\u0161 + iusi",
        explanation="ra\u0161\u0117 \u2192 ra\u0161-iusi (\u0436.р.). Написавшая.",
        ru="Написавшая. Прошедшее однократное.",
        topic="Veik. b\u016bt. kart.",
    ),
    _c(
        "Neveikiamasis <b>esamojo</b> laiko dalyvis от <b>statyti</b> (строить), м.р.:",
        ["statomas", "stat\u0119s", "statantis", "statytas"], 0,
        hint="Страдательное причастие наст. вр.: -omas/-oma",
        explanation="statyti \u2192 stat-omas. Строимый.",
        ru="Строимый / строящийся. Страд. прич. наст. вр.",
        topic="Neveik. esam.",
    ),
    _c(
        "Neveikiamasis <b>b\u016btojo</b> laiko dalyvis от <b>para\u0161yti</b> (написать), ж.р.:",
        ["para\u0161yta", "para\u0161oma", "para\u0161anti", "para\u0161iusi"], 0,
        hint="Страд. прич. прош. вр.: -ytas/-yta",
        explanation="para\u0161yti \u2192 para\u0161-yta. Написанная.",
        ru="Написанная. Самый частый тип причастия в текстах!",
        topic="Neveik. b\u016bt.",
    ),
    _c(
        "<b>Pusdalyvis</b> от <b>eiti</b> (идти), м.р.:",
        ["eidamas", "eidama", "einantis", "\u0117j\u0119s"], 0,
        hint="Pusdalyvis = основа инфинитива + -damas/-dama",
        explanation="ei-ti \u2192 ei-damas. Идя (о мужчине).",
        ru="Идя. Аналог деепричастия, но согласуется по роду!",
        topic="Pusdalyvis",
    ),
    _c(
        "Neveikiamasis <b>b\u016bsimojo</b> laiko dalyvis от <b>skaityti</b> (читать), м.р.:",
        ["skaitysimas", "skaitomas", "skaitytas", "skaitantis"], 0,
        hint="Будущее страдательное: -ysimas/-ysima",
        explanation="skaityti \u2192 skait-ysimas. Тот, что будет прочитан.",
        ru="То, что будет прочитано. Редкая форма.",
        topic="Neveik. b\u016bs.",
    ),
    _c(
        "Veikiamasis esamojo laiko dalyvis от <b>myl\u0117ti</b> (любить), ж.р. <i>(II спряжение!)</i>:",
        ["mylinti", "mylanti", "mylima", "myliusi"], 0,
        hint="II спряжение: myli \u2192 myl-intis/-inti (не -antis!)",
        explanation="myli \u2192 myl-inti. II спряжение \u2192 -intis/-inti.",
        ru="Любящая. II спряжение: -intis/-inti, а не -antis/-anti!",
        topic="Veik. esam. II",
    ),
    _c(
        "<b>Padalyvis</b> от <b>perskaityti</b> (прочитать):",
        ["perskai\u010dius", "perskaitydamas", "perskait\u0119s", "perskaitomas"], 0,
        hint="Padalyvis прош. вр. = основа прош. вр. + -us/-ius",
        explanation="perskait\u0117 \u2192 perskai\u010d-ius. Прочитав.",
        ru="Прочитав. Деепричастие сов. вида.",
        topic="Padalyvis",
    ),
    _c(
        "Veikiamasis <b>b\u016btojo da\u017eninio</b> laiko dalyvis от <b>vaik\u0161\u010dioti</b> (гулять), м.р.:",
        ["vaik\u0161\u010diodav\u0119s", "vaik\u0161\u010diojantis", "vaik\u0161\u010dioj\u0119s", "vaik\u0161\u010diojamas"], 0,
        hint="B\u016btasis da\u017eninis = многократное прошедшее. Основа + -dav\u0119s",
        explanation="vaik\u0161\u010dioti \u2192 vaik\u0161\u010dio-dav\u0119s. Тот, кто обычно гулял.",
        ru="Нет аналога в русском \u2014 передаёт привычное действие в прошлом.",
        topic="Veik. b\u016bt. da\u017en.",
    ),
    _c(
        "Какое причастие в предложении: <i>\u201eVaikai, <b>\u017eaid\u017eiantys</b> kieme, buvo linksmi.\u201c</i>?",
        ["Veikiamasis esamojo laiko", "Neveikiamasis esamojo laiko", "Pusdalyvis", "Padalyvis"], 0,
        hint="\u017eaid\u017eiantys = играющие (кто? \u2014 действующее лицо)",
        explanation="\u017eaid\u017eiantys \u2014 veik. esam. laiko dalyvis (dgs., V.).",
        ru="Играющие \u2014 действ. прич. наст. вр., мн.ч., им.п.",
        topic="Atpa\u017einimas",
    ),
    _c(
        "Veikiamasis esamojo laiko dalyvis от <b>tur\u0117ti</b> (иметь), м.р. <i>(II спр.)</i>:",
        ["turintis", "turantis", "turimas", "tur\u0117j\u0119s"], 0,
        hint="II спряжение: turi \u2192 tur-intis",
        explanation="turi \u2192 tur-intis. II спряжение \u2192 -intis.",
        ru="Имеющий. II спряжение \u2014 окончание -intis!",
        topic="Veik. esam. II",
    ),
    _c(
        "Neveikiamasis esamojo laiko dalyvis от <b>gerinti</b> (улучшать), ж.р.:",
        ["gerinama", "gerinanti", "gerinusi", "gerinta"], 0,
        hint="Страдательное наст. вр.: -ama (ж.р.)",
        explanation="gerinti \u2192 gerin-ama. Улучшаемая.",
        ru="Улучшаемая. Страд. прич. наст. вр., женский род.",
        topic="Neveik. esam.",
    ),
    _c(
        "<b>Pusdalyvis</b> от <b>b\u0117gti</b> (бежать), ж.р.:",
        ["b\u0117gdama", "b\u0117gdamas", "b\u0117ganti", "b\u0117gusi"], 0,
        hint="Основа инф. + -dama (ж.р.)",
        explanation="b\u0117g-ti \u2192 b\u0117g-dama. Бежа (о женщине).",
        ru="Бежа. Полупричастие ж.р. \u2014 согласуется с подлежащим.",
        topic="Pusdalyvis",
    ),
    _c(
        "Veikiamasis <b>b\u016bsimojo</b> laiko dalyvis от <b>mokytis</b> (учиться), м.р.:",
        ["mokysiantis", "mokantis", "mok\u0119sis", "mokomas"], 0,
        hint="Будущее действительное: основа буд. + -iantis",
        explanation="mokysis \u2192 moky-siantis. Тот, кто будет учиться.",
        ru="Тот, кто будет учиться. Будущее действительное.",
        topic="Veik. b\u016bs.",
    ),
    _c(
        "Какой тип: <i>\u201e<b>I\u0161girdusi</b> naujien\u0105, ji nustebo.\u201c</i>",
        ["Padalyvis", "Pusdalyvis", "Veik. b\u016bt. kart. dalyvis", "Neveik. dalyvis"], 0,
        hint="I\u0161girdusi \u2014 предшествующее действие, ж.р.",
        explanation="I\u0161girdusi \u2014 padalyvis, mot. gimin\u0117. Услышав.",
        ru="Услышав. Padalyvis \u2014 деепричастие сов. вида.",
        topic="Atpa\u017einimas",
    ),
    _c(
        "Neveikiamasis b\u016btojo laiko dalyvis от <b>i\u0161spr\u0119sti</b> (решить), mot.g., dgs., K.:",
        ["i\u0161spr\u0119st\u0173", "i\u0161spr\u0119stos", "i\u0161spr\u0119stoms", "i\u0161spr\u0119stas"], 0,
        hint="Dgs. Kilmininkas mot.g.: -\u0173",
        explanation="i\u0161spr\u0119st\u0173 \u2014 neveik. b\u016bt. laiko, dgs., K. Решённых.",
        ru="Решённых. Мн.ч., род.п. Причастие склоняется как прилагательное!",
        topic="Neveik. b\u016bt. + linksniai",
    ),
]

# -------------------------------------------------------------------
# DALYVIAI Drill 2 - Context (12 input)
# -------------------------------------------------------------------
EXERCISES["dalyviai_2"] = [
    _i(
        "Вставьте правильную форму причастия.\n\n"
        "<i>\u201eMoteris, _____ (skaityti, veik. esam., mot.) knyg\u0105, s\u0117d\u0117jo ant suolo.\u201c</i>\n\n"
        "Женщина, <u>читающая</u> книгу, сидела на скамейке.",
        ["skaitanti", "skaitan\u010dia"],
        hint="Veikiamasis esamojo laiko, mot. gimin\u0117, vardininkas",
        explanation="skaitanti \u2014 veik. esam. laiko dalyvis, mot. gimin\u0117, vns., V.",
        ru="Читающая. Женский род, именительный падеж.",
    ),
    _i(
        "<i>\u201e_____ (gr\u012f\u017eti, pusdalyvis, vyr.) namo, jis pamat\u0117 kaimyn\u0105.\u201c</i>\n\n"
        "<u>Возвращаясь</u> домой, он увидел соседа.",
        ["Gr\u012f\u017edamas"],
        hint="Pusdalyvis, vyri\u0161koji gimin\u0117: основа + -damas",
        explanation="Gr\u012f\u017edamas \u2014 pusdalyvis, vyr. gimin\u0117.",
        ru="Возвращаясь. Мужской род, т.к. подлежащее \u201ejis\u201c.",
    ),
    _i(
        "<i>\u201eLai\u0161kas buvo _____ (para\u0161yti, neveik. b\u016bt.) vakar.\u201c</i>\n\n"
        "Письмо было <u>написано</u> вчера.",
        ["para\u0161ytas"],
        hint="Neveikiamasis b\u016btojo laiko: -ytas (vyr. gimin\u0117)",
        explanation="para\u0161ytas \u2014 neveik. b\u016bt. laiko dalyvis. Lai\u0161kas (vyr. g.).",
        ru="Написано/написанный. Согласуется с \u201elai\u0161kas\u201c (м.р.).",
    ),
    _i(
        "<i>\u201e_____ (baigti, padalyvis) darb\u0105, ji i\u0161\u0117jo namo.\u201c</i>\n\n"
        "<u>Закончив</u> работу, она ушла домой.",
        ["Baigusi"],
        hint="Padalyvis прош. вр., mot. gimin\u0117: основа прош. вр. + -usi",
        explanation="Baigusi \u2014 padalyvis. Baig\u0117 \u2192 baig-usi (mot. g.).",
        ru="Закончив. Ж.р., т.к. \u201eji\u201c (она).",
    ),
    _i(
        "<i>\u201e\u0160i knyga yra labai _____ (skaityti, neveik. esam.).\u201c</i>\n\n"
        "Эта книга очень <u>читаемая</u> (популярная).",
        ["skaitoma"],
        hint="Neveikiamasis esamojo laiko, mot. gimin\u0117 (knyga): -oma",
        explanation="skaitoma \u2014 neveik. esam. laiko dalyvis, mot. gimin\u0117.",
        ru="Читаемая. Knyga \u2014 ж.р., поэтому -oma.",
    ),
    _i(
        "<i>\u201eStudentai, _____ (i\u0161laikyti, veik. b\u016bt. kart., dgs.) egzamin\u0105, d\u017eiaug\u0117si.\u201c</i>\n\n"
        "Студенты, <u>сдавшие</u> экзамен, радовались.",
        ["i\u0161laik\u0119"],
        hint="Veik. b\u016btojo kartinio, vyr. gimin\u0117, daugiskaita, V.: -\u0119",
        explanation="i\u0161laik\u0119 \u2014 veik. b\u016bt. kart. dalyvis, vyr. g., dgs., V.",
        ru="Сдавшие. Мн.ч., им.п. В dgs. vyr. g. окончание -\u0119.",
    ),
    _i(
        "<i>\u201e_____ (vairuoti, pusdalyvis, mot.) automobil\u012f, ji klaus\u0117si muzikos.\u201c</i>\n\n"
        "<u>Ведя</u> машину, она слушала музыку.",
        ["Vairuodama"],
        hint="Pusdalyvis, moteri\u0161koji: -dama",
        explanation="Vairuodama \u2014 pusdalyvis, mot. gimin\u0117.",
        ru="Ведя/управляя. Ж.р., т.к. подлежащее \u201eji\u201c.",
    ),
    _i(
        "<i>\u201eTai yra gerai _____ (\u017einoti, neveik. esam.) faktas.\u201c</i>\n\n"
        "Это хорошо <u>известный</u> факт.",
        ["\u017einomas"],
        hint="Neveik. esamojo, vyr. gimin\u0117 (faktas): -omas",
        explanation="\u017einomas \u2014 neveik. esam. laiko dalyvis.",
        ru="Известный / знаемый. Одно из самых частых причастий!",
    ),
    _i(
        "<i>\u201eProblema buvo s\u0117kmingai _____ (i\u0161spr\u0119sti, neveik. b\u016bt., mot.).\u201c</i>\n\n"
        "Проблема была успешно <u>решена</u>.",
        ["i\u0161spr\u0119sta"],
        hint="Neveik. b\u016bt., mot. gimin\u0117 (problema): -ta",
        explanation="i\u0161spr\u0119sta \u2014 neveik. b\u016bt., mot. g.",
        ru="Решена. Problema \u2014 ж.р., поэтому -ta.",
    ),
    _i(
        "<i>\u201eMes mat\u0117me _____ (b\u0117gti, veik. esam., vyr., G.) vaik\u0105.\u201c</i>\n\n"
        "Мы видели <u>бегущего</u> ребёнка.",
        ["b\u0117gant\u012f"],
        hint="Veik. esam., vyr. g., Galininkas (k\u0105?): -ant\u012f",
        explanation="b\u0117gant\u012f \u2014 veik. esam. laiko, vyr. g., G. Mat\u0117me K\u0104?",
        ru="Бегущего. Причастие в вин.п., т.к. mat\u0117me K\u0104?",
    ),
    _i(
        "<i>\u201eTai _____ (padaryti, neveik. b\u016bt.) klaida.\u201c</i>\n\n"
        "Это <u>сделанная</u> ошибка.",
        ["padaryta"],
        hint="Neveik. b\u016bt., mot. gimin\u0117 (klaida): -yta",
        explanation="padaryta \u2014 neveik. b\u016bt. laiko, mot. g.",
        ru="Сделанная. Klaida \u2014 ж.р. \u2192 padaryta.",
    ),
    _i(
        "<i>\u201e_____ (atvykti, padalyvis, vyr.) \u012f Vilni\u0173, jis i\u0161kart \u0117jo \u012f muziej\u0173.\u201c</i>\n\n"
        "<u>Приехав</u> в Вильнюс, он сразу пошёл в музей.",
        ["Atvyk\u0119s"],
        hint="Padalyvis, vyr. gimin\u0117: основа прош. + -\u0119s",
        explanation="Atvyk\u0119s \u2014 padalyvis, vyr. g. Atvyko \u2192 atvyk-\u0119s.",
        ru="Приехав. М.р., т.к. подлежащее \u201ejis\u201c.",
    ),
]

# -------------------------------------------------------------------
# DALYVIAI Drill 3 - Exam format (8 choice)
# -------------------------------------------------------------------
EXERCISES["dalyviai_3"] = [
    _c(
        "<i>\u201e\u0160iemet vykstantis Kauno kino festivalis taps svarbiu _____ "
        "ne tik miestui, bet ir visai Lietuvai.\u201c</i>",
        ["\u012fvykiu", "\u012fvykis", "\u012fvyk\u012f", "\u012fvykyje"], 0,
        hint="taps svarbiu KUO? \u2192 \u012enagininkas",
        explanation="taps svarbiu \u012fvykiu \u2014 tapti + \u012enagininkas.",
        ru="Станет важным ЧЕМ? \u2192 Творительный падеж.",
        topic="Linksniai + kontekstas",
    ),
    _c(
        "<i>\u201eMane su\u017eav\u0117jo slaugytoj\u0173 _____ ir d\u0117mesingumas.\u201c</i>",
        ["r\u016bpestingumas", "r\u016bpestingum\u0105", "r\u016bpestingumo", "r\u016bpestingumu"], 0,
        hint="Kas su\u017eav\u0117jo? \u2192 Vardininkas (подлежащее)",
        explanation="r\u016bpestingumas \u2014 Vardininkas, подлежащее предложения.",
        ru="Что поразило? \u2192 Заботливость (им.п.).",
        topic="Linksniai",
    ),
    _c(
        "<i>\u201e\u017dmoni\u0173, _____ keliauti dvira\u010diais, daug\u0117ja.\u201c</i>\n"
        "Людей, _____ путешествовать на велосипедах, становится больше.",
        ["nusprend\u017eian\u010di\u0173", "nusprend\u017eiantys", "nuspr\u0119st\u0173", "nusprend\u017eian\u010diais"], 0,
        hint="\u017dmoni\u0173 (K.) \u2192 причастие тоже в Kilmininkas, dgs.",
        explanation="nusprend\u017eian\u010di\u0173 \u2014 veik. esam. laiko dalyvis, dgs., Kilmininkas.",
        ru="Решающих. Причастие согласуется с \u201e\u017emoni\u0173\u201c \u2014 род.п., мн.ч.",
        topic="Dalyviai + linksniai",
    ),
    _c(
        "<i>\u201eFestivalio tikslas \u2014 skatinti kino meno _____ .\u201c</i>\n"
        "Цель фестиваля \u2014 способствовать _____ киноискусства.",
        ["pl\u0117tr\u0105", "pl\u0117tra", "pl\u0117tros", "pl\u0117trai"], 0,
        hint="skatinti K\u0104? \u2192 Galininkas",
        explanation="skatinti pl\u0117tr\u0105 \u2014 skatinti + Galininkas (вин.).",
        ru="В русском \u2014 дат., но в литовском skatinti + Galininkas!",
        topic="Linksniai",
    ),
    _c(
        "<i>\u201eNor\u0117\u010diau pad\u0117koti visiems skyriaus administracijos _____ .\u201c</i>\n"
        "Я хотел бы поблагодарить всех _____ администрации.",
        ["darbuotojams", "darbuotojai", "darbuotoj\u0173", "darbuotojus"], 0,
        hint="pad\u0117koti KAM? \u2192 Naudininkas",
        explanation="pad\u0117koti darbuotojams \u2014 pad\u0117koti + Naudininkas (дат.).",
        ru="Поблагодарить КОМУ? \u2192 Дательный.",
        topic="Linksniai",
    ),
    _c(
        "<i>\u201eJ\u0173 _____ mano gydymo procesas buvo sklandus.\u201c</i>\n"
        "Благодаря их _____ процесс лечения был гладким.",
        ["d\u0117ka", "d\u0117kui", "d\u0117l", "d\u0117kas"], 0,
        hint="Благодаря = d\u0117ka (с Kilmininkas)",
        explanation="J\u0173 d\u0117ka \u2014 благодаря им.",
        ru="Благодаря. \u201eD\u0117ka\u201c \u2014 постпозитивный предлог с род.п.",
        topic="Prielinksnis",
    ),
    _c(
        "<i>\u201eKiekvienas gali rasti sau _____ viet\u0105.\u201c</i>\n"
        "Каждый может найти себе _____ место.",
        ["tinkam\u0105", "tinkamas", "tinkanti", "tinkan\u010di\u0105"], 0,
        hint="rasti K\u0104? viet\u0105 \u2192 Galininkas",
        explanation="tinkam\u0105 \u2014 neveik. esam. laiko dalyvis, Galininkas, mot. gimin\u0117.",
        ru="Подходящее. Вин.п., ж.р.",
        topic="Dalyviai vs b\u016bdvard\u017eiai",
    ),
    _c(
        "<i>\u201eGal\u0117dama vie\u0161ai pasidalinti savo gera patirtimi, esu _____ .\u201c</i>\n"
        "Имея возможность поделиться опытом, я _____ .",
        ["d\u0117kinga", "d\u0117kingas", "d\u0117kingai", "d\u0117kingumo"], 0,
        hint="Esu KOKIA? (ji/mot.) \u2192 Vardininkas, mot. gimin\u0117",
        explanation="d\u0117kinga \u2014 b\u016bdvardis, mot. gimin\u0117, V.",
        ru="Благодарна. Ж.р. определяется по \u201egal\u0117dama\u201c (пол.прич. ж.р.).",
        topic="B\u016bdvardis + gimin\u0117",
    ),
]

# -------------------------------------------------------------------
# LINKSNIAI Drill 1 - Case recognition (8 choice)
# -------------------------------------------------------------------
EXERCISES["linksniai_1"] = [
    _c(
        "<i>\u201eA\u0161 gyvenu <b>Vilniuje</b>.\u201c</i>\nОпределите падеж выделенного слова.",
        ["Vietininkas", "Galininkas", "Kilmininkas", "Naudininkas"], 0,
        hint="Kur? Где? \u2192 Vietininkas",
        explanation="Vilniuje \u2014 Vietininkas (местный падеж).",
        ru="Где живёшь? В Вильнюсе. Местный падеж \u2014 без предлога.",
        topic="Vietininkas",
    ),
    _c(
        "<i>\u201eDaviau knyg\u0105 <b>draugui</b>.\u201c</i>\nОпределите падеж.",
        ["Naudininkas", "Galininkas", "Kilmininkas", "\u012enagininkas"], 0,
        hint="Kam? Кому?",
        explanation="draugui \u2014 Naudininkas (дательный). Kam daviau?",
        ru="Кому дал? Другу. Дательный падеж.",
        topic="Naudininkas",
    ),
    _c(
        "<i>\u201eJis ra\u0161o lai\u0161k\u0105 <b>pie\u0161tuku</b>.\u201c</i>\nОпределите падеж слова \u201epie\u0161tuku\u201c.",
        ["\u012enagininkas", "Vietininkas", "Galininkas", "Naudininkas"], 0,
        hint="Kuo? Чем?",
        explanation="pie\u0161tuku \u2014 \u012enagininkas (творительный). Kuo ra\u0161o?",
        ru="Чем пишет? Карандашом. Творительный.",
        topic="\u012enagininkas",
    ),
    _c(
        "<i>\u201e<b>Miesto</b> centras yra gra\u017eus.\u201c</i>\nОпределите падеж слова \u201emiesto\u201c.",
        ["Kilmininkas", "Vardininkas", "Galininkas", "Vietininkas"], 0,
        hint="Ko? Чей? Чего?",
        explanation="miesto \u2014 Kilmininkas (родительный). Ko centras?",
        ru="Чей центр? Города. Родительный.",
        topic="Kilmininkas",
    ),
    _c(
        "<i>\u201eMatau <b>gra\u017ei\u0105 moter\u012f</b>.\u201c</i>\nОпределите падеж.",
        ["Galininkas", "Vardininkas", "Kilmininkas", "\u012enagininkas"], 0,
        hint="K\u0105 matau? Кого вижу?",
        explanation="gra\u017ei\u0105 moter\u012f \u2014 Galininkas (винительный). K\u0105 matau?",
        ru="Кого вижу? Красивую женщину. Винительный.",
        topic="Galininkas",
    ),
    _c(
        "<i>\u201eTai yra mano <b>t\u0117vo</b> automobilis.\u201c</i>\nКакой падеж у слова \u201et\u0117vo\u201c?",
        ["Kilmininkas", "Naudininkas", "Vardininkas", "Galininkas"], 0,
        hint="Ko automobilis? Чья машина?",
        explanation="t\u0117vo \u2014 Kilmininkas. Ko automobilis?",
        ru="Чья машина? Отца. Родительный принадлежности.",
        topic="Kilmininkas",
    ),
    _c(
        "<i>\u201e<b>Vaikai</b> \u017eaid\u017eia parke.\u201c</i>\nКакой падеж у слова \u201evaikai\u201c?",
        ["Vardininkas", "Galininkas", "Naudininkas", "\u0160auksmininkas"], 0,
        hint="Kas \u017eaid\u017eia? Кто играет?",
        explanation="vaikai \u2014 Vardininkas (именительный), подлежащее.",
        ru="Кто играет? Дети. Именительный \u2014 подлежащее.",
        topic="Vardininkas",
    ),
    _c(
        "<i>\u201eEinu <b>\u012f parduotuv\u0119</b>.\u201c</i>\nКакой падеж после предлога \u201e\u012f\u201c?",
        ["Galininkas", "Vietininkas", "Kilmininkas", "Naudininkas"], 0,
        hint="\u012f + K\u0105? Куда? \u2192 Galininkas",
        explanation="\u012f parduotuv\u0119 \u2014 \u012f + Galininkas. Направление.",
        ru="Куда иду? В магазин. \u201e\u012e\u201c всегда с Galininkas!",
        topic="Galininkas",
    ),
]

# -------------------------------------------------------------------
# LINKSNIAI Drill 2 - Endings (8 input)
# -------------------------------------------------------------------
EXERCISES["linksniai_2"] = [
    _i(
        "Поставьте слово <b>miestas</b> в Kilmininkas (K.):\n\n"
        "<i>\u201eTai yra _____ centras.\u201c</i> (Это центр города.)",
        ["miesto"],
        hint="I linksniuot\u0117, -as: K. = -o",
        explanation="miestas \u2192 miesto. I linksniuot\u0117: -as \u2192 -o.",
        ru="Город \u2192 города. Окончание -as \u2192 -o.",
    ),
    _i(
        "Поставьте <b>mokykla</b> в Vietininkas (Vt.):\n\n"
        "<i>\u201eVaikai mokosi _____.\u201c</i> (Дети учатся в школе.)",
        ["mokykloje"],
        hint="III linksniuot\u0117, -a: Vt. = -oje",
        explanation="mokykla \u2192 mokykloje. -a \u2192 -oje.",
        ru="Школа \u2192 в школе. Предлог \u201eв\u201c не нужен!",
    ),
    _i(
        "Поставьте <b>draugas</b> в Naudininkas (N.):\n\n"
        "<i>\u201eNupirkau dovan\u0105 _____.\u201c</i> (Купил подарок другу.)",
        ["draugui"],
        hint="I linksniuot\u0117, -as: N. = -ui",
        explanation="draugas \u2192 draugui. -as \u2192 -ui.",
        ru="Друг \u2192 другу. Окончание -as \u2192 -ui.",
    ),
    _i(
        "Поставьте <b>knyga</b> в Galininkas (G.):\n\n"
        "<i>\u201eSkaitau _____.\u201c</i> (Читаю книгу.)",
        ["knyg\u0105"],
        hint="III linksniuot\u0117, -a: G. = -\u0105",
        explanation="knyga \u2192 knyg\u0105. -a \u2192 -\u0105.",
        ru="Книга \u2192 книгу. Окончание -a \u2192 -\u0105.",
    ),
    _i(
        "Поставьте <b>automobilis</b> в \u012enagininkas (\u012en.):\n\n"
        "<i>\u201eVa\u017eiuoju _____.\u201c</i> (Еду на машине.)",
        ["automobiliu"],
        hint="I linksniuot\u0117, -is: \u012en. = -iu",
        explanation="automobilis \u2192 automobiliu. -is \u2192 -iu.",
        ru="Машина \u2192 машиной. Окончание -is \u2192 -iu.",
    ),
    _i(
        "Поставьте <b>gydytojas</b> в Galininkas, daugiskaita (G., dgs.):\n\n"
        "<i>\u201eMatau _____.\u201c</i> (Вижу врачей.)",
        ["gydytojus"],
        hint="I linksniuot\u0117, -as, dgs.: G. = -us",
        explanation="gydytojas \u2192 gydytojus. Dgs. Galininkas: -us.",
        ru="Врач \u2192 врачей. Мн.ч., вин.п.: -as \u2192 -us.",
    ),
    _i(
        "Поставьте <b>Lietuva</b> в Kilmininkas (K.):\n\n"
        "<i>\u201e_____ istorija yra sena.\u201c</i> (История Литвы древняя.)",
        ["Lietuvos"],
        hint="III linksniuot\u0117, -a: K. = -os",
        explanation="Lietuva \u2192 Lietuvos. -a \u2192 -os.",
        ru="Литва \u2192 Литвы. Окончание -a \u2192 -os.",
    ),
    _i(
        "Поставьте <b>\u017emogus</b> в Naudininkas, daugiskaita (N., dgs.):\n\n"
        "<i>\u201ePad\u0117kite _____.\u201c</i> (Помогите людям.)",
        ["\u017emon\u0117ms"],
        hint="Особое склонение! Dgs.: \u017emon\u0117s \u2192 \u017emon\u0117ms",
        explanation="\u017emogus \u2192 \u017emon\u0117ms. Основа меняется во мн.ч.!",
        ru="Человек \u2192 людям. Основа меняется: \u017emogus \u2192 \u017emon\u0117s.",
    ),
]

# -------------------------------------------------------------------
# LINKSNIAI Drill 3 - Prepositions (12 choice)
# -------------------------------------------------------------------
EXERCISES["linksniai_3"] = [
    _c(
        "Какой падеж требует предлог <b>ant</b> (на)?\n"
        "<i>\u201eKnyga guli ant _____.\u201c</i>",
        ["Kilmininkas (stalo)", "Naudininkas (stalui)", "Galininkas (stal\u0105)", "Vietininkas (stale)"], 0,
        hint="ant + Ko?",
        explanation="ant + Kilmininkas. Ant stalo = на столе.",
        ru="\u201eAnt\u201c всегда требует Kilmininkas (родительный).",
        topic="ant + K.",
    ),
    _c(
        "<b>\u012f</b> (в, куда) + какой падеж?\n<i>\u201eEinu \u012f _____.\u201c</i> (parkas)",
        ["Galininkas (park\u0105)", "Kilmininkas (parko)", "Vietininkas (parke)", "Naudininkas (parkui)"], 0,
        hint="\u012f + K\u0105?",
        explanation="\u012f + Galininkas. \u012e park\u0105 = в парк (направление).",
        ru="\u201e\u012e\u201c \u2014 направление, всегда + Galininkas.",
        topic="\u012f + G.",
    ),
    _c(
        "<b>i\u0161</b> (из) + какой падеж?\n<i>\u201eGr\u012f\u017etu i\u0161 _____.\u201c</i> (darbas)",
        ["Kilmininkas (darbo)", "Galininkas (darb\u0105)", "Vietininkas (darbe)", "\u012enagininkas (darbu)"], 0,
        hint="i\u0161 + Ko?",
        explanation="i\u0161 + Kilmininkas. I\u0161 darbo = с работы.",
        ru="\u201eI\u0161\u201c = из, всегда + Kilmininkas.",
        topic="i\u0161 + K.",
    ),
    _c(
        "<b>su</b> (с) + какой падеж?\n<i>\u201eEinu su _____.\u201c</i> (draugas)",
        ["\u012enagininkas (draugu)", "Kilmininkas (draugo)", "Naudininkas (draugui)", "Galininkas (draug\u0105)"], 0,
        hint="su + Kuo?",
        explanation="su + \u012enagininkas. Su draugu = с другом.",
        ru="\u201eSu\u201c = с, всегда + \u012enagininkas (творительный).",
        topic="su + \u012en.",
    ),
    _c(
        "<b>apie</b> (о, про) + какой падеж?\n<i>\u201eKalbame apie _____.\u201c</i> (darbas)",
        ["Galininkas (darb\u0105)", "Kilmininkas (darbo)", "Naudininkas (darbui)", "Vietininkas (darbe)"], 0,
        hint="apie + K\u0105?",
        explanation="apie + Galininkas. Apie darb\u0105 = о работе.",
        ru="\u201eApie\u201c = о/про + Galininkas. В русском \u201eо\u201c + предложный!",
        topic="apie + G.",
    ),
    _c(
        "<b>prie</b> (у, около) + какой падеж?\n<i>\u201eStoviu prie _____.\u201c</i> (durys)",
        ["Kilmininkas (dur\u0173)", "Galininkas (duris)", "Vietininkas (duryse)", "\u012enagininkas (durimis)"], 0,
        hint="prie + Ko?",
        explanation="prie + Kilmininkas. Prie dur\u0173 = у дверей.",
        ru="\u201ePrie\u201c = у/около + Kilmininkas.",
        topic="prie + K.",
    ),
    _c(
        "<b>d\u0117l</b> (из-за, ради) + какой падеж?\n<i>\u201eD\u0117l _____ negaliu ateiti.\u201c</i> (liga)",
        ["Kilmininkas (ligos)", "Galininkas (lig\u0105)", "Naudininkas (ligai)", "\u012enagininkas (liga)"], 0,
        hint="d\u0117l + Ko?",
        explanation="d\u0117l + Kilmininkas. D\u0117l ligos = из-за болезни.",
        ru="\u201eD\u0117l\u201c = из-за/ради + Kilmininkas.",
        topic="d\u0117l + K.",
    ),
    _c(
        "<b>po</b> (после / под) + какой падеж?\n<i>\u201ePo _____ eisime namo.\u201c</i> (pamoka)",
        ["Kilmininkas (pamokos)", "Galininkas (pamok\u0105)", "Vietininkas (pamokoje)", "\u012enagininkas (pamoka)"], 0,
        hint="po (после) + Ko?",
        explanation="po + Kilmininkas (\u201eпосле\u201c). Po pamokos = после урока.",
        ru="\u201ePo\u201c в значении \u201eпосле\u201c + K. Внимание: \u201eпод\u201c + \u012en.!",
        topic="po + K.",
    ),
    _c(
        "<b>per</b> (через, за) + какой падеж?\n<i>\u201ePer _____ padar\u0117me daug.\u201c</i> (savait\u0117)",
        ["Galininkas (savait\u0119)", "Kilmininkas (savait\u0117s)", "Vietininkas (savait\u0117je)", "\u012enagininkas (savaite)"], 0,
        hint="per + K\u0105?",
        explanation="per + Galininkas. Per savait\u0119 = за неделю.",
        ru="\u201ePer\u201c = через/за + Galininkas.",
        topic="per + G.",
    ),
    _c(
        "<b>be</b> (без) + какой падеж?\n<i>\u201eBe _____ negaliu gyventi.\u201c</i> (muzika)",
        ["Kilmininkas (muzikos)", "Galininkas (muzik\u0105)", "Naudininkas (muzikai)", "Vietininkas (muzikoje)"], 0,
        hint="be + Ko?",
        explanation="be + Kilmininkas. Be muzikos = без музыки.",
        ru="\u201eBe\u201c = без + Kilmininkas.",
        topic="be + K.",
    ),
    _c(
        "<b>pas</b> (у, к) + какой падеж?\n<i>\u201eEinu pas _____.\u201c</i> (gydytojas)",
        ["Galininkas (gydytoj\u0105)", "Kilmininkas (gydytojo)", "Naudininkas (gydytojui)", "\u012enagininkas (gydytoju)"], 0,
        hint="pas + K\u0105?",
        explanation="pas + Galininkas. Pas gydytoj\u0105 = к врачу.",
        ru="\u201ePas\u201c = к/у (человека) + Galininkas. В русском \u201eк\u201c + дательный!",
        topic="pas + G.",
    ),
    _c(
        "<b>tarp</b> (между) + какой падеж?\n<i>\u201eTarp _____ ir mokyklos yra parkas.\u201c</i> (namas)",
        ["Kilmininkas (namo)", "Galininkas (nam\u0105)", "Vietininkas (name)", "Naudininkas (namui)"], 0,
        hint="tarp + Ko?",
        explanation="tarp + Kilmininkas. Tarp namo ir mokyklos = между домом и школой.",
        ru="\u201eTarp\u201c = между + Kilmininkas. В русском \u201eмежду\u201c + тв.п.!",
        topic="tarp + K.",
    ),
]

# -------------------------------------------------------------------
# VEIKSMA\u017dOD\u017dIAI Drill 1 - Conjugation (11 input)
# -------------------------------------------------------------------
EXERCISES["veiksmazodziai_1"] = [
    _i("Проспрягайте <b>skaityti</b> (читать) \u2014 <b>a\u0161</b>, esamasis laikas:",
        ["skaitau"], hint="I asmenuot\u0117: a\u0161 \u2192 -au",
        explanation="skaityti \u2192 a\u0161 skaitau. I спряжение.",
        ru="Я читаю. I спряжение: основа + -au."),
    _i("<b>tur\u0117ti</b> (иметь) \u2014 <b>mes</b>, esamasis laikas:",
        ["turime"], hint="II asmenuot\u0117: mes \u2192 -ime",
        explanation="tur\u0117ti \u2192 mes turime. II спряжение.",
        ru="Мы имеем. II спряжение: основа + -ime."),
    _i("<b>ra\u0161yti</b> (писать) \u2014 <b>jis</b>, b\u016btasis kartinis (прош. вр.):",
        ["ra\u0161\u0117"], hint="I asmenuot\u0117, b\u016bt. kart.: jis \u2192 -\u0117",
        explanation="ra\u0161yti \u2192 jis ra\u0161\u0117. Прошедшее однократное, 3 л.",
        ru="Он писал / написал."),
    _i("<b>dirbti</b> (работать) \u2014 <b>j\u016bs</b>, b\u016bsimasis laikas (буд. вр.):",
        ["dirbsite"], hint="I asmenuot\u0117, b\u016bs.: j\u016bs \u2192 -site",
        explanation="dirbti \u2192 j\u016bs dirbsite. Будущее.",
        ru="Вы будете работать."),
    _i("<b>mokytis</b> (учиться) \u2014 <b>a\u0161</b>, esamasis laikas:",
        ["mokausi"], hint="Возвратный! Основа + окончание + si",
        explanation="mokytis \u2192 a\u0161 mokausi. Mok-au-si.",
        ru="Я учусь. Возвратный: mok-au-si."),
    _i("<b>gal\u0117ti</b> (мочь) \u2014 <b>tu</b>, esamasis laikas:",
        ["gali"], hint="II asmenuot\u0117: tu \u2192 -i",
        explanation="gal\u0117ti \u2192 tu gali. II спряжение.",
        ru="Ты можешь."),
    _i("<b>eiti</b> (идти) \u2014 <b>a\u0161</b>, esamasis laikas:",
        ["einu"], hint="Неправильный глагол: ein-u",
        explanation="eiti \u2192 a\u0161 einu. Неправильное спряжение.",
        ru="Я иду. Неправильный глагол."),
    _i("<b>nor\u0117ti</b> (хотеть) \u2014 <b>ji</b>, b\u016btasis kartinis laikas:",
        ["nor\u0117jo"], hint="II asmenuot\u0117, b\u016bt. kart.: jis/ji \u2192 -\u0117jo",
        explanation="nor\u0117ti \u2192 ji nor\u0117jo. II спряжение, прош. вр., 3 л.",
        ru="Она хотела."),
    _i("<b>valgyti</b> (есть/кушать) \u2014 <b>jie</b>, b\u016bsimasis laikas:",
        ["valgys"], hint="I asmenuot\u0117, b\u016bs.: jie \u2192 -s",
        explanation="valgyti \u2192 jie valgys. Будущее, 3 л.",
        ru="Они будут есть."),
    _i("<b>\u017einoti</b> (знать) \u2014 <b>mes</b>, esamasis laikas:",
        ["\u017einome"], hint="I asmenuot\u0117: mes \u2192 -ome",
        explanation="\u017einoti \u2192 mes \u017einome.",
        ru="Мы знаем."),
    _i("<b>nusipirkti</b> (купить себе, возвр.) \u2014 <b>a\u0161</b>, b\u016btasis kartinis:",
        ["nusipirkau"], hint="Приставка + si + корень + окончание",
        explanation="nu-si-pirk-au. Возвратный с приставкой.",
        ru="Я купил(а) себе. nu + si + pirk + au."),
]

# -------------------------------------------------------------------
# VEIKSMA\u017dOD\u017dIAI Drill 2 - Tenses (8 choice)
# -------------------------------------------------------------------
EXERCISES["veiksmazodziai_2"] = [
    _c("<i>\u201eVakar a\u0161 _____ \u012f kin\u0105.\u201c</i> (Вчера я ходил в кино.)",
        ["\u0117jau", "einu", "eisiu", "eidavau"], 0,
        hint="Vakar = вчера \u2192 прошедшее",
        explanation="Vakar \u2192 b\u016btasis kartinis. A\u0161 \u0117jau.",
        ru="Вчера = прошедшее однократное.", topic="B\u016bt. kartinis"),
    _c("<i>\u201eKit\u0105 savait\u0119 mes _____ atostogas.\u201c</i> (На следующей неделе мы будем в отпуске.)",
        ["tur\u0117sime", "turime", "tur\u0117jome", "tur\u0117davome"], 0,
        hint="Kit\u0105 savait\u0119 = на следующей неделе \u2192 будущее",
        explanation="Kit\u0105 savait\u0119 \u2192 b\u016bsimasis. Mes tur\u0117sime.",
        ru="Будущее время.", topic="B\u016bsimasis"),
    _c("<i>\u201eKai buvau ma\u017eas, kiekvien\u0105 vasar\u0105 _____ pas senelius.\u201c</i>",
        ["va\u017eiuodavau", "va\u017eiavau", "va\u017eiuoju", "va\u017eiuosiu"], 0,
        hint="Kiekvien\u0105 vasar\u0105 = каждое лето \u2192 многократное прошедшее",
        explanation="Регулярно \u2192 b\u016btasis da\u017eninis. A\u0161 va\u017eiuodavau.",
        ru="Каждое лето (регулярно) \u2192 b\u016bt. da\u017eninis. Нет аналога в русском.", topic="B\u016bt. da\u017eninis"),
    _c("<i>\u201e\u0160iuo metu ji _____ universitete.\u201c</i> (Сейчас она учится в университете.)",
        ["mokosi", "mok\u0117si", "mokysis", "mokydavosi"], 0,
        hint="\u0160iuo metu = сейчас \u2192 настоящее",
        explanation="\u0160iuo metu \u2192 esamasis laikas. Ji mokosi.",
        ru="Сейчас \u2192 настоящее время.", topic="Esamasis"),
    _c("<i>\u201eJis man pasak\u0117, kad rytoj _____ anks\u010diau.\u201c</i>",
        ["ateis", "ateina", "at\u0117jo", "ateidavo"], 0,
        hint="Rytoj = завтра \u2192 будущее",
        explanation="Rytoj \u2192 b\u016bsimasis. Jis ateis.",
        ru="Завтра \u2192 будущее.", topic="B\u016bsimasis"),
    _c("<i>\u201eSeniau \u017emon\u0117s _____ lai\u0161kus ranka.\u201c</i>",
        ["ra\u0161ydavo", "ra\u0161\u0117", "ra\u0161o", "ra\u0161ys"], 0,
        hint="Seniau = раньше (обычно) \u2192 многократное прошедшее",
        explanation="Seniau (бывало) \u2192 b\u016btasis da\u017eninis.",
        ru="Раньше (бывало) \u2192 b\u016bt. da\u017eninis.", topic="B\u016bt. da\u017eninis"),
    _c("<i>\u201eAr tu jau _____ t\u0105 film\u0105?\u201c</i> (Ты уже смотрел(а) тот фильм?)",
        ["\u017eiur\u0117jai", "\u017eiuri", "\u017eiur\u0117si", "\u017eiur\u0117davai"], 0,
        hint="Jau = уже \u2192 совершённое действие",
        explanation="Jau \u2192 b\u016btasis kartinis. Tu \u017eiur\u0117jai.",
        ru="Уже \u2192 свершившийся факт \u2192 прошедшее.", topic="B\u016bt. kartinis"),
    _c("<i>\u201eKol j\u016bs _____, a\u0161 paruo\u0161iu vakarien\u0119.\u201c</i>",
        ["ils\u0117sit\u0117s", "ilsit\u0117s", "ils\u0117jot\u0117s", "ils\u0117davot\u0117s"], 0,
        hint="Kol = пока (в будущем) \u2192 будущее",
        explanation="Kol + b\u016bsimasis. J\u016bs ils\u0117sit\u0117s.",
        ru="Пока будете \u2192 будущее время.", topic="B\u016bsimasis"),
]

# -------------------------------------------------------------------
# VEIKSMA\u017dOD\u017dIAI Drill 3 - Prefixes (8 choice)
# -------------------------------------------------------------------
EXERCISES["veiksmazodziai_3"] = [
    _c("Выберите глагол с правильной приставкой:\n"
        "<i>\u201eJis _____ i\u0161 nam\u0173 ir nu\u0117jo \u012f darb\u0105.\u201c</i> (Он вышел из дома...)",
        ["i\u0161\u0117jo", "nu\u0117jo", "at\u0117jo", "par\u0117jo"], 0,
        hint="I\u0161 nam\u0173 = из дома \u2192 движение наружу",
        explanation="i\u0161-eiti = выйти (наружу).",
        ru="Вышел. Приставка \u201ei\u0161-\u201c = из, наружу.", topic="i\u0161-"),
    _c("<i>\u201eVaikai, _____ namo! Vakarien\u0117 paruo\u0161ta.\u201c</i>",
        ["pareikite", "ateikite", "i\u0161eikite", "nueikite"], 0,
        hint="Namo = домой (возвращение) \u2192 par-",
        explanation="par-eiti = вернуться домой.",
        ru="Возвращайтесь. \u201ePar-\u201c = обратно, назад (домой).", topic="par-"),
    _c("<i>\u201eAr galiu _____ prie j\u016bs\u0173?\u201c</i> (Можно присесть к вам?)",
        ["pris\u0117sti", "atsis\u0117sti", "nus\u0117sti", "pasis\u0117sti"], 0,
        hint="Prie j\u016bs\u0173 = к вам \u2192 приближение",
        explanation="pri-s\u0117sti = присесть (к кому-то).",
        ru="Присесть. \u201ePri-\u201c = при, к \u2014 приближение.", topic="pri-"),
    _c("<i>\u201eJi _____ vis\u0105 knyg\u0105 per vien\u0105 vakar\u0105.\u201c</i>",
        ["perskait\u0117", "skait\u0117", "nuskait\u0117", "atskait\u0117"], 0,
        hint="Vis\u0105 knyg\u0105 = всю книгу (от начала до конца) \u2192 per-",
        explanation="per-skaityti = прочитать целиком.",
        ru="Прочитала (целиком). \u201ePer-\u201c = через, полностью.", topic="per-"),
    _c("<i>\u201eReikia _____ \u0161it\u0105 klaid\u0105.\u201c</i> (Нужно исправить эту ошибку.)",
        ["i\u0161taisyti", "pataisyti", "nutaisyti", "sutaisyti"], 0,
        hint="Исправить полностью \u2192 i\u0161-",
        explanation="i\u0161-taisyti = исправить (полностью).",
        ru="Исправить. \u201eI\u0161-\u201c = завершённость действия.", topic="i\u0161-/pa-"),
    _c("<i>\u201eMes _____ nauj\u0105 but\u0105 pernai.\u201c</i> (Мы купили квартиру в прошлом году.)",
        ["nusipirkome", "pirkome", "nupirkome", "supirkome"], 0,
        hint="Купили ДЛЯ СЕБЯ \u2192 возвратный с приставкой nu-",
        explanation="nu-si-pirkti = купить себе.",
        ru="Купили себе. \u201eNusi-\u201c = nu + si (себе).", topic="nusi-"),
    _c("<i>\u201eJie nori _____ nauj\u0105 versl\u0105.\u201c</i> (Они хотят открыть бизнес.)",
        ["prad\u0117ti", "atidaryti", "i\u0161daryti", "sudaryti"], 0,
        hint="Открыть (начать) бизнес = prad\u0117ti",
        explanation="prad\u0117ti versl\u0105 = начать/открыть бизнес.",
        ru="Начать/открыть. Atidaryti = открыть (дверь физически).", topic="Лексика"),
    _c("<i>\u201ePra\u0161au _____ duris.\u201c</i> (Пожалуйста, закройте дверь.)",
        ["u\u017edarykite", "sudarykite", "pridarykite", "atidarykite"], 0,
        hint="Закрыть \u2192 u\u017e-daryti",
        explanation="u\u017e-daryti = закрыть.",
        ru="Закройте. \u201eU\u017e-\u201c = за (закрывание). Atidaryti \u2194 u\u017edaryti.", topic="u\u017e-"),
]

# -------------------------------------------------------------------
# KALBOS VARTOJIMAS Drill 1 - Word forms choice (8 choice)
# -------------------------------------------------------------------
EXERCISES["kalbos_vartojimas_1"] = [
    _c("<i>\u201e\u0160iemet vykstantis festivalis taps svarbiu _____ ne tik miestui.\u201c</i>",
        ["\u012fvykiu", "\u012fvykis", "\u012fvyk\u012f", "\u012fvykio"], 0,
        hint="taps + KUO? \u2192 \u012enagininkas",
        explanation="taps + \u012enagininkas. Taps svarbiu \u012fvykiu = станет важным событием.",
        ru="Станет ЧЕМ? \u2192 Творительный.", topic="\u012enagininkas"),
    _c("<i>\u201eFestivalis pritrauks kino _____ i\u0161 viso pasaulio.\u201c</i>",
        ["myl\u0117toj\u0173", "myl\u0117tojai", "myl\u0117tojus", "myl\u0117tojams"], 0,
        hint="pritrauks K\u0104? \u2192 G., но Kilmininkas dalies",
        explanation="pritrauks kino myl\u0117toj\u0173 \u2014 Kilmininkas (количественный).",
        ru="Привлечёт (некоторое кол-во) любителей. Родительный количественный.", topic="Kilmininkas"),
    _c("<i>\u201eGal\u0117site pamatyti tiek Lietuvoje _____ film\u0173.\u201c</i>",
        ["sukurt\u0173", "sukurti", "sukurtas", "sukurtus"], 0,
        hint="film\u0173 (K., dgs.) \u2192 причастие тоже в K., dgs.",
        explanation="sukurt\u0173 \u2014 neveik. b\u016bt. laiko dalyvis, K., dgs.",
        ru="Созданных фильмов. Причастие согласуется с \u201efilm\u0173\u201c.", topic="Dalyviai + K."),
    _c("<i>\u201eFestivalio tikslas \u2014 skatinti kino meno _____.\u201c</i>",
        ["pl\u0117tr\u0105", "pl\u0117tra", "pl\u0117tros", "pl\u0117trai"], 0,
        hint="skatinti + K\u0104? \u2192 Galininkas",
        explanation="skatinti pl\u0117tr\u0105 \u2014 skatinti + Galininkas.",
        ru="Содействовать ЧЕМУ? В лит. skatinti + Galininkas!", topic="Galininkas"),
    _c("<i>\u201eProgramoje daug d\u0117mesio _____ aktualioms socialin\u0117ms temoms.\u201c</i>",
        ["skiriama", "skiriamas", "skirti", "skiriant"], 0,
        hint="d\u0117mesio skiriama = внимание уделяется",
        explanation="skiriama \u2014 безличная форма причастия.",
        ru="Уделяется. Безличная конструкция.", topic="Neveik. dalyvis"),
    _c("<i>\u201e\u017di\u016brovai gali _____ dokumentini\u0173 film\u0173 sekcij\u0105.\u201c</i>",
        ["aplankyti", "aplanko", "aplankyt\u0173", "aplankydami"], 0,
        hint="gali + инфинитив",
        explanation="gali aplankyti \u2014 gali + bendratis (инфинитив).",
        ru="Могут посетить. После \u201egali\u201c \u2014 инфинитив.", topic="Bendratis"),
    _c("<i>\u201eKauno kino festivalis kasmet auga ir tampa _____ kult\u016brine platforma.\u201c</i>",
        ["svarbia", "svarbi", "svarbi\u0105", "svarbios"], 0,
        hint="tampa + Kuo? \u2192 \u012enagininkas",
        explanation="tampa svarbia \u2014 tampa + \u012enagininkas.",
        ru="Становится ЧЕМ? \u2192 Творительный.", topic="\u012enagininkas"),
    _c("<i>\u201eJis praturtina miesto gyvenim\u0105 bei _____ naujas galimybes.\u201c</i>",
        ["atveria", "atverti", "atverdamas", "atvert\u0173"], 0,
        hint="Однородные сказуемые: praturtina ir _____",
        explanation="atveria \u2014 esamojo laiko, 3 asmuo. Параллельно с \u201epraturtina\u201c.",
        ru="Открывает. Однородные сказуемые \u2014 оба в наст. вр.", topic="Veiksma\u017eodis"),
]

# -------------------------------------------------------------------
# KALBOS VARTOJIMAS Drill 2 - Participles & adjectives (8 choice)
# -------------------------------------------------------------------
EXERCISES["kalbos_vartojimas_2"] = [
    _c("<i>\u201e\u017dinau, kad m\u016bs\u0173 mieste vis da\u017eniau apsilanko _____ \u017emoni\u0173.\u201c</i>",
        ["atvykstan\u010di\u0173", "atvykstantys", "atvykstan\u010dius", "atvykstan\u010diomis"], 0,
        hint="\u017emoni\u0173 (K., dgs.) \u2192 причастие согласуется",
        explanation="atvykstan\u010di\u0173 \u2014 veik. esam. laiko dalyvis, K., dgs.",
        ru="Прибывающих. Согласуется с \u201e\u017emoni\u0173\u201c в род.п., мн.ч.", topic="Dalyviai + K."),
    _c("<i>\u201eKiekvienas gali rasti sau _____ viet\u0105.\u201c</i>",
        ["tinkam\u0105", "tinkamas", "tinkanti", "tinkan\u010di\u0105"], 0,
        hint="rasti K\u0104? viet\u0105 (G., mot.) \u2192 tinkam\u0105",
        explanation="tinkam\u0105 \u2014 Galininkas, mot. gimin\u0117.",
        ru="Подходящее (место). Вин.п., ж.р.", topic="Dalyviai vs b\u016bdv."),
    _c("<i>\u201eDaugum\u0105 vie\u0161bu\u010di\u0173 kambari\u0173 _____ rezervuoti internetu.\u201c</i>",
        ["galima", "galimas", "galimi", "gali"], 0,
        hint="galima + bendratis = можно + инфинитив",
        explanation="galima rezervuoti \u2014 безличная конструкция.",
        ru="Можно забронировать. \u201eGalima\u201c \u2014 безличная форма.", topic="Безличная конструкция"),
    _c("<i>\u201e_____ ilgesniam laikui, verta pagalvoti apie apartamentus.\u201c</i>",
        ["Apsistojant", "Apsistodamas", "Apsistoti", "Apsistojantis"], 0,
        hint="Безличный деепричастный оборот \u2192 padalyvis",
        explanation="Apsistojant \u2014 padalyvis (безличная форма).",
        ru="При проживании. Безличная форма деепричастия.", topic="Padalyvis"),
    _c("<i>\u201eMane su\u017eav\u0117jo slaugytoj\u0173 _____ ir d\u0117mesingumas.\u201c</i>",
        ["r\u016bpestingumas", "r\u016bpestingum\u0105", "r\u016bpestingumo", "r\u016bpestingu"], 0,
        hint="Kas su\u017eav\u0117jo? \u2192 подлежащее \u2192 Vardininkas",
        explanation="r\u016bpestingumas \u2014 Vardininkas, подлежащее.",
        ru="ЧТО поразило? Заботливость. Подлежащее \u2192 им.п.", topic="Vardininkas"),
    _c("<i>\u201eNor\u0117\u010diau _____ nuošird\u017ei\u0105 pad\u0117k\u0105.\u201c</i>",
        ["i\u0161reik\u0161ti", "i\u0161rei\u0161kiu", "i\u0161reik\u0161damas", "i\u0161reik\u0161tas"], 0,
        hint="nor\u0117\u010diau + инфинитив",
        explanation="nor\u0117\u010diau i\u0161reik\u0161ti \u2014 nor\u0117\u010diau + bendratis.",
        ru="Хотел бы ВЫРАЗИТЬ. После \u201enor\u0117\u010diau\u201c \u2014 инфинитив.", topic="Bendratis"),
    _c("<i>\u201e\u010cia d\u017eiaug\u0117si auk\u0161\u010diausios kokyb\u0117s _____ paslaugomis.\u201c</i>",
        ["medicinin\u0117mis", "medicinines", "medicinini\u0173", "medicinin\u0117s"], 0,
        hint="d\u017eiaugtis KUO? \u2192 \u012enagininkas",
        explanation="medicinin\u0117mis \u2014 \u012enagininkas, dgs. D\u017eiaugtis + \u012en.",
        ru="Радоваться ЧЕМУ? В лит.: d\u017eiaugtis + \u012en. (тв.п.).", topic="\u012enagininkas"),
    _c("<i>\u201eJ\u0173 kasdienit\u0117s \u0161ypsenos ir padra\u0105sinimai k\u0117l\u0117 ger\u0105 _____.\u201c</i>",
        ["nuotaik\u0105", "nuotaika", "nuotaikos", "nuotaikai"], 0,
        hint="k\u0117l\u0117 K\u0104? \u2192 Galininkas",
        explanation="k\u0117l\u0117 ger\u0105 nuotaik\u0105 \u2014 Galininkas.",
        ru="Поднимали ЧТО? Настроение \u2192 вин.п.", topic="Galininkas"),
]

# -------------------------------------------------------------------
# KALBOS VARTOJIMAS Drill 3 - Free input (8 input)
# -------------------------------------------------------------------
EXERCISES["kalbos_vartojimas_3"] = [
    _i("<i>\u201e_____ nuošird\u017ei\u0105 pad\u0117k\u0105 u\u017e puik\u0173 gydym\u0105 ir prie\u017ei\u016br\u0105, "
        "kuri\u0105 gavau j\u016bs\u0173 ligonin\u0117je.\u201c</i>\n\n"
        "Хотел бы выразить искреннюю благодарность...",
        ["Nor\u0117\u010diau i\u0161reik\u0161ti", "Nor\u0117\u010diau pareik\u0161ti"],
        hint="Формальное начало письма: Nor\u0117\u010diau + инфинитив",
        explanation="Nor\u0117\u010diau i\u0161reik\u0161ti \u2014 стандартное начало официального письма.",
        ru="Хотел бы выразить. Стандартная формула."),
    _i("<i>\u201e\u010cia d\u017eiaug\u0117si auk\u0161\u010diausios kokyb\u0117s medicinin\u0117mis paslaugomis, "
        "bet ir patyriau \u017emogi\u0161k\u0105 \u0161ilum\u0105 _____ d\u0117mes\u012f.\u201c</i>\n\n"
        "...но и испытал тепло и (= а также) внимание.",
        ["bei", "ir"],
        hint="Союз \u201eа также / и\u201c = bei / ir",
        explanation="bei d\u0117mes\u012f \u2014 \u201ebei\u201c = и, а также.",
        ru="\u201eBei\u201c или \u201eir\u201c = и, а также. Оба правильны."),
    _i("<i>\u201eJau nuo pat _____ dienos ligonin\u0117je skyriaus gydytojai buvo "
        "pasireng\u0119 atsakyti \u012f visus klausimus.\u201c</i>\n\n"
        "С самого _____ дня в больнице... (первого)",
        ["pirmos", "pirmosios"],
        hint="nuo pat + какой? \u2192 первой (Kilmininkas, mot.g.)",
        explanation="nuo pat pirmos dienos \u2014 с самого первого дня.",
        ru="С первого дня. Pirmos/pirmosios \u2014 род.п., ж.р."),
    _i("<i>\u201eMano gydymo procesas buvo _____.\u201c</i>\n\n"
        "Процесс лечения был _____ (гладким/без проблем).",
        ["sklandus"],
        hint="Buvo + какой? \u2192 прилаг. в Vardininkas, vyr.g.",
        explanation="sklandus \u2014 гладкий, без осложнений.",
        ru="Гладкий / без проблем."),
    _i("<i>\u201eGal\u0117dama vie\u0161ai pasidalinti savo gera _____, esu d\u0117kinga.\u201c</i>\n\n"
        "Имея возможность поделиться хорошим _____ (опытом)...",
        ["patirtimi"],
        hint="pasidalinti + Kuo? \u2192 \u012enagininkas",
        explanation="patirtimi \u2014 \u012enagininkas (творительный).",
        ru="Поделиться ЧЕМ? Опытом. Patirtis \u2192 patirtimi."),
    _i("<i>\u201eVis\u0173 J\u016bs\u0173 profesionalumas yra tikras _____ sveikatos prie\u017ei\u016bros \u012fstaigoms.\u201c</i>\n\n"
        "Ваш профессионализм \u2014 настоящий _____ (пример).",
        ["pavyzdys"],
        hint="Vardininkas, vyr. gimin\u0117",
        explanation="pavyzdys \u2014 пример. Vardininkas.",
        ru="Пример. Именительный падеж."),
    _i("<i>\u201e_____ kart\u0105 d\u0117koju u\u017e j\u016bs\u0173 pastangas.\u201c</i>\n\n"
        "Ещё _____ благодарю за ваши старания.",
        ["Dar vien\u0105"],
        hint="Ещё раз = dar vien\u0105 kart\u0105",
        explanation="Dar vien\u0105 kart\u0105 \u2014 ещё раз.",
        ru="Ещё раз. Kart\u0105 \u2014 вин.п. от \u201ekartas\u201c."),
    _i("<i>\u201eLinkiu visiems _____ \u0161iame svarbiame darbe.\u201c</i>\n\n"
        "Желаю всем _____ (успехов) в этой важной работе.",
        ["s\u0117km\u0117s"],
        hint="link\u0117ti + Ko? \u2192 Kilmininkas",
        explanation="s\u0117km\u0117s \u2014 Kilmininkas. Link\u0117ti + K.",
        ru="Желать ЧЕГО? Успехов. Link\u0117ti + род.п."),
]

# -------------------------------------------------------------------
# JUNGTUKAI Drill 1 - Choose conjunction (10 choice)
# -------------------------------------------------------------------
EXERCISES["jungtukai_1"] = [
    _c("<i>\u201eJis neat\u0117jo \u012f darb\u0105, _____ sirgo.\u201c</i>\nОн не пришёл на работу, _____ болел.",
        ["nes", "kad", "bet", "ir"], 0,
        hint="Причина: потому что = nes",
        explanation="nes = потому что (причина).",
        ru="Потому что. \u201eNes\u201c \u2014 самый распространённый союз причины.", topic="Причина"),
    _c("<i>\u201e_____ baigsi studijas, gal\u0117si dirbti.\u201c</i>",
        ["Kai", "Kad", "Nes", "Bet"], 0,
        hint="Когда = kai",
        explanation="Kai = когда (временной союз).",
        ru="Когда. \u201eKai\u201c = когда.", topic="Время"),
    _c("<i>\u201e\u017dinome, _____ tai n\u0117ra lengva.\u201c</i>",
        ["kad", "nes", "kai", "kol"], 0,
        hint="Знаем, ЧТО... = kad",
        explanation="kad = что (изъяснительный союз).",
        ru="Что. \u201eKad\u201c = что (после глаголов знания, речи).", topic="Изъяснительный"),
    _c("<i>\u201e_____ lyja, mes vis tiek eisime pasivaikš\u010dioti.\u201c</i>",
        ["Nors", "Nes", "Kad", "Kai"], 0,
        hint="Хотя = nors",
        explanation="Nors = хотя (уступительный союз).",
        ru="Хотя. \u201eNors\u201c = хотя. Выражает уступку.", topic="Уступка"),
    _c("<i>\u201ePalauk, _____ a\u0161 gr\u012f\u0161iu.\u201c</i>",
        ["kol", "kai", "kad", "nes"], 0,
        hint="Пока = kol",
        explanation="kol = пока.",
        ru="Пока. \u201eKol\u201c = пока.", topic="Время (пока)"),
    _c("<i>\u201eFestivalis svarbus _____ miestui, _____ visai \u0161aliai.\u201c</i>",
        ["ne tik... bet ir", "ir... ir", "tiek... tiek", "nei... nei"], 0,
        hint="Не только... но и",
        explanation="ne tik... bet ir = не только... но и.",
        ru="Не только... но и. Парный союз для усиления.", topic="Не только... но и"),
    _c("<i>\u201e_____ tur\u0117tum pinig\u0173, k\u0105 pirktum?\u201c</i>",
        ["Jeigu", "Kai", "Kad", "Kol"], 0,
        hint="Если (бы) = jeigu / jei",
        explanation="Jeigu = если (условный союз).",
        ru="Если. \u201eJeigu/jei\u201c = если.", topic="Условие"),
    _c("<i>\u201eSirgau, _____ negal\u0117jau ateiti.\u201c</i>",
        ["tod\u0117l", "nes", "kad", "bet"], 0,
        hint="Поэтому = tod\u0117l",
        explanation="tod\u0117l = поэтому (следствие).",
        ru="Поэтому. \u201eTod\u0117l\u201c \u2014 союз следствия.", topic="Следствие"),
    _c("<i>\u201eJis mokosi, _____ dirba vakarais.\u201c</i>",
        ["o", "ir", "bet", "nes"], 0,
        hint="А (противопоставление) = o",
        explanation="o = а (мягкое противопоставление).",
        ru="\u201eА\u201c (противопоставление). \u201eO\u201c \u2014 мягче, чем \u201ebet\u201c.", topic="Противопоставление"),
    _c("<i>\u201eNor\u0117\u010diau, _____ j\u016bs atsi\u0173stum\u0117te man informacij\u0105.\u201c</i>",
        ["kad", "kai", "nes", "tod\u0117l"], 0,
        hint="Хотел бы, ЧТОБЫ = kad + tariamoji nuosaka",
        explanation="kad + сослагательное = чтобы.",
        ru="Чтобы. \u201eKad\u201c + сослагательное наклонение = чтобы.", topic="Изъясн. + сослагательное"),
]

# -------------------------------------------------------------------
# JUNGTUKAI Drill 2 - Joining sentences (8 input)
# -------------------------------------------------------------------
EXERCISES["jungtukai_2"] = [
    _i("Вставьте союз:\n<i>\u201eA\u0161 mokau lietuvi\u0173 kalb\u0105, _____ noriu i\u0161laikyti B2 egzamin\u0105.\u201c</i>",
        ["nes", "kadangi"],
        hint="Причина \u2192 nes / kadangi",
        explanation="nes / kadangi = потому что / поскольку.",
        ru="Потому что / поскольку."),
    _i("<i>\u201eVa\u017eiuosime \u012f paj\u016br\u012f, _____ oras bus geras.\u201c</i>",
        ["jei", "jeigu"],
        hint="Условие \u2192 jei / jeigu",
        explanation="jei / jeigu = если (условие).",
        ru="Если."),
    _i("<i>\u201eJis kalb\u0117jo taip tyliai, _____ niekas negird\u0117jo.\u201c</i>",
        ["kad"],
        hint="Следствие: так тихо, ЧТО... = kad",
        explanation="kad = что (следствие). Taip... kad = так... что.",
        ru="Что (следствие). \u201eTaip... kad\u201c = так... что."),
    _i("<i>\u201e_____ mokiausi universitete, dirbau vakarais.\u201c</i>",
        ["Kai", "Kol"],
        hint="Когда / пока \u2192 kai / kol",
        explanation="Kai = когда. Kol = пока. Оба подходят.",
        ru="Когда / пока."),
    _i("<i>\u201eJis neturi _____ pinig\u0173, _____ laiko.\u201c</i>\nУ него нет ни денег, ни времени.",
        ["nei... nei"],
        hint="Ни... ни = nei... nei",
        explanation="nei... nei = ни... ни.",
        ru="Ни... ни. Отрицательный парный союз."),
    _i("<i>\u201eReikia pasiruo\u0161ti, _____ egzaminas jau greitai.\u201c</i>",
        ["nes", "kadangi", "juk"],
        hint="Причина \u2192 nes / kadangi / juk (ведь)",
        explanation="nes / kadangi / juk = потому что / ведь.",
        ru="Потому что / ведь."),
    _i("<i>\u201e_____ ir kaip steng\u010diausi, nepavyko.\u201c</i>\nКак ни старался, не получилось.",
        ["Kad"],
        hint="Как ни... = Kad ir kaip",
        explanation="Kad ir kaip = как ни (уступительный оборот).",
        ru="Как ни... Устойчивое уступительное выражение."),
    _i("<i>\u201eJis ne _____ protingas, _____ ir darb\u0161tus.\u201c</i>",
        ["tik... bet ir"],
        hint="Не только... но и = ne tik... bet ir",
        explanation="ne tik... bet ir = не только... но и.",
        ru="Не только... но и."),
]

# -------------------------------------------------------------------
# \u017dOD\u017dI\u0172 DARYBA Drill 1 - Prefixes (8 choice)
# -------------------------------------------------------------------
EXERCISES["zodziu_daryba_1"] = [
    _c("<i>\u201e\u0160is sprendimas yra visi\u0161kai _____.\u201c</i>\nЭто решение совершенно _____ (неприемлемо).",
        ["nepriimtinas", "priimtinas", "priimtas", "nepriimtas"], 0,
        hint="Отрицание + приемлемый = ne-priimtinas",
        explanation="nepriimtinas = неприемлемый.",
        ru="Неприемлемый. Приставка \u201ene-\u201c для отрицания.", topic="ne- + priimtinas"),
    _c("<i>\u201e\u0160i informacija yra labai _____.\u201c</i>\nЭта информация очень _____ (важная).",
        ["svarbi", "svarbumas", "svarbiai", "svarbinti"], 0,
        hint="Yra KOKIA? \u2192 прилагательное",
        explanation="svarbi \u2014 b\u016bdvardis, mot. gimin\u0117.",
        ru="Важная. Нужно прилагательное (какая?).", topic="Часть речи"),
    _c("<i>\u201eJo _____ pad\u0117jo i\u0161spr\u0119sti problem\u0105.\u201c</i>\nЕго _____ (опыт) помог решить проблему.",
        ["patirtis", "patyr\u0119s", "patirtas", "patirdamas"], 0,
        hint="Jo KAS? \u2192 существительное",
        explanation="patirtis = опыт (существительное).",
        ru="Опыт. Нужно существительное (подлежащее).", topic="Существительное"),
    _c("<i>\u201eLabai _____ d\u0117koju u\u017e pagalb\u0105.\u201c</i>\nОчень _____ (искренне) благодарю.",
        ["nuošird\u017eiai", "nuoširdus", "nuoširdumas", "nuošird\u017ei\u0105"], 0,
        hint="КАК благодарю? \u2192 наречие \u2192 -ai",
        explanation="nuošird\u017eiai \u2014 prieveiksmis (наречие). КАК?",
        ru="Искренне. Наречие. Окончание -ai.", topic="Наречие"),
    _c("<i>\u201e_____ sistema leid\u017eia taupyti laik\u0105.\u201c</i>\n_____ (электронная) система.",
        ["Elektronin\u0117", "Elektron\u0117", "Elektronika", "Elektroni\u0161ka"], 0,
        hint="КАКАЯ система? \u2192 относительное прилагательное \u2192 -in\u0117",
        explanation="elektronin\u0117 \u2014 относительное прилагательное (-in\u0117).",
        ru="Электронная. Суффикс -inis/-in\u0117.", topic="-in\u0117"),
    _c("<i>\u201eJ\u016bs\u0173 _____ pad\u0117s kitiems pacientams.\u201c</i>\nВаша _____ (благодарность) поможет другим.",
        ["pad\u0117ka", "pad\u0117koti", "d\u0117kingas", "pad\u0117kojimas"], 0,
        hint="J\u016bs\u0173 KAS? \u2192 существительное",
        explanation="pad\u0117ka = благодарность (существительное).",
        ru="Благодарность. Существительное от pad\u0117koti.", topic="Существительное"),
    _c("<i>\u201eTai labai _____ paslauga.\u201c</i>\nЭто очень _____ (полезная) услуга.",
        ["naudinga", "naudingumas", "naudoti", "naudingai"], 0,
        hint="KOKIA paslauga? \u2192 прилагательное",
        explanation="naudinga \u2014 b\u016bdvardis (-inga). Полезная.",
        ru="Полезная. Суффикс -ingas/-inga.", topic="-inga"),
    _c("<i>\u201eBuvo priimtas svarbus _____ d\u0117l miesto pl\u0117tros.\u201c</i>\nБыло принято важное _____ (решение).",
        ["sprendimas", "spr\u0119sti", "sprend\u017eiamas", "i\u0161spr\u0119stas"], 0,
        hint="KAS buvo priimtas? \u2192 существительное",
        explanation="sprendimas = решение. Существительное от spr\u0119sti.",
        ru="Решение. Суффикс -imas.", topic="-imas"),
]

# -------------------------------------------------------------------
# \u017dOD\u017dI\u0172 DARYBA Drill 2 - Suffixes (8 input)
# -------------------------------------------------------------------
EXERCISES["zodziu_daryba_2"] = [
    _i("Образуйте существительное от прилаг. <b>gra\u017eus</b> (красивый):\n"
        "<i>\u201eGamtos _____ yra ne\u012fkainojamas.\u201c</i> (Красота природы бесценна.)",
        ["gro\u017eis"],
        hint="Красота = gro\u017eis (не gro\u017eumas!)",
        explanation="gro\u017eis = красота. Исключение!",
        ru="Красота = gro\u017eis. Исключение! Обычно -umas."),
    _i("Образуйте наречие от <b>greitas</b> (быстрый):\n"
        "<i>\u201eJis b\u0117ga labai _____.\u201c</i>",
        ["greitai"],
        hint="Наречие: -as \u2192 -ai",
        explanation="greitas \u2192 greitai. Окончание -ai.",
        ru="Быстро. -as \u2192 -ai."),
    _i("Образуйте существительное (деятель) от <b>skaityti</b> (читать):\n"
        "<i>\u201eJis yra aktyvus knyg\u0173 _____.\u201c</i>",
        ["skaitytojas"],
        hint="Деятель от глагола: -tojas",
        explanation="skaityti \u2192 skaitytojas (читатель).",
        ru="Читатель. Суффикс -tojas."),
    _i("Образуйте прилагательное от <b>sportas</b> (спорт):\n"
        "<i>\u201eTai _____ renginys.\u201c</i> (спортивное мероприятие)",
        ["sportinis"],
        hint="Относительное прилагательное: -inis",
        explanation="sportas \u2192 sportinis (спортивный).",
        ru="Спортивный. Суффикс -inis."),
    _i("Образуйте существительное (процесс) от <b>mokyti</b> (обучать):\n"
        "<i>\u201e_____ trunka trejus metus.\u201c</i> (Обучение длится три года.)",
        ["Mokymas"],
        hint="Процесс от глагола: -ymas/-imas",
        explanation="mokyti \u2192 mokymas (обучение).",
        ru="Обучение. Суффикс -ymas."),
    _i("Образуйте прилагательное с приставкой <b>ne-</b> от <b>tik\u0117tinas</b> (ожидаемый):\n"
        "<i>\u201eTai buvo _____ rezultatas.\u201c</i> (неожиданный результат)",
        ["netik\u0117tas", "netik\u0117tinas"],
        hint="не + ожидаемый \u2192 ne-tik\u0117tas",
        explanation="netik\u0117tas = неожиданный.",
        ru="Неожиданный. Приставка ne-."),
    _i("Образуйте существительное от <b>d\u0117mesingas</b> (внимательный):\n"
        "<i>\u201eA\u010di\u016b u\u017e j\u016bs\u0173 _____.\u201c</i> (Спасибо за внимательность.)",
        ["d\u0117mesingum\u0105", "d\u0117mesingumas"],
        hint="Абстрактное качество: -umas. U\u017e + K\u0104 \u2192 Galininkas",
        explanation="d\u0117mesingas \u2192 d\u0117mesingumas. U\u017e K\u0104? \u2192 d\u0117mesingum\u0105.",
        ru="Внимательность. -ingas \u2192 -ingumas."),
    _i("Образуйте наречие от <b>profesionalus</b> (профессиональный):\n"
        "<i>\u201eJi dirba labai _____.\u201c</i>",
        ["profesionaliai"],
        hint="-us \u2192 -iai",
        explanation="profesionalus \u2192 profesionaliai.",
        ru="Профессионально. -us \u2192 -iai."),
]

# -------------------------------------------------------------------
# SKYRYBA Drill 1 - Punctuation (8 choice)
# -------------------------------------------------------------------
EXERCISES["skyryba_1"] = [
    _c("Где нужна запятая?\n<i>\u201e\u017dinau __ kad jis ateis.\u201c</i>",
        ["\u017dinau, kad jis ateis.", "\u017dinau kad, jis ateis.",
         "\u017dinau kad jis, ateis.", "\u017dinau kad jis ateis."], 0,
        hint="Запятая перед \u201ekad\u201c",
        explanation="Запятая перед \u201ekad\u201c (подчинительный союз).",
        ru="Запятая перед \u201ekad\u201c \u2014 всегда!", topic="Перед kad"),
    _c("Правильная пунктуация?\n<i>\u201e\u017dmogus skaitantis knyg\u0105 s\u0117d\u0117jo parke.\u201c</i>\n"
        "(Причастие ПОСЛЕ определяемого)",
        ["\u017dmogus, skaitantis knyg\u0105, s\u0117d\u0117jo parke.",
         "\u017dmogus skaitantis knyg\u0105, s\u0117d\u0117jo parke.",
         "\u017dmogus, skaitantis knyg\u0105 s\u0117d\u0117jo parke.",
         "\u017dmogus skaitantis, knyg\u0105 s\u0117d\u0117jo parke."], 0,
        hint="Причастный оборот ПОСЛЕ определяемого \u2192 запятые с обеих сторон",
        explanation="Причастный оборот после определяемого слова выделяется запятыми.",
        ru="Как в русском!", topic="Dalyvinis pa\u017eyminys"),
    _c("Правильная пунктуация?\n<i>\u201eGr\u012f\u017edamas namo jis pamat\u0117 kaimyn\u0105.\u201c</i>",
        ["Gr\u012f\u017edamas namo, jis pamat\u0117 kaimyn\u0105.",
         "Gr\u012f\u017edamas, namo jis pamat\u0117 kaimyn\u0105.",
         "Gr\u012f\u017edamas namo jis, pamat\u0117 kaimyn\u0105.",
         "Gr\u012f\u017edamas namo jis pamat\u0117, kaimyn\u0105."], 0,
        hint="Оборот с pusdalyvis \u2192 запятая после оборота",
        explanation="Pusdalyvis оборот отделяется запятой.",
        ru="Деепричастный оборот \u2192 запятая.", topic="Pusdalyvis"),
    _c("Нужна ли запятая?\n<i>\u201eJis pirko duonos pieno ir sviesto.\u201c</i>",
        ["Jis pirko duonos, pieno ir sviesto.",
         "Jis pirko duonos pieno, ir sviesto.",
         "Jis pirko, duonos pieno ir sviesto.",
         "Jis pirko duonos pieno ir, sviesto."], 0,
        hint="Однородные через запятую, перед одиночным \u201eir\u201c \u2014 нет",
        explanation="Между однородными \u2014 запятая, перед одиночным \u201eir\u201c \u2014 нет.",
        ru="Как в русском: хлеба, молока и масла.", topic="Однородные + ir"),
    _c("<i>\u201eNors lyja __ mes vis tiek eisime.\u201c</i>",
        ["Nors lyja, mes vis tiek eisime.",
         "Nors, lyja mes vis tiek eisime.",
         "Nors lyja mes, vis tiek eisime.",
         "Nors lyja mes vis tiek, eisime."], 0,
        hint="После придаточного с \u201enors\u201c \u2192 запятая",
        explanation="Придаточное отделяется запятой от главного.",
        ru="Запятая между придаточным и главным.", topic="Перед nors"),
    _c("<i>\u201eSkaitantis knyg\u0105 \u017emogus atsisedo ant suolo.\u201c</i>\nНужна ли запятая?",
        ["Запятая не нужна \u2014 оборот ПЕРЕД определяемым словом",
         "Нужна: Skaitantis, knyg\u0105 \u017emogus...",
         "Нужна: Skaitantis knyg\u0105, \u017emogus...",
         "Нужна: Skaitantis knyg\u0105 \u017emogus, atsisedo..."], 0,
        hint="Причастный оборот ПЕРЕД определяемым \u2192 без запятой",
        explanation="ПЕРЕД определяемым словом \u2014 запятая не нужна.",
        ru="Совпадает с русским!", topic="Dalyvinis PRIE\u0160"),
    _c("<i>\u201eA\u0161 ateisiu jei tur\u0117siu laiko.\u201c</i>\nПоставьте запятую.",
        ["A\u0161 ateisiu, jei tur\u0117siu laiko.",
         "A\u0161 ateisiu jei, tur\u0117siu laiko.",
         "A\u0161, ateisiu jei tur\u0117siu laiko.",
         "A\u0161 ateisiu jei tur\u0117siu, laiko."], 0,
        hint="Перед \u201ejei\u201c (если) \u2192 всегда запятая",
        explanation="Запятая перед \u201ejei\u201c (условный союз).",
        ru="Перед \u201eесли\u201c \u2014 запятая.", topic="Перед jei"),
    _c("Как оформить прямую речь по-литовски?\n"
        "Он сказал: \u201eЯ приду завтра.\u201c",
        ["Jis pasak\u0117: \u201eA\u0161 ateisiu rytoj.\u201c",
         "Jis pasak\u0117: \u00abA\u0161 ateisiu rytoj.\u00bb",
         "Jis pasak\u0117: \"A\u0161 ateisiu rytoj.\"",
         "Jis pasak\u0117 \u201eA\u0161 ateisiu rytoj.\u201c"], 0,
        hint="Литовские кавычки: \u201e \u201c (внизу-вверху)",
        explanation="Литовские кавычки: \u201e \u201c (открывающая внизу, закрывающая вверху).",
        ru="В литовском кавычки \u201e \u201c (не \u00ab \u00bb и не \" \").", topic="Прямая речь"),
]


# ===================================================================
# Getter functions
# ===================================================================

def get_exercises(module_id, drill_num):
    """Return list of exercise dicts for a given module and drill number."""
    return EXERCISES.get(f"{module_id}_{drill_num}", [])


def get_theory(topic_id):
    """Return list of theory page strings for a given topic."""
    return THEORY.get(topic_id, [])


def get_module(module_id):
    """Return module definition dict or None."""
    for m in MODULES:
        if m["id"] == module_id:
            return m
    return None
