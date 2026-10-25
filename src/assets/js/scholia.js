(function () {
  var current = 'all';
  var rows = Array.prototype.slice.call(document.querySelectorAll('#cat tbody tr'));
  var only = document.getElementById('nowhere');
  var empty = document.getElementById('empty');
  function apply() {
    var shown = 0;
    rows.forEach(function (r) {
      var ok = (current === 'all' || r.dataset.g === current) && (!only.checked || r.dataset.nowhere === '1');
      r.hidden = !ok; if (ok) shown++;
    });
    empty.hidden = shown > 0;
    document.querySelectorAll('.filters button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.f === current)); });
  }
  document.querySelector('.filters').addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return; current = b.dataset.f; apply();
  });
  only.addEventListener('change', apply);
  apply();
})();
