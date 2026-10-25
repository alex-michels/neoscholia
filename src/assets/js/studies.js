(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('#list .study'));
  var sec = 'all', onlyWork = false;
  var workBtn = document.getElementById('only-work');
  var empty = document.getElementById('empty');
  function count(kind) { return items.filter(function (i) { return i.dataset.kind === kind; }).length; }
  function word(n) { var m10 = n % 10, m100 = n % 100; return (m10 === 1 && m100 !== 11) ? 'работа' : (m10 >= 2 && m10 <= 4 && (m100 < 12 || m100 > 14)) ? 'работы' : 'работ'; }
  [['n-text', 'text'], ['n-method', 'method'], ['n-data', 'data']].forEach(function (p) { var n = count(p[1]); document.getElementById(p[0]).textContent = n + ' ' + word(n) + ' в плане'; });
  function apply() {
    var shown = 0;
    items.forEach(function (i) {
      var ok = (sec === 'all' || i.dataset.sec === sec) && (!onlyWork || i.dataset.st === 'work');
      i.hidden = !ok; if (ok) shown++;
    });
    empty.hidden = shown > 0;
    document.querySelectorAll('.filters [data-sec]').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.sec === sec)); });
    workBtn.setAttribute('aria-pressed', String(onlyWork));
  }
  document.querySelector('.filters').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b === workBtn) onlyWork = !onlyWork; else sec = b.dataset.sec;
    apply();
  });
  apply();
})();
