(function () {
  // filter all four indexes at once by a substring of the heading or the original form
  var q = document.getElementById('ix-q'), empty = document.getElementById('ix-empty');
  var entries = Array.prototype.slice.call(document.querySelectorAll('.entry'));
  function norm(s) { return s.toLowerCase().replace(/ё/g, 'е'); }
  q.addEventListener('input', function () {
    var term = norm(q.value.trim()), shown = 0;
    entries.forEach(function (e) {
      var hit = !term || norm(e.querySelector('dt').textContent).indexOf(term) > -1;
      e.hidden = !hit; if (hit) shown++;
    });
    document.querySelectorAll('.letter').forEach(function (l) {
      var n = l.nextElementSibling, any = false;
      while (n && !n.classList.contains('letter')) { if (!n.hidden) any = true; n = n.nextElementSibling; }
      l.hidden = !!term && !any;
    });
    empty.hidden = shown > 0;
  });
})();
