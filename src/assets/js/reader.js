// Neoscholia — страница чтения (тип reader): то, чего нет в общем site.js. Стили — assets/css/layouts/reader.css.
//
//   Введение     <section data-fold="Подпись кнопки"> с блоком .fold: длинный текст свёрнут, кнопка раскрывает его.
//   Примечания   Поле .margin обрезано по высоте колонки текста. Где примечания не поместились, появляется кнопка
//                «Все примечания (N)»; она раскрывает сегмент. Переход к примечанию (значок в тексте, ссылка из
//                указателя, поиск по странице) раскрывает его сегмент сам.
//   Переход      <select data-jump> показывает главу, которая сейчас на экране.
//   Озвучка      <button class="listen" data-src data-fallback>: один проигрыватель на страницу.
(function () {
  var root = document.documentElement;
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function lang() { return root.dataset.tr === 'en' ? 'en' : 'ru'; }
  function button(cls) { var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--sm ' + cls; return b; }
  // прокрутка к элементу; instant — без плавного хода: там, где место на странице только что сдвинулось
  function show(el, instant) { try { el.scrollIntoView(instant ? { behavior: 'instant' } : undefined); } catch (e) { el.scrollIntoView(); } }
  // после сворачивания возвращает начало блока на экран, если оно ушло вверх, под панель чтения
  function backTo(el) { if (el.getBoundingClientRect().top < 60) show(el, true); }

  // ----- введение: свёрнуто, пока читатель не раскроет -----
  var folds = $$('[data-fold]').map(function (box) {
    var x = { box: box, body: box.querySelector('.fold'), btn: button('fold-more'), open: false };
    x.btn.addEventListener('click', function () { setFold(x, !x.open); if (!x.open) backTo(box); });
    return x;
  }).filter(function (x) { return x.body; });
  function setFold(x, open) {
    x.open = open;
    x.box.classList.toggle('is-open', open);
    x.btn.setAttribute('aria-expanded', String(open));
    x.btn.textContent = open ? 'Свернуть' : x.box.dataset.fold;
  }
  // короткому введению кнопка не нужна: оно показано целиком
  function fitFolds() {
    folds.forEach(function (x) {
      if (x.open) return;
      x.box.classList.remove('is-open', 'is-folded');
      var folded = x.body.scrollHeight - x.body.clientHeight > 96;
      if (folded && !x.btn.parentNode) x.box.appendChild(x.btn);
      x.btn.hidden = !folded;
      x.box.classList.toggle('is-folded', folded);
      if (folded) setFold(x, false); else x.box.classList.add('is-open');
    });
  }

  // ----- новые схолии: поле не растягивает сегмент -----
  var segs = $$('.seg').map(function (el) { return { el: el, margin: el.querySelector('.margin'), btn: null, open: false }; })
    .filter(function (x) { return x.margin; });
  function segOf(el) { return segs.filter(function (x) { return x.el === el; })[0]; }
  function setOpen(x, open) {
    x.open = open;
    x.el.classList.toggle('is-open', open);
    if (!x.btn) { x.btn = button('notes-more'); x.margin.appendChild(x.btn); }
    x.btn.setAttribute('aria-expanded', String(open));
    x.btn.textContent = open ? 'Свернуть' : 'Все примечания (' + x.margin.querySelectorAll('.note[data-lang="' + lang() + '"]').length + ')';
  }
  // Сначала все поля возвращаются в обрезанное состояние и измеряются разом, потом расставляются кнопки:
  // чтение размеров и правки разметки не перемежаются, иначе длинная страница пересчитывается на каждом сегменте.
  // Небольшой излишек (до трёх-четырёх строк) кнопки не стоит: такой сегмент просто становится выше.
  function fitNotes() {
    segs.forEach(function (x) { x.el.classList.remove('is-open', 'is-clipped'); });
    var size = segs.map(function (x) { return { over: x.margin.scrollHeight - x.margin.clientHeight, top: x.margin.scrollTop }; });
    segs.forEach(function (x, i) {
      var clipped = size[i].over > 72;
      x.el.classList.toggle('is-clipped', clipped);
      if (clipped) setOpen(x, x.open);
      else { x.open = false; x.el.classList.toggle('is-open', size[i].over > 0); }
      if (x.btn) x.btn.hidden = !clipped;
    });
    segs.forEach(function (x, i) { if (size[i].top) x.margin.scrollTop = 0; });
  }
  // Перемер не уводит страницу с места чтения: блок текста под панелью чтения остаётся там, где был.
  // Переключатели режима меняют высоты ещё до события neoscholia:reader, поэтому место запоминается по нажатию на них.
  // Запоминаются несколько блоков сверху вниз и их сегмент: верхний может оказаться тем самым, что переключатель скроет.
  var kept = null, arriving = false;
  function places() {
    var x = document.querySelector('main').getBoundingClientRect().left + 24, list = [], last = null;
    for (var y = 70; y < window.innerHeight && list.length < 6; y += 40) {
      var hit = document.elementFromPoint(x, y);
      var el = hit && hit.closest('.note, .orig-text, .tr-text, .part-label, .seg-head, .intro');
      if (el && el !== last) { list.push({ el: el, top: el.getBoundingClientRect().top }); last = el; }
    }
    var seg = list.length && list[0].el.closest('.seg');
    if (seg) list.push({ el: seg, top: seg.getBoundingClientRect().top });
    return list;
  }
  function place() { return places()[0] || null; }
  // Запомненный блок, если он остался на странице. Оригинал или перевод, скрытый переключателем, заменяет
  // соседний текст той же части: он встаёт на место скрытого.
  function alive(c) {
    if (c.el.getClientRects().length) return c;
    var part = c.el.closest('.part'), tr = c.el.classList.contains('tr-text');
    if (!part || !(tr || c.el.classList.contains('orig-text'))) return null;
    var twin = $$('.tr-text', part).concat(tr ? $$('.orig-text', part) : []).filter(function (e) { return e.getClientRects().length; })[0];
    return twin ? { el: twin, top: c.top } : null;
  }
  // Сначала блоки, начало которых было на экране: блок, начавшийся выше, меняет высоту и сдвинул бы текст под собой.
  function still(list) {
    var found = null, i;
    for (i = 0; i < list.length && !found; i++) if (list[i].top >= 50) found = alive(list[i]);
    for (i = 0; i < list.length && !found; i++) found = alive(list[i]);
    return found;
  }
  function keep(at) {
    if (!at || !at.el.getClientRects().length) return;
    var by = at.el.getBoundingClientRect().top - at.top;
    if (Math.abs(by) > 1) try { window.scrollBy({ top: by, behavior: 'instant' }); } catch (e) { window.scrollBy(0, by); }
  }
  function fit() {
    // страница только что открыта по ссылке с якорем: после перемера переход к якорю повторяется, без плавного хода
    if (arriving) { kept = null; fitFolds(); fitNotes(); toHash(true); return; }
    var at = still(kept || places());
    kept = null;
    fitFolds(); fitNotes();
    keep(at);
  }
  ['click', 'change'].forEach(function (type) {
    document.addEventListener(type, function (e) {
      if (!e.target.closest || !e.target.closest('[data-pref]')) return;
      kept = places();
      setTimeout(function () { kept = null; }, 0);
    }, true);
  });

  document.addEventListener('click', function (e) {
    var b = e.target.closest('.notes-more');
    if (b) { var x = segOf(b.closest('.seg')); setOpen(x, !x.open); if (!x.open) backTo(x.el); return; }
    // ссылка на примечание: сначала раскрыть его сегмент, потом перейти
    var a = e.target.closest('a[href^="#"]'); if (!a) return;
    var t = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    if (!t || !t.closest('.margin')) return;
    var note = reveal(t);
    if (note !== t) { e.preventDefault(); location.hash = '#' + note.id; }
  });

  // Показывает примечание: включает поле, если оно выключено, берёт пару на выбранном языке, раскрывает сегмент.
  function reveal(el) {
    var note = el.closest('.note'); if (!note) return el;
    var box = document.querySelector('input[data-pref="notes"]');
    if (root.dataset.notes === 'off' && box) { box.checked = true; box.dispatchEvent(new Event('change')); }
    if (note.dataset.lang !== lang()) note = document.getElementById(lang() === 'en' ? note.id + '-en' : note.id.replace(/-en$/, '')) || note;
    var x = segOf(note.closest('.seg'));
    if (x && x.el.classList.contains('is-clipped') && !x.open) setOpen(x, true);
    return note;
  }
  // Переход к якорю из адреса. К главе браузер приходит сам; примечание сначала нужно показать.
  function toHash(instant, notesOnly) {
    var t = location.hash.length > 1 && document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!t) return;
    if (t.closest('.margin')) {
      var note = reveal(t);
      if (note !== t) { location.replace('#' + note.id); return; }
    } else if (notesOnly) return;
    show(t, instant);
  }
  window.addEventListener('hashchange', function () { toHash(arriving, true); });

  // Браузер сам прокручивает обрезанный блок, когда в его скрытой части оказывается найденное слово или фокус:
  // вместо прокрутки блок раскрывается.
  document.addEventListener('scroll', function (e) {
    var m = e.target; if (m.nodeType !== 1 || !m.scrollTop) return;
    var by = m.scrollTop, x;
    if (m.classList.contains('margin') && (x = segOf(m.parentNode))) { m.scrollTop = 0; x.el.classList.add('is-clipped'); setOpen(x, true); x.btn.hidden = false; }
    else if (m.classList.contains('fold') && (x = folds.filter(function (f) { return f.body === m; })[0])) { m.scrollTop = 0; setFold(x, true); }
    else return;
    // то, ради чего браузер прокручивал блок, остаётся на экране: элемент с фокусом или найденное слово
    var f = document.activeElement;
    if (f && m.contains(f)) f.scrollIntoView({ block: 'nearest' });
    else try { window.scrollBy({ top: by, behavior: 'instant' }); } catch (err) { window.scrollBy(0, by); }
  }, true);

  // размеры меняются: смена языка, показа и поля (событие из site.js), раскрытие журнала, ширина окна, загрузка шрифтов
  var timer = 0, width = window.innerWidth;
  function later() { clearTimeout(timer); timer = setTimeout(fit, 150); }
  document.addEventListener('neoscholia:reader', fit);
  document.addEventListener('toggle', later, true);
  window.addEventListener('resize', function () { if (window.innerWidth !== width) { width = window.innerWidth; later(); } });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(later);

  // Страница открыта по ссылке с якорем: высоты выше по странице меняются (перемер, загрузка шрифтов), поэтому переход
  // к якорю повторяется после каждого перемера (arriving), пока читатель не начал прокручивать или нажимать сам.
  // При перезагрузке и возврате по истории браузер восстанавливает прежнее место сам: там примечание из адреса
  // только раскрывается, без прокрутки.
  var nav = window.performance && performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  arriving = (!nav || nav.type === 'navigate') && location.hash.length > 1;
  if (arriving) {
    var settle = function () { arriving = false; };
    ['wheel', 'touchmove', 'keydown', 'pointerdown'].forEach(function (type) { window.addEventListener(type, settle, { capture: true, passive: true, once: true }); });
    setTimeout(settle, 4000);
  }
  fit();
  if (nav && nav.type !== 'navigate') {
    var t0 = location.hash.length > 1 && document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (t0 && t0.closest('.margin')) {
      // если само примечание стояло на экране, оно остаётся на месте; иначе на месте остаётся блок под панелью
      var r0 = t0.getBoundingClientRect();
      var at0 = r0.height && r0.top >= 0 && r0.top < window.innerHeight ? { el: t0, top: r0.top } : place();
      reveal(t0); keep(at0);
    }
  }

  // ----- переход: в списке показана глава, которая сейчас на экране -----
  var jump = document.querySelector('select[data-jump]');
  if (jump && 'IntersectionObserver' in window) {
    var quiet = 0, here = {}, above = $$('.page-head, .intro, .verses');
    $$('option', jump).forEach(function (o) { if (o.value.charAt(0) === '#') here[o.value.slice(1)] = o.value; });
    // пока страница едет к выбранной главе, список не трогаем
    jump.addEventListener('change', function () { quiet = Date.now() + 1500; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        // шапка и вводная панель стоят выше текста: там список показывает свой первый пункт
        var value = here[e.target.id] || (above.indexOf(e.target) > -1 && jump.options[0].value);
        if (e.isIntersecting && value && Date.now() > quiet) jump.value = value;
      });
    }, { rootMargin: '-15% 0px -70% 0px' });
    Object.keys(here).forEach(function (id) { var t = document.getElementById(id); if (t) io.observe(t); });
    above.forEach(function (el) { io.observe(el); });
  }

  // ----- озвучка: один проигрыватель на страницу; у главы по кнопке на каждый язык (заранее записанная синтетическая речь) -----
  // data-src — копия на сайте (scripts/fetch-audio.mjs, при публикации); data-fallback — выпуск на GitHub,
  // он нужен, когда копии нет, например при локальной сборке.
  var listen = $$('button.listen');
  if (listen.length) {
    var player = new Audio(), current = null, spoken = lang();
    player.preload = 'none';
    var stopped = function () { if (current) { current.setAttribute('aria-pressed', 'false'); current.classList.remove('playing'); } current = null; };
    var start = function (b, src) {
      player.src = src;
      player.play().catch(function () {
        if (current === b && b.dataset.fallback && src !== b.dataset.fallback) start(b, b.dataset.fallback);
        else if (current === b) stopped();
      });
    };
    player.addEventListener('ended', stopped);
    player.addEventListener('pause', function () { if (current && player.ended === false && player.currentTime > 0 && player.paused) current.classList.remove('playing'); });
    listen.forEach(function (b) {
      b.addEventListener('click', function () {
        if (current === b) {
          if (player.paused) { player.play(); b.classList.add('playing'); b.setAttribute('aria-pressed', 'true'); }
          else { player.pause(); b.setAttribute('aria-pressed', 'false'); }
          return;
        }
        stopped();
        current = b; b.classList.add('playing'); b.setAttribute('aria-pressed', 'true');
        start(b, b.dataset.src);
      });
    });
    // при смене языка перевода чтение на прежнем языке останавливается
    document.addEventListener('neoscholia:reader', function () {
      if (lang() === spoken) return;
      spoken = lang();
      if (current) { player.pause(); stopped(); }
    });
  }
})();
