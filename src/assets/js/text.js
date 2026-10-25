(function () {
  var body = document.body;
  var prefs = { view: 'parallel', lang: 'ru', notes: true };
  try { var saved = JSON.parse(localStorage.getItem('neoscholia-reader') || '{}'); Object.assign(prefs, saved); } catch (e) {}

  function save() { try { localStorage.setItem('neoscholia-reader', JSON.stringify(prefs)); } catch (e) {} }

  function apply() {
    body.classList.remove('view-translation', 'view-parallel', 'view-original');
    body.classList.add('view-' + prefs.view);
    body.dataset.tr = prefs.lang;
    body.classList.toggle('no-notes', !prefs.notes);
    document.querySelectorAll('#view-ctl button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.view === prefs.view)); });
    document.querySelectorAll('#lang-ctl button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.langSet === prefs.lang)); });
    document.getElementById('notes-toggle').checked = prefs.notes;
    // note anchors point at the RU ids; redirect to EN twins when English is shown
    document.querySelectorAll('sup.n a').forEach(function (a) {
      var base = a.getAttribute('href').replace(/-en$/, '');
      a.setAttribute('href', prefs.lang === 'en' ? base + '-en' : base);
    });
  }

  document.getElementById('view-ctl').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return; prefs.view = b.dataset.view; apply(); save();
  });
  document.getElementById('lang-ctl').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return; prefs.lang = b.dataset.langSet; apply(); save();
  });
  document.getElementById('notes-toggle').addEventListener('change', function (e) {
    prefs.notes = e.target.checked; apply(); save();
  });
  document.getElementById('copy-cite').addEventListener('click', function () {
    var btn = this, text = document.getElementById('cite-text').textContent;
    function selectIt() { var r = document.createRange(); r.selectNodeContents(document.getElementById('cite-text')); var s = getSelection(); s.removeAllRanges(); s.addRange(r); btn.textContent = 'Выделено — нажмите Ctrl+C'; }
    try {
      navigator.clipboard.writeText(text).then(function () { btn.textContent = 'Скопировано'; }, selectIt);
    } catch (e) { selectIt(); }
  });
  apply();

  // Audio: one player for the page; each chapter has a button per language (pre-recorded synthetic speech).
  var player = new Audio(), current = null;
  player.preload = 'none';
  function stopped() { if (current) { current.setAttribute('aria-pressed', 'false'); current.classList.remove('playing'); } current = null; }
  player.addEventListener('ended', stopped);
  player.addEventListener('pause', function () { if (current && player.ended === false && player.currentTime > 0 && player.paused) current.classList.remove('playing'); });
  document.querySelectorAll('button.listen').forEach(function (b) {
    b.addEventListener('click', function () {
      if (current === b) {
        if (player.paused) { player.play(); b.classList.add('playing'); b.setAttribute('aria-pressed', 'true'); }
        else { player.pause(); b.setAttribute('aria-pressed', 'false'); }
        return;
      }
      stopped();
      player.src = b.dataset.src;
      player.play().catch(function () { stopped(); });
      current = b; b.classList.add('playing'); b.setAttribute('aria-pressed', 'true');
    });
  });
  // switching the language stops the other language's reading
  document.getElementById('lang-ctl').addEventListener('click', function () { if (current) { player.pause(); stopped(); } });
})();
