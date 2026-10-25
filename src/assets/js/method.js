(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var map = {};
  links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.removeAttribute('aria-current'); });
          var a = map[e.target.id]; if (a) a.setAttribute('aria-current', 'true');
        }
      });
    }, { rootMargin: '-10% 0px -75% 0px' });
    document.querySelectorAll('.ch').forEach(function (s) { io.observe(s); });
  }
  var btn = document.getElementById('copy-cite');
  btn.addEventListener('click', function () {
    var el = document.getElementById('cite-sample');
    function selectIt() { var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); btn.textContent = 'Выделено — нажмите Ctrl+C'; }
    try { navigator.clipboard.writeText(el.textContent).then(function () { btn.textContent = 'Скопировано'; }, selectIt); } catch (e) { selectIt(); }
  });
})();
