(function () {
  var q = document.getElementById('q');
  var empty = document.getElementById('empty');
  var hint = document.getElementById('hint');
  var shelves = Array.prototype.slice.call(document.querySelectorAll('[data-shelf]'));
  document.getElementById('search-form').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('collections').scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  });
  function norm(s) { return s.toLowerCase().replace(/ё/g, 'е'); }
  q.addEventListener('input', function () {
    var term = norm(q.value.trim());
    var total = 0;
    shelves.forEach(function (shelf) {
      var shelfHit = term && norm(shelf.querySelector('h3').textContent + ' ' + shelf.querySelector('.scope').textContent).indexOf(term) > -1;
      var shown = 0;
      shelf.querySelectorAll('.texts li').forEach(function (li) {
        var hit = !term || shelfHit || norm(li.textContent).indexOf(term) > -1;
        li.hidden = !hit; if (hit) shown++;
      });
      shelf.querySelectorAll('.subhead').forEach(function (h) {
        var list = h.nextElementSibling; h.hidden = !!term && !list.querySelector('li:not([hidden])');
      });
      shelf.hidden = !!term && shown === 0;
      total += shown;
    });
    empty.hidden = !term || total > 0;
    hint.textContent = term ? (total ? 'Найдено текстов: ' + total : 'Совпадений нет') : 'Поиск сразу фильтрует разделы ниже.';
  });
})();
