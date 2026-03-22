// ═══════════════════════════════════════════════════════════════
// DALYVIAI — EXPANDED THEORY & DRILLS 4–7 (B2)
// Called from index.html as global functions
// ═══════════════════════════════════════════════════════════════

function getDalyviaiExpandedTheory() {
  return `
    <!-- ──────── 1. КАК ОБРАЗОВАТЬ КАЖДЫЙ ТИП ПРИЧАСТИЯ ──────── -->
    <div class="card">
      <h3>1. Как образовать каждый тип причастия — пошаговые правила</h3>
      <p class="subtitle">Полная система литовских причастий с примерами I и II спряжения</p>

      <div class="theory-block">
        <h4>Общий принцип</h4>
        <p>Литовские причастия образуются от <strong>основы глагола</strong>. Чтобы правильно образовать причастие, нужно знать:</p>
        <p>1) <strong>Спряжение</strong> (I: -a / II: -i в 3-м лице наст. вр.)<br>
        2) <strong>Основу настоящего времени</strong> (3-е лицо без окончания)<br>
        3) <strong>Основу прошедшего времени</strong> (3-е лицо без окончания)<br>
        4) <strong>Основу инфинитива</strong> (без -ti/-yti)</p>
        <p class="ru-note">Запомните: I спряжение → суффиксы с <strong>-a-</strong> (antis, amas); II спряжение → суффиксы с <strong>-i-</strong> (intis, imas).</p>
      </div>

      <h4 style="margin-top:20px">1.1 Veikiamasis esamojo laiko dalyvis (действ. прич. наст. вр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа 3-го лица наст. вр. + <em>-antis/-anti</em> (I спр.) или <em>-intis/-inti</em> (II спр.)</p>
        <p><strong>Шаг 1:</strong> Найти 3-е лицо наст. вр.: dirba, rašo, myli<br>
        <strong>Шаг 2:</strong> Убрать гласное окончание: dirb-, raš-, myl-<br>
        <strong>Шаг 3:</strong> Добавить суффикс по спряжению</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>3 asm. esam.</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti (I)</td><td>dirba</td><td>dirb<strong>antis</strong></td><td>dirb<strong>anti</strong></td><td>работающий/-ая</td></tr>
        <tr><td>rašyti (I)</td><td>rašo</td><td>raš<strong>antis</strong></td><td>raš<strong>anti</strong></td><td>пишущий/-ая</td></tr>
        <tr><td>eiti (I)</td><td>eina</td><td>ein<strong>antis</strong></td><td>ein<strong>anti</strong></td><td>идущий/-ая</td></tr>
        <tr><td>mylėti (II)</td><td>myli</td><td>myl<strong>intis</strong></td><td>myl<strong>inti</strong></td><td>любящий/-ая</td></tr>
        <tr><td>kalbėti (II)</td><td>kalba</td><td>kalb<strong>antis</strong></td><td>kalb<strong>anti</strong></td><td>говорящий/-ая</td></tr>
        <tr><td>matyti (II)</td><td>mato</td><td>mat<strong>antis</strong></td><td>mat<strong>anti</strong></td><td>видящий/-ая</td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">Мнемоника: <strong>«А — Активный, сейчАс»</strong>. I спряжение = -Antis. Если 3-е лицо на -a → убирай -a, ставь -antis.</p>

      <h4 style="margin-top:20px">1.2 Veikiamasis būtojo kartinio laiko dalyvis (действ. прич. прош. однокр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа 3-го лица прош. вр. + <em>-ęs/-usi</em></p>
        <p><strong>Шаг 1:</strong> Найти 3-е лицо прош. вр.: dirbo, rašė, mylėjo<br>
        <strong>Шаг 2:</strong> Убрать окончание: dirb-, raš-, mylėj-<br>
        <strong>Шаг 3:</strong> Добавить -ęs (м.р.) / -usi (ж.р.)</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>3 asm. būt.</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti</td><td>dirbo</td><td>dirb<strong>ęs</strong></td><td>dirb<strong>usi</strong></td><td>работавший/-ая</td></tr>
        <tr><td>rašyti</td><td>rašė</td><td>raš<strong>ęs</strong></td><td>raš<strong>iusi</strong></td><td>писавший/-ая</td></tr>
        <tr><td>mylėti</td><td>mylėjo</td><td>mylėj<strong>ęs</strong></td><td>mylėj<strong>usi</strong></td><td>любивший/-ая</td></tr>
        <tr><td>eiti</td><td>ėjo</td><td>ėj<strong>ęs</strong></td><td>ėj<strong>usi</strong></td><td>шедший/-ая</td></tr>
        <tr><td>skaityti</td><td>skaitė</td><td>skait<strong>ęs</strong></td><td>skaič<strong>iusi</strong></td><td>читавший/-ая</td></tr>
        <tr><td>statyti</td><td>statė</td><td>stat<strong>ęs</strong></td><td>stač<strong>iusi</strong></td><td>строивший/-ая</td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">Мнемоника: <strong>«-ĘS = прошлОЕ»</strong>. Женский род: если основа на согласный → -usi, если на гласный → -iusi (rašė → raš-iusi).</p>

      <h4 style="margin-top:20px">1.3 Veikiamasis būtojo dažninio laiko dalyvis (действ. прич. прош. многокр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа инфинитива + <em>-davęs/-davusi</em></p>
        <p><strong>Шаг 1:</strong> Убрать -ti/-yti: dirb-, raš-, mylė-<br>
        <strong>Шаг 2:</strong> Добавить -davęs (м.р.) / -davusi (ж.р.)</p>
        <p class="ru-note">Это самый регулярный тип: одна формула для всех спряжений!</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti</td><td>dirb<strong>davęs</strong></td><td>dirb<strong>davusi</strong></td><td>обычно работавший/-ая</td></tr>
        <tr><td>rašyti</td><td>raš<strong>ydavęs</strong></td><td>raš<strong>ydavusi</strong></td><td>обычно писавший/-ая</td></tr>
        <tr><td>mylėti</td><td>mylė<strong>davęs</strong></td><td>mylė<strong>davusi</strong></td><td>обычно любивший/-ая</td></tr>
      </table>

      <h4 style="margin-top:20px">1.4 Veikiamasis būsimojo laiko dalyvis (действ. прич. буд. вр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа инфинитива + <em>-siantis/-sianti</em></p>
        <p><strong>Шаг 1:</strong> Убрать -ti: dirb-, raš-y-, mylė-<br>
        <strong>Шаг 2:</strong> Добавить -siantis (м.р.) / -sianti (ж.р.)</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti</td><td>dirb<strong>siantis</strong></td><td>dirb<strong>sianti</strong></td><td>тот, кто будет работать</td></tr>
        <tr><td>rašyti</td><td>raš<strong>ysiantis</strong></td><td>raš<strong>ysianti</strong></td><td>тот, кто будет писать</td></tr>
        <tr><td>mylėti</td><td>mylė<strong>siantis</strong></td><td>mylė<strong>sianti</strong></td><td>тот, кто будет любить</td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">Мнемоника: <strong>«-S- = будущее»</strong> (как в būsimasis laikas: dirb-s-iu).</p>

      <h4 style="margin-top:20px">1.5 Neveikiamasis esamojo laiko dalyvis (страд. прич. наст. вр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа 3-го лица наст. вр. + <em>-amas/-ama</em> (I спр.) или <em>-imas/-ima</em> (II спр.)</p>
        <p><strong>Шаг 1:</strong> Найти 3-е лицо наст. вр.: dirba, myli<br>
        <strong>Шаг 2:</strong> Убрать гласное окончание: dirb-, myl-<br>
        <strong>Шаг 3:</strong> Добавить -amas/-ama (I спр.) или -imas/-ima (II спр.)</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti (I)</td><td>dirb<strong>amas</strong></td><td>dirb<strong>ama</strong></td><td>делаемый/-ая</td></tr>
        <tr><td>rašyti (I)</td><td>raš<strong>omas</strong></td><td>raš<strong>oma</strong></td><td>пишемый/-ая (писаный)</td></tr>
        <tr><td>statyti (I)</td><td>stat<strong>omas</strong></td><td>stat<strong>oma</strong></td><td>строящийся</td></tr>
        <tr><td>mylėti (II)</td><td>myl<strong>imas</strong></td><td>myl<strong>ima</strong></td><td>любимый/-ая</td></tr>
        <tr><td>matyti (II)</td><td>mat<strong>omas</strong></td><td>mat<strong>oma</strong></td><td>видимый/-ая</td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">Совпадает с русским: работа-ем-ый, люб-им-ый. I спр. → -amas (как -емый), II спр. → -imas (как -имый).</p>

      <h4 style="margin-top:20px">1.6 Neveikiamasis būtojo laiko dalyvis (страд. прич. прош. вр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа инфинитива + <em>-tas/-ta</em></p>
        <p>Для глаголов на -yti: основа на -y- → -ytas/-yta</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti</td><td>dirb<strong>tas</strong></td><td>dirb<strong>ta</strong></td><td>сделанный/-ая</td></tr>
        <tr><td>rašyti</td><td>raš<strong>ytas</strong></td><td>raš<strong>yta</strong></td><td>написанный/-ая</td></tr>
        <tr><td>pastatyti</td><td>pastat<strong>ytas</strong></td><td>pastat<strong>yta</strong></td><td>построенный/-ая</td></tr>
        <tr><td>mylėti</td><td>mylė<strong>tas</strong></td><td>mylė<strong>ta</strong></td><td>любленный/-ая</td></tr>
        <tr><td>pirkti</td><td>pirk<strong>tas</strong></td><td>pirk<strong>ta</strong></td><td>купленный/-ая</td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">Мнемоника: <strong>«-TAS = сделано»</strong>. Как русское краткое причастие: сделан, написан.</p>

      <h4 style="margin-top:20px">1.7 Neveikiamasis būsimojo laiko dalyvis (страд. прич. буд. вр.)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа инфинитива + <em>-simas/-sima</em></p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. g.</th><th>Mot. g.</th><th>Перевод</th></tr>
        <tr><td>dirbti</td><td>dirb<strong>simas</strong></td><td>dirb<strong>sima</strong></td><td>тот, что будет делаться</td></tr>
        <tr><td>rašyti</td><td>raš<strong>ysimas</strong></td><td>raš<strong>ysima</strong></td><td>тот, что будет писаться</td></tr>
        <tr><td>mylėti</td><td>mylė<strong>simas</strong></td><td>mylė<strong>sima</strong></td><td>тот, что будет любим</td></tr>
      </table>

      <h4 style="margin-top:20px">1.8 Pusdalyvis (полупричастие / деепричастие одновременности)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> основа инфинитива + <em>-damas/-dama</em></p>
        <p><strong>Важно:</strong> согласуется с подлежащим в <strong>роде и числе</strong>!</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. g. vns.</th><th>Mot. g. vns.</th><th>Vyr. g. dgs.</th><th>Mot. g. dgs.</th></tr>
        <tr><td>dirbti</td><td>dirb<strong>damas</strong></td><td>dirb<strong>dama</strong></td><td>dirb<strong>dami</strong></td><td>dirb<strong>damos</strong></td></tr>
        <tr><td>rašyti</td><td>raš<strong>ydamas</strong></td><td>raš<strong>ydama</strong></td><td>raš<strong>ydami</strong></td><td>raš<strong>ydamos</strong></td></tr>
        <tr><td>mylėti</td><td>mylė<strong>damas</strong></td><td>mylė<strong>dama</strong></td><td>mylė<strong>dami</strong></td><td>mylė<strong>damos</strong></td></tr>
        <tr><td>eiti</td><td>ei<strong>damas</strong></td><td>ei<strong>dama</strong></td><td>ei<strong>dami</strong></td><td>ei<strong>damos</strong></td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">Аналог русского деепричастия «делая, работая», но в литовском оно <strong>изменяется по роду и числу!</strong></p>

      <h4 style="margin-top:20px">1.9 Padalyvis (деепричастие предшествования)</h4>
      <div class="theory-block">
        <p><strong>Правило:</strong> форма совпадает с veik. būt. kart. dalyviu, но используется как обстоятельство</p>
        <p>Vyr. g.: <em>-ęs</em> (ед.ч.) / <em>-ę</em> (мн.ч.)<br>
        Mot. g.: <em>-usi</em> (ед.ч.) / <em>-usios</em> (мн.ч.)</p>
        <p><strong>Важно:</strong> обозначает действие, которое произошло <strong>ДО</strong> основного действия.</p>
      </div>
      <table class="grammar-table">
        <tr><th>Veiksmažodis</th><th>Vyr. vns.</th><th>Mot. vns.</th><th>Vyr. dgs.</th><th>Mot. dgs.</th><th>Перевод</th></tr>
        <tr><td>grįžti</td><td>grįž<strong>ęs</strong></td><td>grįž<strong>usi</strong></td><td>grįž<strong>ę</strong></td><td>grįž<strong>usios</strong></td><td>вернувшись</td></tr>
        <tr><td>perskaityti</td><td>perskait<strong>ęs</strong></td><td>perskaič<strong>iusi</strong></td><td>perskait<strong>ę</strong></td><td>perskaič<strong>iusios</strong></td><td>прочитав</td></tr>
        <tr><td>baigti</td><td>baig<strong>ęs</strong></td><td>baig<strong>usi</strong></td><td>baig<strong>ę</strong></td><td>baig<strong>usios</strong></td><td>закончив</td></tr>
        <tr><td>pavalgyti</td><td>pavalgęs</td><td>pavalgius<strong>i</strong></td><td>pavalgę</td><td>pavalgius<strong>ios</strong></td><td>поев</td></tr>
      </table>
      <p class="ru-note" style="margin-top:8px">В русском: «прочитав книгу, он...» = «Perskaitęs knygą, jis...». Но в литовском padalyvis <strong>согласуется с подлежащим</strong> по роду и числу!</p>

      <h4 style="margin-top:20px">Сводная таблица всех типов</h4>
      <table class="grammar-table">
        <tr><th>Tipas</th><th>Priesaga</th><th>dirbti</th><th>mylėti</th><th>Перевод</th></tr>
        <tr><td>Veik. esam.</td><td>-antis/-intis</td><td>dirbantis</td><td>mylintis</td><td>работающий / любящий</td></tr>
        <tr><td>Veik. būt. kart.</td><td>-ęs/-usi</td><td>dirbęs</td><td>mylėjęs</td><td>работавший / любивший</td></tr>
        <tr><td>Veik. būt. dažn.</td><td>-davęs/-davusi</td><td>dirbdavęs</td><td>mylėdavęs</td><td>обычно работавший</td></tr>
        <tr><td>Veik. būsim.</td><td>-siantis/-sianti</td><td>dirbsiantis</td><td>mylėsiantis</td><td>тот, кто будет работать</td></tr>
        <tr><td>Neveik. esam.</td><td>-amas/-imas</td><td>dirbamas</td><td>mylimas</td><td>делаемый / любимый</td></tr>
        <tr><td>Neveik. būt.</td><td>-tas/-ta</td><td>dirbtas</td><td>mylėtas</td><td>сделанный / любленный</td></tr>
        <tr><td>Neveik. būsim.</td><td>-simas/-sima</td><td>dirbsimas</td><td>mylėsimas</td><td>будет делаться</td></tr>
        <tr><td>Pusdalyvis</td><td>-damas/-dama</td><td>dirbdamas</td><td>mylėdamas</td><td>работая / любя</td></tr>
        <tr><td>Padalyvis</td><td>-ęs/-usi</td><td>dirbęs</td><td>mylėjęs</td><td>поработав / полюбив</td></tr>
      </table>
    </div>

    <!-- ──────── 2. PUSDALYVIS vs PADALYVIS ──────── -->
    <div class="card">
      <h3>2. Pusdalyvis vs Padalyvis — подробное сравнение</h3>
      <p class="subtitle">Самая частая ловушка на B2 экзамене: два типа деепричастий</p>

      <div class="theory-block">
        <h4>Pusdalyvis (-damas/-dama) — одновременное действие</h4>
        <p>Используется, когда два действия происходят <strong>одновременно</strong>.</p>
        <p><strong>Образование:</strong> основа инфинитива + -damas / -dama / -dami / -damos</p>
        <p><strong>Согласование:</strong> с подлежащим в <strong>роде</strong> и <strong>числе</strong></p>
        <p><em>Jis ėjo <strong>dainuodamas</strong>.</em> — Он шёл, <u>напевая</u> (одновременно).</p>
        <p><em>Ji ėjo <strong>dainuodama</strong>.</em> — Она шла, <u>напевая</u> (одновременно).</p>
        <p><em>Jie ėjo <strong>dainuodami</strong>.</em> — Они шли, <u>напевая</u> (одновременно).</p>
      </div>

      <div class="theory-block" style="margin-top:16px">
        <h4>Padalyvis — предшествующее действие</h4>
        <p>Используется, когда одно действие произошло <strong>раньше</strong> другого.</p>
        <p><strong>Образование:</strong> как veik. būt. kart. dalyvis: -ęs / -usi / -ę / -usios</p>
        <p><strong>Согласование:</strong> с подлежащим в <strong>роде</strong> и <strong>числе</strong></p>
        <p><em><strong>Grįžęs</strong> namo, jis atsisėdo.</em> — <u>Вернувшись</u> домой, он сел.</p>
        <p><em><strong>Grįžusi</strong> namo, ji atsisėdo.</em> — <u>Вернувшись</u> домой, она села.</p>
        <p><em><strong>Grįžę</strong> namo, jie atsisėdo.</em> — <u>Вернувшись</u> домой, они сели.</p>
      </div>

      <h4 style="margin-top:20px">Контрастные примеры</h4>
      <table class="grammar-table">
        <tr><th>Pusdalyvis (одновременно)</th><th>Padalyvis (предшествование)</th></tr>
        <tr>
          <td><em><strong>Skaitydama</strong> knygą, ji gėrė kavą.</em><br>Читая книгу, она пила кофе. (= одновременно)</td>
          <td><em><strong>Perskaičiusi</strong> knygą, ji ją padėjo.</em><br>Прочитав книгу, она её положила. (= сначала прочитала, потом положила)</td>
        </tr>
        <tr>
          <td><em><strong>Valgydami</strong> pietus, jie kalbėjosi.</em><br>Обедая, они разговаривали. (= одновременно)</td>
          <td><em><strong>Pavalgę</strong> pietus, jie išėjo pasivaikščioti.</em><br>Пообедав, они пошли гулять. (= сначала пообедали)</td>
        </tr>
        <tr>
          <td><em>Jis dirbo <strong>klausydamas</strong> muzikos.</em><br>Он работал, слушая музыку. (= одновременно)</td>
          <td><em><strong>Išklausęs</strong> paskaitą, jis parašė ataskaitą.</em><br>Прослушав лекцию, он написал отчёт. (= сначала прослушал)</td>
        </tr>
        <tr>
          <td><em><strong>Eidama</strong> gatve, ji sutiko draugę.</em><br>Идя по улице, она встретила подругу. (= одновременно)</td>
          <td><em><strong>Atėjusi</strong> į darbą, ji patikrino paštą.</em><br>Придя на работу, она проверила почту. (= сначала пришла)</td>
        </tr>
        <tr>
          <td><em>Vaikai žaidė <strong>šaukdami</strong>.</em><br>Дети играли, крича. (= одновременно)</td>
          <td><em><strong>Baigę</strong> pamokas, vaikai išbėgo į kiemą.</em><br>Закончив уроки, дети выбежали во двор. (= сначала закончили)</td>
        </tr>
      </table>

      <div class="theory-block" style="margin-top:16px">
        <h4>Экзаменационные ловушки</h4>
        <p>❌ <strong>Ошибка 1:</strong> Pusdalyvis для последовательных действий<br>
        <em>*Dirbdamas darbą, jis išėjo namo.</em> — НЕПРАВИЛЬНО (нельзя работать и уйти одновременно)<br>
        ✅ <em><strong>Baigęs</strong> darbą, jis išėjo namo.</em></p>

        <p>❌ <strong>Ошибка 2:</strong> Padalyvis для одновременных действий<br>
        <em>*Baigęs darbą, jis klausėsi radijo.</em> — двусмысленно, если имеется в виду «работая, слушал»<br>
        ✅ <em><strong>Dirbdamas</strong>, jis klausėsi radijo.</em></p>

        <p>❌ <strong>Ошибка 3:</strong> Несогласование pusdalyvis по роду<br>
        <em>*Ji ėjo <strong>dainuodamas</strong>.</em> — м.р. при подлежащем ж.р.!<br>
        ✅ <em>Ji ėjo <strong>dainuodama</strong>.</em></p>

        <p class="ru-note">Главный тест: можно ли делать оба действия ОДНОВРЕМЕННО? Да → pusdalyvis (-damas). Нет → padalyvis (-ęs).</p>
      </div>
    </div>

    <!-- ──────── 3. ЗАМЕНА ПРИДАТОЧНЫХ ПРИЧАСТНЫМИ ОБОРОТАМИ ──────── -->
    <div class="card">
      <h3>3. Замена придаточных предложений причастными оборотами</h3>
      <p class="subtitle">«kuris + глагол» → причастный оборот — ключевой навык B2</p>

      <div class="theory-block">
        <h4>Общее правило</h4>
        <p>Придаточное с <strong>kuris/kuri</strong> заменяется причастием, которое <strong>совпадает по времени</strong> с глаголом в придаточном:</p>
        <p>• kuris + наст. вр. → veik. esamojo laiko dalyvis (-antis/-anti)<br>
        • kuris + прош. вр. → veik. būtojo kartinio laiko dalyvis (-ęs/-usi)<br>
        • kurį + наст. вр. (пассив) → neveik. esamojo laiko dalyvis (-amas/-ama)<br>
        • kurį + прош. вр. (пассив) → neveik. būtojo laiko dalyvis (-tas/-ta)</p>
        <p class="ru-note">Причастие должно согласоваться с определяемым словом в <strong>роде, числе и падеже</strong>.</p>
      </div>

      <h4 style="margin-top:20px">Пошаговые трансформации</h4>

      <div class="theory-block">
        <h4>Пример 1: Настоящее время, активный залог</h4>
        <p><strong>Исходное:</strong> <em>Žmogus, <u>kuris skaito</u> knygą, sėdi parke.</em><br>
        Человек, <u>который читает</u> книгу, сидит в парке.</p>
        <p><strong>Шаг 1:</strong> kuris skaito → причастие наст. вр. акт. = skaitantis<br>
        <strong>Шаг 2:</strong> Согласуем с «žmogus» (м.р., ед.ч., V.) = skaitantis<br>
        <strong>Результат:</strong> <em>Knygą <strong>skaitantis</strong> žmogus sėdi parke.</em> или <em>Žmogus, <strong>skaitantis</strong> knygą, sėdi parke.</em></p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>Пример 2: Прошедшее время, активный залог</h4>
        <p><strong>Исходное:</strong> <em>Draugas, <u>kuris parašė</u> laišką, išvyko.</em><br>
        Друг, <u>который написал</u> письмо, уехал.</p>
        <p><strong>Шаг 1:</strong> kuris parašė → причастие прош. вр. акт. = parašęs<br>
        <strong>Шаг 2:</strong> Согласуем с «draugas» (м.р., ед.ч., V.) = parašęs<br>
        <strong>Результат:</strong> <em>Laišką <strong>parašęs</strong> draugas išvyko.</em></p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>Пример 3: Прошедшее время, пассивный залог</h4>
        <p><strong>Исходное:</strong> <em>Laiškas, <u>kurį parašė</u> draugas, buvo ilgas.</em><br>
        Письмо, <u>которое написал</u> друг, было длинным.</p>
        <p><strong>Шаг 1:</strong> kurį parašė → страд. прич. прош. вр. = parašytas<br>
        <strong>Шаг 2:</strong> Согласуем с «laiškas» (м.р., ед.ч., V.) = parašytas<br>
        <strong>Шаг 3:</strong> Автор действия → kilmininkas (Gen.): draugo<br>
        <strong>Результат:</strong> <em>Draugo <strong>parašytas</strong> laiškas buvo ilgas.</em></p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>Пример 4: Настоящее время, пассивный залог</h4>
        <p><strong>Исходное:</strong> <em>Namas, <u>kurį stato</u> darbininkai, yra didelis.</em><br>
        Дом, <u>который строят</u> рабочие, большой.</p>
        <p><strong>Шаг 1:</strong> kurį stato → страд. прич. наст. вр. = statomas<br>
        <strong>Шаг 2:</strong> Согласуем с «namas» (м.р., ед.ч., V.) = statomas<br>
        <strong>Шаг 3:</strong> Автор → kilmininkas: darbininkų<br>
        <strong>Результат:</strong> <em>Darbininkų <strong>statomas</strong> namas yra didelis.</em></p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>Пример 5: Множественное число, женский род</h4>
        <p><strong>Исходное:</strong> <em>Moterys, <u>kurios dirba</u> ligoninėje, yra patyrusios.</em><br>
        Женщины, <u>которые работают</u> в больнице, опытные.</p>
        <p><strong>Шаг 1:</strong> kurios dirba → причастие наст. вр. акт. = dirbančios<br>
        <strong>Шаг 2:</strong> Согласуем с «moterys» (ж.р., мн.ч., V.) = dirbančios<br>
        <strong>Результат:</strong> <em>Ligoninėje <strong>dirbančios</strong> moterys yra patyrusios.</em></p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>Пример 6: Будущее время, активный залог</h4>
        <p><strong>Исходное:</strong> <em>Studentas, <u>kuris studijuos</u> Vilniuje, gavo stipendiją.</em><br>
        Студент, <u>который будет учиться</u> в Вильнюсе, получил стипендию.</p>
        <p><strong>Шаг 1:</strong> kuris studijuos → причастие буд. вр. акт. = studijuosiantis<br>
        <strong>Шаг 2:</strong> Согласуем с «studentas» (м.р., ед.ч., V.) = studijuosiantis<br>
        <strong>Результат:</strong> <em>Vilniuje <strong>studijuosiantis</strong> studentas gavo stipendiją.</em></p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>Пример 7: Косвенный падеж (Galininkas)</h4>
        <p><strong>Исходное:</strong> <em>Matau žmogų, <u>kuris bėga</u> parke.</em><br>
        Вижу человека, <u>который бежит</u> в парке.</p>
        <p><strong>Шаг 1:</strong> kuris bėga → причастие наст. вр. акт. = bėgantis<br>
        <strong>Шаг 2:</strong> Согласуем с «žmogų» (м.р., ед.ч., <strong>G.</strong>) = bėgantį<br>
        <strong>Результат:</strong> <em>Matau parke <strong>bėgantį</strong> žmogų.</em></p>
      </div>

      <table class="grammar-table" style="margin-top:16px">
        <tr><th>Придаточное с kuris</th><th>Причастный оборот</th><th>Тип причастия</th></tr>
        <tr><td>kuris skaito</td><td>skaitantis</td><td>veik. esam.</td></tr>
        <tr><td>kuris skaitė</td><td>skaitęs</td><td>veik. būt. kart.</td></tr>
        <tr><td>kuris skaitys</td><td>skaitysiantis</td><td>veik. būsim.</td></tr>
        <tr><td>kurį skaito (kažkas)</td><td>skaitomas</td><td>neveik. esam.</td></tr>
        <tr><td>kurį skaitė (kažkas)</td><td>skaitytas</td><td>neveik. būt.</td></tr>
        <tr><td>kurį skaitys (kažkas)</td><td>skaitysimas</td><td>neveik. būsim.</td></tr>
      </table>
    </div>

    <!-- ──────── 4. ЧАСТЫЕ ОШИБКИ ──────── -->
    <div class="card">
      <h3>4. Dažnos klaidos / Частые ошибки русскоязычных</h3>
      <p class="subtitle">На что обращать внимание на экзамене B2</p>

      <div class="theory-block">
        <h4>❌ Ошибка 1: Неправильный тип причастия</h4>
        <p>❌ <em>Aš mačiau <strong>dirbantis</strong> žmogų.</em> (veik. esam. V. вместо G.)<br>
        ✅ <em>Aš mačiau <strong>dirbantį</strong> žmogų.</em> (veik. esam. G. — «видел работающего человека»)</p>
        <p class="ru-note">Причастие — это прилагательное! Оно склоняется по падежам, как и существительное, к которому относится.</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 2: Несогласование pusdalyvis по роду</h4>
        <p>❌ <em>Mergaitė bėgo <strong>šaukdamas</strong>.</em> (м.р. при подлежащем ж.р.)<br>
        ✅ <em>Mergaitė bėgo <strong>šaukdama</strong>.</em> (ж.р. — согласование с «mergaitė»)</p>
        <p class="ru-note">В русском деепричастие «крича» не изменяется по роду. В литовском — изменяется! Всегда проверяйте подлежащее.</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 3: Путаница pusdalyvis и padalyvis</h4>
        <p>❌ <em><strong>Grįždamas</strong> namo, jis nusipirko duonos.</em> (= шёл домой и одновременно купил хлеб?)<br>
        ✅ <em><strong>Grįždamas</strong> namo, jis dainavo.</em> (= шёл и пел — одновременно ✓)<br>
        ✅ <em><strong>Grįžęs</strong> namo, jis atsisėdo.</em> (= сначала вернулся, потом сел ✓)</p>
        <p class="ru-note">Тест: если действия не могут происходить одновременно, используйте padalyvis (-ęs), а не pusdalyvis (-damas).</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 4: Неправильный падеж причастия в обороте</h4>
        <p>❌ <em>Kalbėjau su dirbant<strong>is</strong> žmogumi.</em> (V. вместо Įn.)<br>
        ✅ <em>Kalbėjau su dirbanč<strong>iu</strong> žmogumi.</em> (Įn. — «разговаривал с работающим человеком»)</p>
        <p class="ru-note">Причастие стоит в том же падеже, что и существительное! su + Įn. → dirbančiu.</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 5: Калька с русского порядка слов</h4>
        <p>❌ <em><strong>Skaitantis</strong> knygą <strong>žmogus</strong> sėdi parke.</em> (причастие далеко от существительного — допустимо, но часто путают порядок)<br>
        ✅ <em>Knygą <strong>skaitantis žmogus</strong> sėdi parke.</em> (причастие непосредственно перед существительным)</p>
        <p class="ru-note">В литовском причастный оборот обычно ставится <strong>перед</strong> определяемым словом, а дополнения причастия — перед причастием.</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 6: Активное причастие вместо пассивного</h4>
        <p>❌ <em>Knyga, <strong>rašiusi</strong> autoriaus...</em> (= книга, которая писала автора??)<br>
        ✅ <em>Autoriaus <strong>parašyta</strong> knyga...</em> (= написанная автором книга)</p>
        <p class="ru-note">Если подлежащее не является деятелем (книга не пишет!), нужно страдательное причастие.</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 7: Смешение спряжений в суффиксах</h4>
        <p>❌ <em>myl<strong>antis</strong></em> (I спр. суффикс для глагола II спр.)<br>
        ✅ <em>myl<strong>intis</strong></em> (II спр. → -intis)</p>
        <p>❌ <em>dirb<strong>imas</strong></em> (II спр. суффикс для глагола I спр.)<br>
        ✅ <em>dirb<strong>amas</strong></em> (I спр. → -amas)</p>
        <p class="ru-note">Правило: I спр. (3 asm. на -a) → суффиксы с -a- (-antis, -amas). II спр. (3 asm. на -i) → суффиксы с -i- (-intis, -imas).</p>
      </div>

      <div class="theory-block" style="margin-top:12px">
        <h4>❌ Ошибка 8: Пропуск приставки в padalyvis</h4>
        <p>❌ <em><strong>Skaitęs</strong> knygą, jis ją padėjo.</em> (без приставки — не передаёт завершённость)<br>
        ✅ <em><strong>Perskaitęs</strong> knygą, jis ją padėjo.</em> (per- = до конца)</p>
        <p class="ru-note">Padalyvis обычно используется с приставочными (совершенными) глаголами, т.к. обозначает завершённое действие.</p>
      </div>
    </div>
  `;
}


// ═══════════════════════════════════════════════════════════════
// DRILL 4 — Dalyvių linksniavimas (склонение причастий)
// 15 exercises: 8 choice + 7 input
// ═══════════════════════════════════════════════════════════════

function getDalyviaiDrill4() {
  return [
    {
      type: 'choice',
      question: 'Matau <strong>(bėgti, veik. esam., vyr., G.)</strong> vaiką.<br><br>Вижу <u>бегущего</u> ребёнка.',
      options: ['bėgantį', 'bėgantis', 'bėgančiu', 'bėgančiam'],
      correct: 0,
      topic: 'Veik. esam. + G.',
      hint: 'Matau KĄ? → Galininkas (G.). Bėgantis → bėgantį.',
      explanation: 'bėgantis (V.) → bėgantį (G.). Veikiamasis esamojo laiko dalyvis, vyr. g., vns., galininkas.',
      ruExplanation: 'Вижу КОГО? → Винительный падеж (Galininkas). Бегущий → бегущего = bėgantį.'
    },
    {
      type: 'choice',
      question: 'Kalbėjau su <strong>(atvykti, veik. būt. kart., vyr., Įn.)</strong> svečiu.<br><br>Разговаривал с <u>прибывшим</u> гостем.',
      options: ['atvykusiu', 'atvykęs', 'atvykusiam', 'atvykusį'],
      correct: 0,
      topic: 'Veik. būt. kart. + Įn.',
      hint: 'Su KUO? → Įnagininkas. Atvykęs → atvykusiu.',
      explanation: 'atvykęs (V.) → atvykusiu (Įn.). Su + Įnagininkas.',
      ruExplanation: 'Разговаривал С КЕМ? → Творительный падеж (Įnagininkas). Прибывший → прибывшим = atvykusiu.'
    },
    {
      type: 'choice',
      question: 'Knygoje rašoma apie mieste <strong>(gyventi, veik. esam., dgs., G.)</strong> žmones.<br><br>В книге пишется о <u>живущих</u> в городе людях.',
      options: ['gyvenančius', 'gyvenantys', 'gyvenančių', 'gyvenančiuose'],
      correct: 0,
      topic: 'Veik. esam. + G. dgs.',
      hint: 'Apie KĄ? → Galininkas. Daugiskaita: gyvenantys → gyvenančius.',
      explanation: 'gyvenantys (V. dgs.) → gyvenančius (G. dgs.). Apie + galininkas.',
      ruExplanation: 'О КОГО? (лит. apie + G.) → Винительный падеж мн.ч. Живущие → живущих = gyvenančius.'
    },
    {
      type: 'choice',
      question: 'Tai yra darbininkų <strong>(statyti, neveik. esam., vyr., V.)</strong> namas.<br><br>Это <u>строящийся</u> рабочими дом.',
      options: ['statomas', 'statomą', 'statomam', 'statomu'],
      correct: 0,
      topic: 'Neveik. esam. + V.',
      hint: 'Namas yra KAS? → Vardininkas. Statyti → statomas.',
      explanation: 'statomas — neveikiamasis esamojo laiko dalyvis, vyr. g., vns., vardininkas.',
      ruExplanation: 'Дом — это ЧТО? → Именительный падеж (Vardininkas). Строящийся = statomas.'
    },
    {
      type: 'choice',
      question: 'Sėdėjau prie <strong>(degti, veik. esam., vyr., K.)</strong> laužo.<br><br>Сидел у <u>горящего</u> костра.',
      options: ['degančio', 'degantis', 'degantį', 'degančiam'],
      correct: 0,
      topic: 'Veik. esam. + K.',
      hint: 'Prie KO? → Kilmininkas. Degantis → degančio.',
      explanation: 'degantis (V.) → degančio (K.). Prie + kilmininkas.',
      ruExplanation: 'У ЧЕГО? → Родительный падеж (Kilmininkas). Горящий → горящего = degančio.'
    },
    {
      type: 'choice',
      question: 'Mokytoja papasakojo apie <strong>(rašyti, neveik. būt., mot., G.)</strong> knygą.<br><br>Учительница рассказала о <u>написанной</u> книге.',
      options: ['parašytą', 'parašyta', 'parašytos', 'parašytai'],
      correct: 0,
      topic: 'Neveik. būt. + G.',
      hint: 'Apie KĄ? → Galininkas. Parašyta (V. mot.) → parašytą (G.).',
      explanation: 'parašyta (V.) → parašytą (G. mot. g. vns.). Apie + galininkas.',
      ruExplanation: 'О ЧТО? (лит. apie + G.) → Винительный падеж. Написанная → написанную = parašytą.'
    },
    {
      type: 'choice',
      question: 'Jis gyvena <strong>(pastatyti, neveik. būt., vyr., Vt.)</strong> name.<br><br>Он живёт в <u>построенном</u> доме.',
      options: ['pastatytame', 'pastatytas', 'pastatytą', 'pastatytu'],
      correct: 0,
      topic: 'Neveik. būt. + Vt.',
      hint: 'Gyvena KUR? Name → Vietininkas. Pastatytas → pastatytame.',
      explanation: 'pastatytas (V.) → pastatytame (Vt.). Vietininkas — „в построенном".',
      ruExplanation: 'Живёт ГДЕ? В доме → Местный падеж (Vietininkas). Построенный → построенном = pastatytame.'
    },
    {
      type: 'choice',
      question: '<strong>(kurti, veik. esam., mot., N.)</strong> menininkei reikia ramybės.<br><br><u>Творящей</u> художнице нужен покой.',
      options: ['kuriančiai', 'kurianti', 'kuriančios', 'kuriančią'],
      correct: 0,
      topic: 'Veik. esam. + N.',
      hint: 'Reikia KAM? → Naudininkas. Kurianti → kuriančiai.',
      explanation: 'kurianti (V.) → kuriančiai (N. mot. g. vns.). Naudininkas — кому нужен покой.',
      ruExplanation: 'Нужен покой КОМУ? → Дательный падеж (Naudininkas). Творящая → творящей = kuriančiai.'
    },
    {
      type: 'input',
      question: 'Užsienyje <strong>(gyventi, veik. esam., dgs., K.)</strong> lietuvių skaičius auga.<br><br>Число <u>живущих</u> за границей литовцев растёт.<br><br>Įrašykite tinkamą formą:',
      answer: ['gyvenančių'],
      topic: 'Veik. esam. + K. dgs.',
      hint: 'Lietuvių KO? → Kilmininkas dgs. Gyvenantys → gyvenančių.',
      explanation: 'gyvenantys (V. dgs.) → gyvenančių (K. dgs.). Kilmininkas daugiskaitos.',
      ruExplanation: 'Число КОГО? → Родительный падеж мн.ч. (Kilmininkas dgs.). Живущие → живущих = gyvenančių.'
    },
    {
      type: 'input',
      question: 'Policija ieško <strong>(dingti, veik. būt. kart., vyr., K.)</strong> žmogaus.<br><br>Полиция ищет <u>пропавшего</u> человека.<br><br>Įrašykite tinkamą formą:',
      answer: ['dingusio'],
      topic: 'Veik. būt. kart. + K.',
      hint: 'Ieško KO? → Kilmininkas. Dingęs → dingusio.',
      explanation: 'dingęs (V.) → dingusio (K. vyr. g. vns.). Ieškoti + kilmininkas.',
      ruExplanation: 'Ищет КОГО? → Родительный падеж (Kilmininkas). Пропавший → пропавшего = dingusio.'
    },
    {
      type: 'input',
      question: 'Padėkojau <strong>(padėti, veik. būt. kart., mot., N.)</strong> draugei.<br><br>Поблагодарил <u>помогавшую</u> подругу.<br><br>Įrašykite tinkamą formą:',
      answer: ['padėjusiai'],
      topic: 'Veik. būt. kart. + N.',
      hint: 'Padėkojau KAM? → Naudininkas. Padėjusi → padėjusiai.',
      explanation: 'padėjusi (V. mot.) → padėjusiai (N. mot. g. vns.).',
      ruExplanation: 'Поблагодарил КОМУ? → Дательный падеж (Naudininkas). Помогавшая → помогавшей = padėjusiai.'
    },
    {
      type: 'input',
      question: 'Vaikai žaidžia <strong>(pastatyti, neveik. būt., mot., Vt.)</strong> aikštelėje.<br><br>Дети играют на <u>построенной</u> площадке.<br><br>Įrašykite tinkamą formą:',
      answer: ['pastatytoje'],
      topic: 'Neveik. būt. + Vt.',
      hint: 'Aikštelėje KUR? → Vietininkas. Pastatyta → pastatytoje.',
      explanation: 'pastatyta (V. mot.) → pastatytoje (Vt. mot. g. vns.).',
      ruExplanation: 'Играют ГДЕ? На площадке → Местный падеж (Vietininkas). Построенная → построенной = pastatytoje.'
    },
    {
      type: 'input',
      question: 'Jis nuėjo pas <strong>(gyventi, veik. esam., mot., G.)</strong> kaimynę.<br><br>Он пошёл к <u>живущей</u> (рядом) соседке.<br><br>Įrašykite tinkamą formą:',
      answer: ['gyvenančią'],
      topic: 'Veik. esam. + G. mot.',
      hint: 'Pas KĄ? → Galininkas. Gyvenanti → gyvenančią.',
      explanation: 'gyvenanti (V. mot.) → gyvenančią (G. mot. g. vns.). Pas + galininkas.',
      ruExplanation: 'Пошёл К КОМУ? (лит. pas + G.) → Винительный падеж. Живущая → живущую = gyvenančią.'
    },
    {
      type: 'input',
      question: 'Mes gėrėjomės <strong>(žydėti, veik. esam., dgs., Įn.)</strong> gėlėmis.<br><br>Мы любовались <u>цветущими</u> цветами.<br><br>Įrašykite tinkamą formą:',
      answer: ['žydinčiomis'],
      topic: 'Veik. esam. + Įn. dgs.',
      hint: 'Gėrėjomės KUO? → Įnagininkas dgs. mot. g. Žydinčios → žydinčiomis.',
      explanation: 'žydinti (V. mot.) → žydinčios (V. dgs.) → žydinčiomis (Įn. dgs.).',
      ruExplanation: 'Любовались ЧЕМ? → Творительный падеж мн.ч. (Įnagininkas dgs.). Цветущие → цветущими = žydinčiomis.'
    },
    {
      type: 'input',
      question: 'Šiame mieste nėra gerai <strong>(mokėti, neveik. esam., vyr., K.)</strong> darbo.<br><br>В этом городе нет хорошо <u>оплачиваемой</u> работы.<br><br>Įrašykite tinkamą formą:',
      answer: ['mokamo'],
      topic: 'Neveik. esam. + K.',
      hint: 'Nėra KO? → Kilmininkas. Mokamas → mokamo (vyr. g. vns. K.).',
      explanation: 'mokamas (V.) → mokamo (K. vyr. g. vns.). Nėra + kilmininkas.',
      ruExplanation: 'Нет ЧЕГО? → Родительный падеж (Kilmininkas). Оплачиваемый → оплачиваемого = mokamo.'
    }
  ];
}


// ═══════════════════════════════════════════════════════════════
// DRILL 5 — Pusdalyvis ir padalyvis
// 15 exercises: 7 choice + 8 input
// ═══════════════════════════════════════════════════════════════

function getDalyviaiDrill5() {
  return [
    {
      type: 'choice',
      question: '_____ <strong>(grįžti, одновр., м.р.)</strong> namo, jis klausėsi muzikos.<br><br><u>Возвращаясь</u> домой, он слушал музыку.',
      options: ['Grįždamas', 'Grįžęs', 'Grįždama', 'Grįžusi'],
      correct: 0,
      topic: 'Pusdalyvis',
      hint: 'Одновременные действия: шёл домой + слушал музыку → pusdalyvis. Jis = vyr. g.',
      explanation: 'Grįždamas — pusdalyvis, vyr. g. Два действия одновременно: шёл и слушал.',
      ruExplanation: 'Возвращаясь (одновременно слушая). Подлежащее «jis» → мужской род → Grįždamas.'
    },
    {
      type: 'choice',
      question: '_____ <strong>(baigti, предшеств., ж.р.)</strong> darbą, ji išėjo namo.<br><br><u>Закончив</u> работу, она пошла домой.',
      options: ['Baigusi', 'Baigdama', 'Baigęs', 'Baigdamas'],
      correct: 0,
      topic: 'Padalyvis',
      hint: 'Последовательные действия: сначала закончила, потом пошла → padalyvis. Ji = mot. g.',
      explanation: 'Baigusi — padalyvis, mot. g. Сначала закончила работу, потом ушла.',
      ruExplanation: 'Закончив (сначала закончила, потом пошла). Подлежащее «ji» → женский род → Baigusi.'
    },
    {
      type: 'choice',
      question: '_____ <strong>(perskaityti, предшеств., дgs. vyr.)</strong> knygą, studentai ją aptarė.<br><br><u>Прочитав</u> книгу, студенты её обсудили.',
      options: ['Perskaitę', 'Perskaitydami', 'Perskaitęs', 'Perskaičiusios'],
      correct: 0,
      topic: 'Padalyvis dgs.',
      hint: 'Сначала прочитали, потом обсудили → padalyvis. Studentai = vyr. g. dgs. → -ę.',
      explanation: 'Perskaitę — padalyvis, vyr. g. dgs. Последовательные действия.',
      ruExplanation: 'Прочитав (сначала прочитали, потом обсудили). Множественное число мужского рода → Perskaitę.'
    },
    {
      type: 'choice',
      question: 'Vaikai žaidė kieme, garsiai _____.<br><br>Дети играли во дворе, громко <u>крича</u>.',
      options: ['šaukdami', 'šaukę', 'šaukdamos', 'šaukusios'],
      correct: 0,
      topic: 'Pusdalyvis dgs.',
      hint: 'Играли и кричали одновременно → pusdalyvis. Vaikai = vyr. g. dgs.',
      explanation: 'šaukdami — pusdalyvis, vyr. g. dgs. Одновременно играли и кричали.',
      ruExplanation: 'Крича (одновременно с игрой). Vaikai — мн.ч. м.р. → šaukdami.'
    },
    {
      type: 'choice',
      question: 'Mokytoja aiškino temą, _____ <strong>(rodyti, одновр.)</strong> paveikslėlius.<br><br>Учительница объясняла тему, <u>показывая</u> картинки.',
      options: ['rodydama', 'rodžiusi', 'rodydamas', 'rodę'],
      correct: 0,
      topic: 'Pusdalyvis mot.',
      hint: 'Объясняла и показывала одновременно → pusdalyvis. Mokytoja = mot. g.',
      explanation: 'rodydama — pusdalyvis, mot. g. Mokytoja = женский род.',
      ruExplanation: 'Показывая (одновременно с объяснением). Подлежащее «mokytoja» → женский род → rodydama.'
    },
    {
      type: 'choice',
      question: '_____ <strong>(nusipirkti, предшеств., vyr.)</strong> bilietą, jis nuėjo į kiną.<br><br><u>Купив</u> билет, он пошёл в кино.',
      options: ['Nusipirkęs', 'Nusipirkdamas', 'Nusipirkusi', 'Nusipirkdama'],
      correct: 0,
      topic: 'Padalyvis',
      hint: 'Сначала купил, потом пошёл → padalyvis. Jis = vyr. g.',
      explanation: 'Nusipirkęs — padalyvis, vyr. g. vns. Последовательные действия.',
      ruExplanation: 'Купив (сначала купил, потом пошёл). Подлежащее «jis» → мужской род → Nusipirkęs.'
    },
    {
      type: 'choice',
      question: 'Senelė mezgė, _____ <strong>(klausytis, одновр.)</strong> radijo.<br><br>Бабушка вязала, <u>слушая</u> радио.',
      options: ['klausydamasi', 'klausydamasis', 'klausiusi', 'klausęsi'],
      correct: 0,
      topic: 'Pusdalyvis (sangrąžinis)',
      hint: 'Вязала и слушала одновременно → pusdalyvis. Senelė = mot. g. Klausytis = возвратный.',
      explanation: 'klausydamasi — pusdalyvis от возвратного глагола klausytis, mot. g.',
      ruExplanation: 'Слушая (одновременно с вязанием). Возвратный глагол klausytis → klausydamasi (ж.р.).'
    },
    {
      type: 'input',
      question: '_____ <strong>(išeiti, предшеств., mot.)</strong> iš namų, ji pamatė kaimynę.<br><br><u>Выйдя</u> из дома, она увидела соседку.<br><br>Įrašykite tinkamą formą:',
      answer: ['Išėjusi'],
      topic: 'Padalyvis mot.',
      hint: 'Сначала вышла, потом увидела → padalyvis. Ji = mot. g.',
      explanation: 'Išėjusi — padalyvis, mot. g. vns. Išeiti → 3 asm. būt.: išėjo → išėj-usi.',
      ruExplanation: 'Выйдя (сначала вышла, потом увидела). Женский род → Išėjusi.'
    },
    {
      type: 'input',
      question: 'Jis skaitė laikraštį, _____ <strong>(gerti, одновр., vyr.)</strong> kavą.<br><br>Он читал газету, <u>попивая</u> кофе.<br><br>Įrašykite tinkamą formą:',
      answer: ['gerdamas'],
      topic: 'Pusdalyvis vyr.',
      hint: 'Одновременные действия → pusdalyvis. Jis = vyr. g.',
      explanation: 'gerdamas — pusdalyvis, vyr. g. Gerti → ger-damas.',
      ruExplanation: 'Попивая (одновременно с чтением). Мужской род → gerdamas.'
    },
    {
      type: 'input',
      question: '_____ <strong>(pamatyti, предшеств., vyr.)</strong> draugą, jis nustebo.<br><br><u>Увидев</u> друга, он удивился.<br><br>Įrašykite tinkamą formą:',
      answer: ['Pamatęs'],
      topic: 'Padalyvis vyr.',
      hint: 'Сначала увидел, потом удивился → padalyvis. Jis = vyr. g.',
      explanation: 'Pamatęs — padalyvis, vyr. g. vns. Pamatyti → pamatė → pamat-ęs.',
      ruExplanation: 'Увидев (сначала увидел, потом удивился). Мужской род → Pamatęs.'
    },
    {
      type: 'input',
      question: 'Mergaitės ėjo per mišką, _____ <strong>(dainuoti, одновр., mot. dgs.)</strong>.<br><br>Девочки шли через лес, <u>напевая</u>.<br><br>Įrašykite tinkamą formą:',
      answer: ['dainuodamos'],
      topic: 'Pusdalyvis mot. dgs.',
      hint: 'Шли и пели одновременно → pusdalyvis. Mergaitės = mot. g. dgs.',
      explanation: 'dainuodamos — pusdalyvis, mot. g. dgs. Dainuoti → dainuo-damos.',
      ruExplanation: 'Напевая (одновременно). Множественное число женского рода → dainuodamos.'
    },
    {
      type: 'input',
      question: '_____ <strong>(išmokti, предшеств., mot.)</strong> lietuvių kalbą, ji rado gerą darbą.<br><br><u>Выучив</u> литовский язык, она нашла хорошую работу.<br><br>Įrašykite tinkamą formą:',
      answer: ['Išmokusi'],
      topic: 'Padalyvis mot.',
      hint: 'Сначала выучила, потом нашла → padalyvis. Ji = mot. g.',
      explanation: 'Išmokusi — padalyvis, mot. g. vns. Išmokti → išmoko → išmok-usi.',
      ruExplanation: 'Выучив (сначала выучила, потом нашла). Женский род → Išmokusi.'
    },
    {
      type: 'input',
      question: 'Jie diskutavo, _____ <strong>(vaikščioti, одновр., vyr. dgs.)</strong> po parką.<br><br>Они дискутировали, <u>прогуливаясь</u> по парку.<br><br>Įrašykite tinkamą formą:',
      answer: ['vaikščiodami'],
      topic: 'Pusdalyvis vyr. dgs.',
      hint: 'Дискутировали и гуляли одновременно → pusdalyvis. Jie = vyr. g. dgs.',
      explanation: 'vaikščiodami — pusdalyvis, vyr. g. dgs. Vaikščioti → vaikščio-dami.',
      ruExplanation: 'Прогуливаясь (одновременно с дискуссией). Множественное число м.р. → vaikščiodami.'
    },
    {
      type: 'input',
      question: '_____ <strong>(pavakarieniavti → pavakarieniavęs, предшеств., vyr.)</strong>, jis atsigulė.<br><br><u>Поужинав</u>, он лёг спать.<br><br>Įrašykite tinkamą formą:',
      answer: ['Pavakarieniavęs'],
      topic: 'Padalyvis vyr.',
      hint: 'Сначала поужинал, потом лёг → padalyvis. Jis = vyr. g.',
      explanation: 'Pavakarieniavęs — padalyvis, vyr. g. vns. Pavakarieniauti → pavakarieniavo → pavakarieniav-ęs.',
      ruExplanation: 'Поужинав (сначала поужинал, потом лёг). Мужской род → Pavakarieniavęs.'
    },
    {
      type: 'input',
      question: '_____ <strong>(atsisėsti, предшеств., mot. dgs.)</strong> prie stalo, moterys pradėjo kalbėtis.<br><br><u>Сев</u> за стол, женщины начали разговаривать.<br><br>Įrašykite tinkamą formą:',
      answer: ['Atsisėdusios'],
      topic: 'Padalyvis mot. dgs.',
      hint: 'Сначала сели, потом начали говорить → padalyvis. Moterys = mot. g. dgs.',
      explanation: 'Atsisėdusios — padalyvis, mot. g. dgs. Atsisėsti → atsisėdo → atsisėd-usios.',
      ruExplanation: 'Сев (сначала сели, потом заговорили). Множественное число женского рода → Atsisėdusios.'
    }
  ];
}


// ═══════════════════════════════════════════════════════════════
// DRILL 6 — Sakinių transformavimas (трансформация предложений)
// 15 exercises: all choice
// ═══════════════════════════════════════════════════════════════

function getDalyviaiDrill6() {
  return [
    {
      type: 'choice',
      question: 'Transformuokite sakinį su dalyviu:<br><br><em>Žmogus, <u>kuris skaito</u> knygą, sėdi parke.</em><br><br>Трансформируйте предложение с причастием:',
      options: [
        'Knygą skaitantis žmogus sėdi parke.',
        'Knygą skaitęs žmogus sėdi parke.',
        'Knygą skaitomas žmogus sėdi parke.',
        'Knygą skaitydamas žmogus sėdi parke.'
      ],
      correct: 0,
      topic: 'Veik. esam.',
      hint: 'kuris skaito (наст. вр., акт.) → veik. esamojo laiko dalyvis: skaitantis.',
      explanation: 'kuris skaito → skaitantis (veik. esam.). Причастие перед существительным: Knygą skaitantis žmogus.',
      ruExplanation: 'Который читает → читающий = skaitantis. Действительное причастие настоящего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Draugas, <u>kuris parašė</u> laišką, išvyko.</em><br><br>Друг, который написал письмо, уехал.',
      options: [
        'Laišką parašęs draugas išvyko.',
        'Laišką parašantis draugas išvyko.',
        'Laišką parašytas draugas išvyko.',
        'Laišką parašydamas draugas išvyko.'
      ],
      correct: 0,
      topic: 'Veik. būt. kart.',
      hint: 'kuris parašė (прош. вр., акт.) → veik. būtojo kartinio laiko dalyvis: parašęs.',
      explanation: 'kuris parašė → parašęs (veik. būt. kart.). Написавший друг уехал.',
      ruExplanation: 'Который написал → написавший = parašęs. Действительное причастие прошедшего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Namas, <u>kurį stato</u> darbininkai, yra didelis.</em><br><br>Дом, который строят рабочие, большой.',
      options: [
        'Darbininkų statomas namas yra didelis.',
        'Darbininkų statęs namas yra didelis.',
        'Darbininkų statytas namas yra didelis.',
        'Darbininkų statantis namas yra didelis.'
      ],
      correct: 0,
      topic: 'Neveik. esam.',
      hint: 'kurį stato (наст. вр., пассив) → neveik. esamojo laiko dalyvis: statomas. Автор → K.: darbininkų.',
      explanation: 'kurį stato → statomas (neveik. esam.). Автор действия в kilmininkas: darbininkų.',
      ruExplanation: 'Который строят → строящийся/строимый = statomas. Страдательное причастие настоящего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Laiškas, <u>kurį parašė</u> draugas, buvo ilgas.</em><br><br>Письмо, которое написал друг, было длинным.',
      options: [
        'Draugo parašytas laiškas buvo ilgas.',
        'Draugo parašantis laiškas buvo ilgas.',
        'Draugo parašomas laiškas buvo ilgas.',
        'Draugo rašęs laiškas buvo ilgas.'
      ],
      correct: 0,
      topic: 'Neveik. būt.',
      hint: 'kurį parašė (прош. вр., пассив) → neveik. būtojo laiko dalyvis: parašytas. Draugas → K.: draugo.',
      explanation: 'kurį parašė → parašytas (neveik. būt.). Автор в kilmininkas: draugo.',
      ruExplanation: 'Которое написал → написанное = parašytas. Страдательное причастие прошедшего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Moterys, <u>kurios dirba</u> ligoninėje, yra patyrusios.</em><br><br>Женщины, которые работают в больнице, опытные.',
      options: [
        'Ligoninėje dirbančios moterys yra patyrusios.',
        'Ligoninėje dirbusios moterys yra patyrusios.',
        'Ligoninėje dirbamos moterys yra patyrusios.',
        'Ligoninėje dirbdamos moterys yra patyrusios.'
      ],
      correct: 0,
      topic: 'Veik. esam. dgs.',
      hint: 'kurios dirba (наст. вр., акт., мн.ч. ж.р.) → dirbančios.',
      explanation: 'kurios dirba → dirbančios (veik. esam. mot. g. dgs.).',
      ruExplanation: 'Которые работают → работающие (ж.р. мн.ч.) = dirbančios.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Studentas, <u>kuris studijuos</u> Vilniuje, gavo stipendiją.</em><br><br>Студент, который будет учиться в Вильнюсе, получил стипендию.',
      options: [
        'Vilniuje studijuosiantis studentas gavo stipendiją.',
        'Vilniuje studijuojantis studentas gavo stipendiją.',
        'Vilniuje studijuosimas studentas gavo stipendiją.',
        'Vilniuje studijuodamas studentas gavo stipendiją.'
      ],
      correct: 0,
      topic: 'Veik. būsim.',
      hint: 'kuris studijuos (буд. вр., акт.) → veik. būsimojo laiko dalyvis: studijuosiantis.',
      explanation: 'kuris studijuos → studijuosiantis (veik. būsim.).',
      ruExplanation: 'Который будет учиться → тот, кто будет учиться = studijuosiantis. Действительное причастие будущего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Daina, <u>kurią dainuoja</u> choras, yra graži.</em><br><br>Песня, которую поёт хор, красивая.',
      options: [
        'Choro dainuojama daina yra graži.',
        'Choro dainuojanti daina yra graži.',
        'Choro dainuota daina yra graži.',
        'Choro dainuodama daina yra graži.'
      ],
      correct: 0,
      topic: 'Neveik. esam.',
      hint: 'kurią dainuoja (наст. вр., пассив) → neveik. esam.: dainuojama. Choras → K.: choro.',
      explanation: 'kurią dainuoja → dainuojama (neveik. esam. mot. g.). Choro = автор в kilmininkas.',
      ruExplanation: 'Которую поёт → поющаяся/исполняемая = dainuojama. Хор в родительном: choro.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Vaikas, <u>kuris bėgo</u> per kiemą, pargriuvo.</em><br><br>Ребёнок, который бежал по двору, упал.',
      options: [
        'Per kiemą bėgęs vaikas pargriuvo.',
        'Per kiemą bėgantis vaikas pargriuvo.',
        'Per kiemą bėgdamas vaikas pargriuvo.',
        'Per kiemą bėgtas vaikas pargriuvo.'
      ],
      correct: 0,
      topic: 'Veik. būt. kart.',
      hint: 'kuris bėgo (прош. вр., акт.) → veik. būtojo kartinio laiko dalyvis: bėgęs.',
      explanation: 'kuris bėgo → bėgęs (veik. būt. kart.). Бежавший ребёнок упал.',
      ruExplanation: 'Который бежал → бежавший = bėgęs. Действительное причастие прошедшего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Filmas, <u>kurį režisavo</u> žymus režisierius, laimėjo prizą.</em><br><br>Фильм, который режиссировал известный режиссёр, выиграл приз.',
      options: [
        'Žymaus režisieriaus režisuotas filmas laimėjo prizą.',
        'Žymaus režisieriaus režisuojamas filmas laimėjo prizą.',
        'Žymaus režisieriaus režisuojantis filmas laimėjo prizą.',
        'Žymaus režisieriaus režisuodamas filmas laimėjo prizą.'
      ],
      correct: 0,
      topic: 'Neveik. būt.',
      hint: 'kurį režisavo (прош. вр., пассив) → neveik. būt.: režisuotas. Režisierius → K.: režisieriaus.',
      explanation: 'kurį režisavo → režisuotas (neveik. būt.). Žymus → žymaus (K.).',
      ruExplanation: 'Который режиссировал → снятый/режиссированный = režisuotas. Режиссёр в родительном: režisieriaus.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Matau žmogų, <u>kuris bėga</u> parke.</em><br><br>Вижу человека, который бежит в парке.',
      options: [
        'Matau parke bėgantį žmogų.',
        'Matau parke bėgantis žmogų.',
        'Matau parke bėgusį žmogų.',
        'Matau parke bėgamą žmogų.'
      ],
      correct: 0,
      topic: 'Veik. esam. + G.',
      hint: 'kuris bėga → bėgantis, но žmogų — galininkas! Bėgantis → bėgantį.',
      explanation: 'Žmogų стоит в galininkas → причастие тоже: bėgantį.',
      ruExplanation: 'Вижу КОГО? → бегущего = bėgantį. Причастие согласуется с существительным в падеже.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Knyga, <u>kurią skaitys</u> studentai, yra įdomi.</em><br><br>Книга, которую будут читать студенты, интересная.',
      options: [
        'Studentų skaitysima knyga yra įdomi.',
        'Studentų skaitoma knyga yra įdomi.',
        'Studentų skaityta knyga yra įdomi.',
        'Studentų skaičiusiama knyga yra įdomi.'
      ],
      correct: 0,
      topic: 'Neveik. būsim.',
      hint: 'kurią skaitys (буд. вр., пассив) → neveik. būsimojo laiko dalyvis: skaitysima.',
      explanation: 'kurią skaitys → skaitysima (neveik. būsim. mot. g.). Studentai → K.: studentų.',
      ruExplanation: 'Которую будут читать → та, что будет читаться = skaitysima. Страдательное причастие будущего времени.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Vaikai, <u>kurie grojo</u> koncerte, buvo talentingi.</em><br><br>Дети, которые играли на концерте, были талантливы.',
      options: [
        'Koncerte groję vaikai buvo talentingi.',
        'Koncerte grojantys vaikai buvo talentingi.',
        'Koncerte grojami vaikai buvo talentingi.',
        'Koncerte grodami vaikai buvo talentingi.'
      ],
      correct: 0,
      topic: 'Veik. būt. kart. dgs.',
      hint: 'kurie grojo (прош. вр., акт., мн.ч.) → veik. būt. kart. dgs.: groję.',
      explanation: 'kurie grojo → groję (veik. būt. kart. vyr. g. dgs.).',
      ruExplanation: 'Которые играли → игравшие = groję. Действительное причастие прошедшего времени, мн.ч.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Moteris, <u>kuri gyveno</u> Kaune, persikėlė į Vilnių.</em><br><br>Женщина, которая жила в Каунасе, переехала в Вильнюс.',
      options: [
        'Kaune gyvenusi moteris persikėlė į Vilnių.',
        'Kaune gyvenanti moteris persikėlė į Vilnių.',
        'Kaune gyvendama moteris persikėlė į Vilnių.',
        'Kaune gyvenama moteris persikėlė į Vilnių.'
      ],
      correct: 0,
      topic: 'Veik. būt. kart. mot.',
      hint: 'kuri gyveno (прош. вр., акт., ж.р.) → veik. būt. kart.: gyvenusi.',
      explanation: 'kuri gyveno → gyvenusi (veik. būt. kart. mot. g. vns.).',
      ruExplanation: 'Которая жила → жившая = gyvenusi. Действительное причастие прошедшего времени, ж.р.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Kalbėjau su žmogumi, <u>kuris dirba</u> banke.</em><br><br>Разговаривал с человеком, который работает в банке.',
      options: [
        'Kalbėjau su banke dirbančiu žmogumi.',
        'Kalbėjau su banke dirbantis žmogumi.',
        'Kalbėjau su banke dirbamu žmogumi.',
        'Kalbėjau su banke dirbusiu žmogumi.'
      ],
      correct: 0,
      topic: 'Veik. esam. + Įn.',
      hint: 'kuris dirba → dirbantis, но žmogumi — Įnagininkas! Dirbantis → dirbančiu.',
      explanation: 'Su žmogumi = Įnagininkas → dirbančiu (veik. esam. vyr. g. Įn.).',
      ruExplanation: 'С работающим человеком = su dirbančiu žmogumi. Причастие согласуется в творительном падеже.'
    },
    {
      type: 'choice',
      question: 'Transformuokite:<br><br><em>Tai yra tiltas, <u>kurį pastatė</u> inžinieriai.</em><br><br>Это мост, который построили инженеры.',
      options: [
        'Tai yra inžinierių pastatytas tiltas.',
        'Tai yra inžinierių pastatantis tiltas.',
        'Tai yra inžinierių pastatomas tiltas.',
        'Tai yra inžinierių pastatydamas tiltas.'
      ],
      correct: 0,
      topic: 'Neveik. būt.',
      hint: 'kurį pastatė (прош. вр., пассив) → neveik. būt.: pastatytas. Inžinieriai → K.: inžinierių.',
      explanation: 'kurį pastatė → pastatytas (neveik. būt.). Inžinierių = автор в kilmininkas.',
      ruExplanation: 'Который построили → построенный = pastatytas. Инженеры в родительном: inžinierių.'
    }
  ];
}


// ═══════════════════════════════════════════════════════════════
// DRILL 7 — Visų tipų dalyviai (смешанный)
// 20 exercises: 10 choice + 7 input + 2 multi-input + 1 choice ("select")
// ═══════════════════════════════════════════════════════════════

function getDalyviaiDrill7() {
  return [
    {
      type: 'choice',
      question: 'Nurodykite dalyvio tipą:<br><br><em>Mieste <strong>gyvenantys</strong> žmonės dažniau naudojasi viešuoju transportu.</em><br><br>Определите тип причастия <strong>gyvenantys</strong>:',
      options: [
        'Veikiamasis esamojo laiko dalyvis',
        'Veikiamasis būtojo kartinio laiko dalyvis',
        'Neveikiamasis esamojo laiko dalyvis',
        'Pusdalyvis'
      ],
      correct: 0,
      topic: 'Dalyvio tipas',
      hint: 'gyvenantys — от gyventi. Суффикс -ant- → esamojo laiko.',
      explanation: 'gyvenantys — veikiamasis esamojo laiko dalyvis, vyr. g. dgs. (живущие).',
      ruExplanation: 'Живущие — действительное причастие настоящего времени. Суффикс -ant- указывает на настоящее время активного залога.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą dalyvį:<br><br><em>Mokslininkai tyrinėja neseniai _____ augalų rūšį.</em><br><br>Учёные исследуют недавно <u>обнаруженный</u> вид растений.',
      options: ['atrastą', 'atrandančią', 'atradusią', 'atrandamą'],
      correct: 0,
      topic: 'Neveik. būt. + G.',
      hint: 'Вид был обнаружен (пассив, прош. вр.) → neveik. būt. Rūšį = galininkas mot. g.',
      explanation: 'atrastą — neveikiamasis būtojo laiko dalyvis, mot. g. G. (atrasta → atrastą).',
      ruExplanation: 'Обнаруженный вид → страдательное причастие прошедшего времени. Rūšį (G. mot.) → atrastą.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>Vakar _____ koncertas buvo labai įspūdingas.</em><br><br>Вчера <u>состоявшийся</u> концерт был очень впечатляющим.',
      options: ['vykęs', 'vykstantis', 'vykdamas', 'vyksiantis'],
      correct: 0,
      topic: 'Veik. būt. kart.',
      hint: 'Vakar = вчера → прошедшее время. Концерт сам происходил (акт.) → veik. būt. kart.',
      explanation: 'vykęs — veikiamasis būtojo kartinio laiko dalyvis (vykti → vyko → vyk-ęs).',
      ruExplanation: 'Вчера состоявшийся → прошедшее время, активный залог = vykęs.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>Artėjantis egzaminas kelia _____ studentams stresą.</em><br><br>Приближающийся экзамен вызывает стресс у <u>готовящихся</u> студентов.',
      options: ['besiruošiantiems', 'besiruošiantys', 'besiruošiančių', 'besiruošiančiais'],
      correct: 0,
      topic: 'Veik. esam. + N.',
      hint: 'Kelia stresą KAM? → Naudininkas. Studentams = N. dgs. → besiruošiantiems.',
      explanation: 'besiruošiantiems — veik. esam. laiko dalyvis, vyr. g. dgs. naudininkas.',
      ruExplanation: 'Вызывает стресс КОМУ? → готовящимся студентам = besiruošiantiems (дательный мн.ч.).'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>Ši knyga, _____ prieš šimtą metų, vis dar aktuali.</em><br><br>Эта книга, <u>написанная</u> сто лет назад, всё ещё актуальна.',
      options: ['parašyta', 'parašiusi', 'rašanti', 'rašoma'],
      correct: 0,
      topic: 'Neveik. būt.',
      hint: 'Книга была написана (пассив, прош. вр.) → neveik. būt.: parašyta.',
      explanation: 'parašyta — neveikiamasis būtojo laiko dalyvis, mot. g. (knyga = mot. g.).',
      ruExplanation: 'Книга написана → страдательное причастие прошедшего времени. Книга (ж.р.) → parašyta.'
    },
    {
      type: 'choice',
      question: 'Nurodykite dalyvio tipą:<br><br><em>Jis kalbėjo <strong>šypsodamasis</strong>.</em><br><br>Определите тип: <strong>šypsodamasis</strong>.',
      options: [
        'Pusdalyvis (sangrąžinis)',
        'Padalyvis',
        'Veikiamasis esamojo laiko dalyvis',
        'Neveikiamasis esamojo laiko dalyvis'
      ],
      correct: 0,
      topic: 'Dalyvio tipas',
      hint: 'Суффикс -dama- + возвратное -si- → pusdalyvis от šypsotis.',
      explanation: 'šypsodamasis — pusdalyvis от возвратного глагола šypsotis (улыбаться). Одновременное действие.',
      ruExplanation: 'Улыбаясь — полупричастие (pusdalyvis) от возвратного глагола šypsotis. Суффикс -dama- + -si.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>_____ laišką, jis jį išsiuntė.</em><br><br><u>Написав</u> письмо, он его отправил.',
      options: ['Parašęs', 'Rašydamas', 'Parašytas', 'Rašantis'],
      correct: 0,
      topic: 'Padalyvis',
      hint: 'Сначала написал, потом отправил → padalyvis. Jis = vyr. g.',
      explanation: 'Parašęs — padalyvis, vyr. g. Последовательные действия: написал → отправил.',
      ruExplanation: 'Написав (предшествующее действие) → padalyvis. Мужской род → Parašęs.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>Tai yra rytoj _____ susitikimas.</em><br><br>Это завтра <u>состоящееся</u> собрание.',
      options: ['vyksiantis', 'vykstantis', 'vykęs', 'vykdomas'],
      correct: 0,
      topic: 'Veik. būsim.',
      hint: 'Rytoj = завтра → будущее время. Собрание состоится (акт.) → veik. būsim.',
      explanation: 'vyksiantis — veikiamasis būsimojo laiko dalyvis (vykti → vyks → vyksiantis).',
      ruExplanation: 'Завтра состоящееся → будущее время, активный залог = vyksiantis.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>Šis projektas bus _____ kitą savaitę.</em><br><br>Этот проект будет <u>завершён</u> на следующей неделе.',
      options: ['užbaigtas', 'užbaigiantis', 'užbaigdamas', 'užbaigsiantis'],
      correct: 0,
      topic: 'Neveik. būt.',
      hint: 'Проект будет завершён (пассив) → neveik. būt.: užbaigtas. Bus + dalyvis.',
      explanation: 'užbaigtas — neveikiamasis būtojo laiko dalyvis. Bus užbaigtas = будет завершён.',
      ruExplanation: 'Будет завершён → страдательное причастие прошедшего времени (в конструкции с bus). Užbaigtas.'
    },
    {
      type: 'choice',
      question: 'Pasirinkite tinkamą formą:<br><br><em>Visų _____ filmas pelnė „Oskarą".</em><br><br>Всеми <u>любимый</u> фильм получил «Оскар».',
      options: ['mylimas', 'mylintis', 'mylėjęs', 'mylėtas'],
      correct: 0,
      topic: 'Neveik. esam.',
      hint: 'Фильм любим (сейчас, пассив) → neveik. esam.: mylimas.',
      explanation: 'mylimas — neveikiamasis esamojo laiko dalyvis. Visų mylimas = всеми любимый.',
      ruExplanation: 'Любимый всеми → страдательное причастие настоящего времени = mylimas.'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą dalyvio formą:<br><br><em>Mes matėme gatvėje _____ (vaikščioti, veik. esam., mot. G.) moterį.</em><br><br>Мы видели на улице <u>гуляющую</u> женщину.',
      answer: ['vaikščiojančią', 'vaikščiojančia'],
      topic: 'Veik. esam. + G.',
      hint: 'Matėme KĄ? → Galininkas. Vaikščiojanti → vaikščiojančią (mot. g. G.).',
      explanation: 'vaikščiojančią — veik. esam. laiko dalyvis, mot. g. vns. galininkas.',
      ruExplanation: 'Видели КОГО? → гуляющую = vaikščiojančią. Причастие в винительном падеже женского рода.'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą formą:<br><br><em>Ji ėjo gatve, _____ (žiūrėti, pusdalyvis, mot.) į vitrinas.</em><br><br>Она шла по улице, <u>разглядывая</u> витрины.',
      answer: ['žiūrėdama'],
      topic: 'Pusdalyvis',
      hint: 'Одновременные действия → pusdalyvis. Ji = mot. g.',
      explanation: 'žiūrėdama — pusdalyvis, mot. g. Žiūrėti → žiūrė-dama.',
      ruExplanation: 'Разглядывая (одновременно) → полупричастие. Женский род → žiūrėdama.'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą formą:<br><br><em>Tai yra profesoriaus _____ (parašyti, neveik. būt., mot. V.) monografija.</em><br><br>Это <u>написанная</u> профессором монография.',
      answer: ['parašyta'],
      topic: 'Neveik. būt.',
      hint: 'Монография была написана (пассив, прош.) → neveik. būt. Monografija = mot. g. V.',
      explanation: 'parašyta — neveikiamasis būtojo laiko dalyvis, mot. g. vardininkas.',
      ruExplanation: 'Написанная профессором → страдательное причастие прошедшего времени, ж.р. = parašyta.'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą formą:<br><br><em>_____ (sužinoti, padalyvis, vyr.) naujieną, jis labai apsidžiaugė.</em><br><br><u>Узнав</u> новость, он очень обрадовался.',
      answer: ['Sužinojęs'],
      topic: 'Padalyvis',
      hint: 'Сначала узнал, потом обрадовался → padalyvis. Jis = vyr. g.',
      explanation: 'Sužinojęs — padalyvis, vyr. g. Sužinoti → sužinojo → sužinoj-ęs.',
      ruExplanation: 'Узнав (сначала узнал) → деепричастие предшествования, м.р. = Sužinojęs.'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą formą:<br><br><em>Vaikai klausėsi senelės _____ (pasakoti, neveik. esam., mot. K.) pasakos.</em><br><br>Дети слушали <u>рассказываемую</u> бабушкой сказку.',
      answer: ['pasakojamos'],
      topic: 'Neveik. esam. + K.',
      hint: 'Pasakos KO? → Kilmininkas. Pasakojama → pasakojamos (mot. g. K.).',
      explanation: 'pasakojamos — neveik. esam. laiko dalyvis, mot. g. kilmininkas.',
      ruExplanation: 'Слушали ЧЕГО? → рассказываемой сказки = pasakojamos (родительный ж.р.).'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą formą:<br><br><em>Mes lankėme _____ (sirgti, veik. esam., vyr. G.) draugą.</em><br><br>Мы навещали <u>болеющего</u> друга.',
      answer: ['sergantį'],
      topic: 'Veik. esam. + G.',
      hint: 'Lankėme KĄ? → Galininkas. Sergantis → sergantį (vyr. g. G.).',
      explanation: 'sergantį — veik. esam. laiko dalyvis, vyr. g. galininkas.',
      ruExplanation: 'Навещали КОГО? → болеющего друга = sergantį (винительный м.р.).'
    },
    {
      type: 'input',
      question: 'Parašykite tinkamą formą:<br><br><em>_____ (apsirengti, padalyvis, mot. dgs.) paltais, merginos išėjo į lauką.</em><br><br><u>Надев</u> пальто, девушки вышли на улицу.',
      answer: ['Apsirengusios'],
      topic: 'Padalyvis mot. dgs.',
      hint: 'Сначала оделись, потом вышли → padalyvis. Merginos = mot. g. dgs.',
      explanation: 'Apsirengusios — padalyvis, mot. g. dgs. Apsirengti → apsirenk-usios.',
      ruExplanation: 'Надев (сначала оделись) → деепричастие предшествования, ж.р. мн.ч. = Apsirengusios.'
    },
    {
      type: 'multi-input',
      question: 'Užpildykite abi spragas tinkamomis dalyvių formomis:<br><br><em>"<strong>(1)</strong> _____ (parašyti, padalyvis, vyr.) laišką ir <strong>(2)</strong> _____ (įdėti, padalyvis, vyr.) jį į voką, jis nuėjo į paštą."</em><br><br><u>Написав</u> письмо и <u>вложив</u> его в конверт, он пошёл на почту.',
      topic: 'Padalyvis (du veiksmažodžiai)',
      blanks: [
        { num: 1, answer: ['Parašęs'] },
        { num: 2, answer: ['įdėjęs'] }
      ],
      hint: 'Оба действия предшествуют походу на почту → padalyvis. Jis = vyr. g.',
      explanation: 'Parašęs (parašyti → parašė → paraš-ęs) и įdėjęs (įdėti → įdėjo → įdėj-ęs) — оба padalyvis, vyr. g.',
      ruExplanation: 'Написав и вложив — два последовательных предшествующих действия. Оба в форме padalyvis мужского рода.'
    },
    {
      type: 'multi-input',
      question: 'Užpildykite abi spragas:<br><br><em>"Gatvėje buvo daug <strong>(1)</strong> _____ (skubėti, veik. esam., dgs. K.) žmonių ir <strong>(2)</strong> _____ (statyti, neveik. esam., dgs. K.) pastatų."</em><br><br>На улице было много <u>спешащих</u> людей и <u>строящихся</u> зданий.',
      topic: 'Veik. + neveik. esam.',
      blanks: [
        { num: 1, answer: ['skubančių'] },
        { num: 2, answer: ['statomų'] }
      ],
      hint: 'Daug KO? → Kilmininkas dgs. Люди спешат (акт.) → skubančių. Здания строятся (пассив) → statomų.',
      explanation: '(1) skubančių — veik. esam. dgs. K. (2) statomų — neveik. esam. dgs. K.',
      ruExplanation: 'Много КОГО/ЧЕГО? → родительный мн.ч. Спешащих = skubančių (акт.). Строящихся = statomų (пассив).'
    },
    {
      type: 'choice',
      question: 'Kuris sakinys yra <strong>teisingas</strong> (грамматически правильный)?<br><br>Какое предложение грамматически правильное?',
      options: [
        'Grįžusi namo, ji paruošė vakarienę.',
        'Grįždama namo, ji paruošė vakarienę.',
        'Grįžęs namo, ji paruošė vakarienę.',
        'Grįždamas namo, ji paruošė vakarienę.'
      ],
      correct: 0,
      topic: 'Padalyvis vs pusdalyvis',
      hint: 'Сначала вернулась, потом приготовила → padalyvis. Ji = mot. g. → -usi.',
      explanation: 'Grįžusi — padalyvis, mot. g. Последовательные действия. Вариант B неверен: нельзя идти домой и готовить одновременно. Варианты C и D — мужской род при подлежащем ji.',
      ruExplanation: 'Вернувшись домой, она приготовила ужин. Padalyvis (предшествование) + женский род = Grįžusi.'
    }
  ];
}
