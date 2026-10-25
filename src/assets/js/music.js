(function () {
  var current = 'all';
  var cards = Array.prototype.slice.call(document.querySelectorAll('#cards .card'));
  var only = document.getElementById('nowhere');
  var empty = document.getElementById('empty');
  function apply() {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (current === 'all' || c.dataset.g === current) && (!only.checked || c.dataset.nowhere === '1');
      c.hidden = !ok; if (ok) shown++;
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
