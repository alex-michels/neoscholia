// Neoscholia — общее поведение страниц. Подключается на каждой странице; всё управляется атрибутами разметки,
// поэтому новой странице свой скрипт обычно не нужен.
//
//   Тема            <button data-theme-toggle> — светлая / тёмная тема; выбор хранится в браузере.
//   Режим чтения    <div class="seg-ctl" data-pref="view|tr"> с кнопками data-value и флажок <input data-pref="notes">.
//                   Состояние лежит на <html> (data-view, data-tr, data-notes) и запоминается в браузере; язык — ещё и
//                   в адресе (?tr=en); ?view=… читается из адреса. До отрисовки состояние выставляет скрипт в <head>
//                   (layouts/base.njk).
//   Переключатель   <div class="seg-ctl" data-switch="#блок"> с кнопками data-value: внутри блока остаются видимыми
//                   только элементы с data-when="значение".
//   Фильтры         <div class="filters" data-filter="#список" data-empty="#пусто"> с кнопками data-f="группа" и
//                   флажками data-flag="имя" (чекбокс или кнопка); у элементов списка — data-g="группа" и data-имя="1";
//                   data-flag-value="значение" у флажка — если отбирать нужно не по "1".
//   Копирование     <button data-copy="#элемент"> кладёт текст элемента в буфер обмена.
//   Оглавление      <nav class="toc" data-spy> подсвечивает раздел, который сейчас на экране; на узком экране сворачивается.
//   Переход         <select data-jump> с адресами #якорей в значениях.
//   Поиск по списку <input data-search="#область" …> — описание атрибутов у кода ниже.
(function () {
  var root = document.documentElement;
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  // сравнение без регистра и надстрочных знаков: «ё» = «е», греческое слово находится и без ударений и придыханий
  function norm(s) { return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ς/g, 'σ'); }
  function pressed(buttons, test) { buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(!!test(b))); }); }

  // ----- тема -----
  $$('[data-theme-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
      root.dataset.theme = dark ? 'light' : 'dark';
      try { localStorage.setItem('neoscholia-theme', root.dataset.theme); } catch (e) {}
      // цвет панели браузера на телефоне — по выбранной теме, а не по системной
      $$('meta[name="theme-color"]').forEach(function (m) { m.removeAttribute('media'); m.content = dark ? '#e7dcc4' : '#17130e'; });
    });
  });

  // ----- режим чтения: показ (перевод / параллельно / оригинал), язык перевода, новые схолии -----
  var prefCtls = $$('[data-pref]');
  if (prefCtls.length) {
    var KEY = 'neoscholia-reader';
    var state = { view: root.dataset.view || 'parallel', lang: root.dataset.tr || 'ru', notes: root.dataset.notes !== 'off' };
    var apply = function () {
      root.dataset.view = state.view; root.dataset.tr = state.lang; root.dataset.notes = state.notes ? 'on' : 'off';
      prefCtls.forEach(function (c) {
        if (c.dataset.pref === 'notes') c.checked = state.notes;
        else pressed($$('button[data-value]', c), function (b) { return b.dataset.value === (c.dataset.pref === 'tr' ? state.lang : state.view); });
      });
      // ссылки на примечания ведут к русским якорям; при английском переводе — к их английским парам
      $$('sup.n a').forEach(function (a) {
        var base = a.getAttribute('href').replace(/-en$/, '');
        a.setAttribute('href', state.lang === 'en' ? base + '-en' : base);
      });
    };
    var save = function () {
      try {
        var all = JSON.parse(localStorage.getItem(KEY) || '{}');
        all.view = state.view; all.lang = state.lang; all.notes = state.notes;
        localStorage.setItem(KEY, JSON.stringify(all));
      } catch (e) {}
      try {
        var url = new URL(location.href);
        if (state.lang === 'en') url.searchParams.set('tr', 'en'); else url.searchParams.delete('tr');
        if (url.searchParams.has('view')) url.searchParams.set('view', state.view);
        history.replaceState(null, '', url);
      } catch (e) {}
      document.dispatchEvent(new CustomEvent('neoscholia:reader', { detail: state }));
    };
    prefCtls.forEach(function (c) {
      if (c.dataset.pref === 'notes') c.addEventListener('change', function () { state.notes = c.checked; apply(); save(); });
      else c.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-value]'); if (!b) return;
        if (c.dataset.pref === 'tr') state.lang = b.dataset.value; else state.view = b.dataset.value;
        apply(); save();
      });
    });
    apply();
  }

  // ----- местный переключатель (язык аннотации, формат ссылки) -----
  $$('.seg-ctl[data-switch]').forEach(function (ctl) {
    var target = document.querySelector(ctl.dataset.switch); if (!target) return;
    ctl.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-value]'); if (!b) return;
      $$('[data-when]', target).forEach(function (el) { el.hidden = el.dataset.when !== b.dataset.value; });
      pressed($$('button[data-value]', ctl), function (x) { return x === b; });
      $$('[data-copy]', target).forEach(function (c) { if (c.dataset.label) c.textContent = c.dataset.label; });
    });
  });

  // ----- фильтры каталога -----
  $$('.filters[data-filter]').forEach(function (bar) {
    var target = document.querySelector(bar.dataset.filter); if (!target) return;
    var items = $$('[data-g]', target);
    var empty = bar.dataset.empty ? document.querySelector(bar.dataset.empty) : null;
    var flags = $$('[data-flag]', bar);
    var current = 'all';
    function on(el) { return el.type === 'checkbox' ? el.checked : el.getAttribute('aria-pressed') === 'true'; }
    function apply() {
      var shown = 0;
      items.forEach(function (it) {
        var ok = (current === 'all' || it.dataset.g === current) &&
          flags.every(function (f) { return !on(f) || it.dataset[f.dataset.flag] === (f.dataset.flagValue || '1'); });
        it.hidden = !ok; if (ok) shown++;
      });
      if (empty) empty.hidden = shown > 0;
      pressed($$('button[data-f]', bar), function (b) { return b.dataset.f === current; });
    }
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.dataset.flag) b.setAttribute('aria-pressed', String(!on(b)));
      else if (b.dataset.f) current = b.dataset.f;
      else return;
      apply();
    });
    bar.addEventListener('change', apply);
    apply();
  });

  // ----- копирование в буфер -----
  $$('[data-copy]').forEach(function (btn) {
    btn.dataset.label = btn.textContent;
    btn.addEventListener('click', function () {
      var scope = document.querySelector(btn.dataset.copy); if (!scope) return;
      var el = $$('[data-when]', scope).filter(function (x) { return !x.hidden; })[0] || scope;
      function selectIt() {
        var r = document.createRange(); r.selectNodeContents(el);
        var s = getSelection(); s.removeAllRanges(); s.addRange(r);
        btn.textContent = 'Выделено — нажмите Ctrl+C';
      }
      try { navigator.clipboard.writeText(el.textContent).then(function () { btn.textContent = 'Скопировано'; setTimeout(function () { btn.textContent = btn.dataset.label; }, 2500); }, selectIt); }
      catch (e) { selectIt(); }
    });
  });

  // ----- оглавление: на широком экране раскрыто и следит за прокруткой, на узком сворачивается -----
  $$('.toc').forEach(function (toc) {
    var details = toc.querySelector('details');
    var wide = matchMedia('(min-width: 1201px)');
    function fit() { if (details) details.open = wide.matches; }
    fit();
    if (wide.addEventListener) wide.addEventListener('change', fit);
    if (details) toc.addEventListener('click', function (e) { if (e.target.closest('a') && !wide.matches) details.open = false; });
    if (!toc.hasAttribute('data-spy')) return;
    // текущий раздел — последний, чей заголовок уже выше четверти экрана (верно и после перехода по ссылке вглубь раздела)
    var links = $$('a[href^="#"]', toc), targets = [], ticking = false;
    links.forEach(function (a) { var t = document.getElementById(a.getAttribute('href').slice(1)); if (t) targets.push({ el: t, a: a }); });
    function spy() {
      ticking = false;
      var line = innerHeight * 0.25, cur = null;
      targets.forEach(function (x) { if (x.el.getBoundingClientRect().top <= line) cur = x; });
      links.forEach(function (a) { if (cur && a === cur.a) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
    }
    addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(spy); } }, { passive: true });
    spy();
  });

  // ----- переход к главе или разделу -----
  $$('select[data-jump]').forEach(function (sel) {
    sel.addEventListener('change', function () {
      if (!sel.value) return;
      var t = document.getElementById(sel.value.replace(/^#/, ''));
      if (t) { t.scrollIntoView(); try { history.replaceState(null, '', sel.value); } catch (e) {} }
    });
  });

  // ----- поиск-фильтр по списку на странице -----
  // data-search="#область": элементы data-search-item (по умолчанию li) скрываются, если не содержат запрос;
  // data-search-text — где искать внутри элемента (по умолчанию весь его текст); у самого элемента можно дать
  // дополнительные слова в data-keywords (например, название раздела);
  // data-search-group — контейнеры, которые прячутся целиком, если в них ничего не найдено;
  // data-search-head — подзаголовки: прячутся, если до следующего подзаголовка нет видимых элементов;
  // data-empty="#элемент" показывается, когда ничего не найдено; data-search-hint="#элемент" — строка с числом найденного.
  $$('input[data-search]').forEach(function (q) {
    var area = document.querySelector(q.dataset.search); if (!area) return;
    var itemSel = q.dataset.searchItem || 'li';
    var items = $$(itemSel, area);
    var groups = q.dataset.searchGroup ? $$(q.dataset.searchGroup, area) : [];
    var headSel = q.dataset.searchHead;
    var empty = q.dataset.empty ? document.querySelector(q.dataset.empty) : null;
    var hint = q.dataset.searchHint ? document.querySelector(q.dataset.searchHint) : null;
    var idle = hint ? hint.textContent : '';
    function text(el) { var t = q.dataset.searchText ? el.querySelector(q.dataset.searchText) : null; return norm((t || el).textContent + ' ' + (el.dataset.keywords || '')); }
    q.addEventListener('input', function () {
      var term = norm(q.value.trim()), total = 0;
      items.forEach(function (it) { var hit = !term || text(it).indexOf(term) > -1; it.hidden = !hit; if (hit) total++; });
      if (headSel) $$(headSel, area).forEach(function (h) {
        var n = h.nextElementSibling, any = false;
        while (n && !n.matches(headSel)) {
          if (n.matches(itemSel) ? !n.hidden : !!n.querySelector(itemSel + ':not([hidden])')) any = true;
          n = n.nextElementSibling;
        }
        h.hidden = !!term && !any;
      });
      groups.forEach(function (g) { g.hidden = !!term && !g.querySelector(itemSel + ':not([hidden])'); });
      if (empty) empty.hidden = !term || total > 0;
      if (hint) hint.textContent = term ? (total ? 'Найдено: ' + total : 'Совпадений нет') : idle;
    });
    if (q.form) q.form.addEventListener('submit', function (e) { e.preventDefault(); });
    // ссылка внутри списка ведёт к записи, которую поиск скрыл: поиск сбрасывается, и переход срабатывает
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#"]'); if (!a || !q.value) return;
      var t = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
      if (t && area.contains(t) && !t.getClientRects().length) { q.value = ''; q.dispatchEvent(new Event('input')); }
    });
  });
})();
