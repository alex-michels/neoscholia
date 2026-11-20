// Neoscholia — поведение страницы статьи (тип article); каркас подключает его сам по pageType: "article".
// Переключатели (язык аннотации, формат ссылки, режим показа приложения), копирование и оглавление — в site.js.
//
//   Примечания   lib/article.js ставит в текст номер <button class="sn-ref" aria-controls="nN"> и сразу за ним
//                текст <span class="sn" id="nN">. На широком экране примечания стоят на поле, и нажатие на номер
//                только выделяет своё примечание. На узком (≤ 900px) примечание скрыто и открывается под строкой
//                по нажатию на номер. Ссылка на #nN (например, из указателей) сама открывает нужное примечание.
(function () {
  var narrow = matchMedia('(max-width: 900px)');
  var refs = Array.prototype.slice.call(document.querySelectorAll('.sn-ref[aria-controls]'));
  function noteOf(btn) { return document.getElementById(btn.getAttribute('aria-controls')); }
  // aria-expanded говорит, видно ли примечание: на широком экране — всегда, на узком — только открытое
  function sync(btn) {
    var note = noteOf(btn);
    if (note) btn.setAttribute('aria-expanded', String(!narrow.matches || note.classList.contains('open')));
  }
  function setOpen(btn, open) {
    var note = noteOf(btn); if (!note) return;
    note.classList.toggle('open', open);
    sync(btn);
  }
  refs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var note = noteOf(btn); if (!note) return;
      var open = !note.classList.contains('open');
      setOpen(btn, open);
      // примечание могло оказаться за краем экрана (на поле — ниже своего номера): подвинуть страницу ровно настолько, чтобы его было видно
      if (open) note.scrollIntoView({ block: 'nearest' });
    });
    sync(btn);
  });
  if (narrow.addEventListener) narrow.addEventListener('change', function () { refs.forEach(sync); });

  // переход по ссылке на примечание: открыть его и показать
  function openTarget() {
    var id = location.hash.slice(1); if (!id) return;
    refs.forEach(function (btn) {
      if (btn.getAttribute('aria-controls') !== id) return;
      setOpen(btn, true);
      if (narrow.matches) noteOf(btn).scrollIntoView({ block: 'center' });
    });
  }
  window.addEventListener('hashchange', openTarget);
  // второй раз — после загрузки шрифтов: строки переверстались, и примечание могло уехать
  if (document.readyState !== 'complete') window.addEventListener('load', openTarget);
  openTarget();
})();
