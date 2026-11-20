// «Короткие ночи лестригонов» — рисунок 1: небо на выбранной широте около 150 г. до н. э.
// Разметка рисунка — в _includes/study/laestrygonians-figure.njk (svg#sphere, ползунок #lat, кнопки мест #presets,
// показания #r-day, #r-night, #r-az, #r-dra, пояснение #place-note); цвета линий — в css/pages/study-laestrygonians.css.
// Общее поведение статьи (примечания) — в article.js.
(function () {
  var svg = document.getElementById('sphere');
  if (!svg) return;

  var EPS = 23.713;          // наклон эклиптики, 150 г. до н. э. (Laskar 1986)
  var DEC_G = 52.959;        // склонение γ Дракона, 150 г. до н. э. (прецессия IAU 2006)
  var PLACES = [
    { id: 'alex', name: 'Александрия', phi: 31.20, note: 'Голова Дракона заходит почти на пять часов: здесь строка Арата неверна.' },
    { id: 'rhod', name: 'Родос', phi: 36.44, note: 'Голова Дракона уходит под горизонт примерно на полтора часа. Аттал, оппонент Гиппарха, считал, что она ненадолго заходит; рассуждал ли он от широты Родоса, мы не знаем.' },
    { id: 'hell', name: 'Эллада Гиппарха', phi: 36.87, note: 'Гномон 4:3. По расчёту γ Дракона опускается на 0,17° под горизонт и заходит примерно на 50 минут; у Гиппарха, с его данными в целых градусах, она лежит на самом круге незаходящих звёзд. Летняя ночь — больше девяти часов.' },
    { id: 'leon', name: 'Леонтины', phi: 37.28, note: 'Сицилийская версия схолий. γ Дракона не заходит, но проходит всего в 0,24° над горизонтом; летняя ночь — больше девяти часов.' },
    { id: 'athn', name: 'Афины', phi: 37.97, note: 'Голова Дракона не заходит. Летняя ночь — больше девяти часов.' },
    { id: 'perg', name: 'Пергам', phi: 39.13, note: 'Здесь работал Кратет (родом он из Малла, 36,8°). Летняя ночь — около девяти часов.' },
    { id: 'zen', name: 'Дракон в зените', phi: 52.96, note: 'Гипотеза: γ Дракона проходит через зенит. Ночь около семи часов, но не час; для других звёзд головы — до шести часов.' },
    { id: 'arat', name: 'Схолия к Арату', phi: 63.11, note: 'День 20 часов, ночь 4: цифры схолии к Арату 61–62, где связь Арата с Гомером приписана Кратету.' },
    { id: 'crat', name: 'Гемин: 23 часа', phi: 66.105, note: '23-часовой день Кратета по Гемину: ночь — один час, закат рядом с восходом.' }
  ];
  var R = 130, CX = 200, CY = 165, D2R = Math.PI / 180;
  var NS = 'http://www.w3.org/2000/svg';
  function el(tag, attrs, text) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text) e.textContent = text;
    svg.appendChild(e); return e;
  }
  function pt(theta) { return { x: CX + R * Math.cos(theta * D2R), y: CY - R * Math.sin(theta * D2R) }; }
  function fmt(n, d) { return n.toFixed(d).replace('.', ','); }
  function hm(h) { var t = Math.round(h * 60); return Math.floor(t / 60) + ' ч ' + String(t % 60).padStart(2, '0') + ' мин'; }

  el('path', { 'class': 'sv-ground', d: 'M' + (CX - R) + ' ' + CY + ' A' + R + ' ' + R + ' 0 0 0 ' + (CX + R) + ' ' + CY + ' Z' });
  el('circle', { 'class': 'sv-sphere', cx: CX, cy: CY, r: R });
  var eq = el('line', { 'class': 'sv-eq' });
  var circ = el('line', { 'class': 'sv-circ' });
  var axis = el('line', { 'class': 'sv-axis' });
  var dra = el('line', { 'class': 'sv-dra' });
  var night = el('line', { 'class': 'sv-night' });
  var day = el('line', { 'class': 'sv-day' });
  el('line', { 'class': 'sv-hor', x1: CX - R - 8, y1: CY, x2: CX + R + 8, y2: CY });
  var noon = el('circle', { 'class': 'sv-pt', r: 4 });
  var midn = el('circle', { 'class': 'sv-pt-hollow', r: 4 });
  var pole = el('circle', { 'class': 'sv-pole', r: 3.5 });
  var star = el('circle', { 'class': 'sv-star', r: 5 });
  el('text', { 'class': 'sv-lbl strong', x: CX + R + 12, y: CY + 4 }, 'N');
  el('text', { 'class': 'sv-lbl strong', x: CX - R - 22, y: CY + 4 }, 'S');
  el('text', { 'class': 'sv-lbl', x: CX + 6, y: CY - R - 8 }, 'зенит');
  el('text', { 'class': 'sv-lbl', x: CX - R + 6, y: CY - 6 }, 'горизонт');
  var poleLbl = el('text', { 'class': 'sv-lbl strong' }, 'полюс мира');
  var sunLbl = el('text', { 'class': 'sv-lbl sun', 'text-anchor': 'end' }, 'полдень');
  var draLbl = el('text', { 'class': 'sv-lbl dra', 'text-anchor': 'end' });
  var draG = document.createElementNS(NS, 'tspan'); draG.setAttribute('class', 'sv-grk'); draG.textContent = 'γ'; draLbl.appendChild(draG);
  draLbl.appendChild(document.createTextNode(' Дракона'));
  var midLbl = el('text', { 'class': 'sv-lbl sun', 'text-anchor': 'end' }, 'полночь');

  function chord(line, a, b) { line.setAttribute('x1', a.x); line.setAttribute('y1', a.y); line.setAttribute('x2', b.x); line.setAttribute('y2', b.y); }
  function place(node, p) { node.setAttribute('cx', p.x); node.setAttribute('cy', p.y); }

  function dayLength(phi, dec) {
    var c = -Math.tan(phi * D2R) * Math.tan(dec * D2R);
    if (c <= -1) return 24; if (c >= 1) return 0;
    return 2 * Math.acos(c) / D2R / 15;
  }

  var latIn = document.getElementById('lat');
  var presetBox = document.getElementById('presets');
  PLACES.forEach(function (p) {
    var b = document.createElement('button');
    b.type = 'button'; b.textContent = p.name; b.dataset.phi = p.phi; b.setAttribute('aria-pressed', 'false');
    presetBox.appendChild(b);
  });
  presetBox.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    latIn.value = b.dataset.phi; draw();
  });

  function draw() {
    var phi = parseFloat(latIn.value);
    document.getElementById('lat-out').textContent = fmt(phi, Math.abs(phi + DEC_G - 90) < 0.05 ? 3 : 1) + '°'; // больше знаков там, где звезда касается горизонта
    // ось мира, экватор, граница незаходящих звёзд
    chord(axis, pt(phi), pt(phi + 180));
    chord(eq, pt(phi + 90), pt(phi - 90));
    chord(circ, pt(2 * phi), pt(0));
    place(pole, pt(phi));
    var pp = pt(phi);
    poleLbl.setAttribute('x', pp.x + 8); poleLbl.setAttribute('y', pp.y - 6);
    // Солнце в летнее солнцестояние: хорда от полудня (вверху) до полуночи (внизу)
    var up = pt(phi + 90 - EPS), lo = pt(phi - (90 - EPS));
    place(noon, up); place(midn, lo);
    sunLbl.setAttribute('x', up.x - 9); sunLbl.setAttribute('y', up.y + 4);
    midLbl.setAttribute('x', lo.x - 9); midLbl.setAttribute('y', lo.y + 15);
    if (lo.y > CY) {
      var t = (CY - up.y) / (lo.y - up.y);
      var ix = { x: up.x + t * (lo.x - up.x), y: CY };
      chord(day, up, ix); chord(night, ix, lo); night.style.display = '';
    } else { chord(day, up, lo); night.style.display = 'none'; }
    // γ Дракона: суточный круг и нижняя точка
    var dUp = pt(phi + 90 - DEC_G), dLo = pt(phi - (90 - DEC_G));
    chord(dra, dUp, dLo); place(star, dLo);
    draLbl.setAttribute('x', dLo.x - 10); draLbl.setAttribute('y', dLo.y + 18);
    var low = phi + DEC_G - 90;
    var TOL = 1e-9; // только погрешность вычислений: звезда «касается горизонта» лишь ровно при 0°
    star.setAttribute('class', 'sv-star' + (low < -TOL ? ' below' : ''));

    // показания
    var L = dayLength(phi, EPS);
    document.getElementById('r-day').innerHTML = '<b>' + hm(L) + '</b>';
    document.getElementById('r-night').innerHTML = L >= 24 ? 'Солнце не заходит' : '<b>' + hm(24 - L) + '</b>';
    var cA = Math.sin(EPS * D2R) / Math.cos(phi * D2R);
    document.getElementById('r-az').textContent = cA >= 1 ? 'Солнце летом не заходит'
      : 'в ' + fmt(Math.acos(cA) / D2R, 0) + '° к востоку и западу от точки севера';
    var draText;
    var near = Math.abs(low) < 0.5 ? ' — почти касается горизонта' : '';
    var dig = Math.abs(low) < 0.01 ? 3 : 2; // показать −0,001°, а не −0,00°
    if (Math.abs(low) <= TOL) draText = 'касается горизонта';
    else if (low > 0) draText = 'не заходит; в нижней точке +' + fmt(low, dig) + '°' + near;
    else draText = 'заходит примерно на ' + hm(24 - dayLength(phi, DEC_G)) + '; в нижней точке −' + fmt(-low, dig) + '°' + near;
    document.getElementById('r-dra').textContent = draText;

    var match = PLACES.filter(function (p) { return Math.abs(p.phi - phi) < 0.003; })[0];
    presetBox.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', String(!!match && parseFloat(b.dataset.phi) === match.phi)); });
    document.getElementById('place-note').textContent = match ? match.name + '. ' + match.note
      : 'Двигайте ползунок или выберите место: на рисунке видно, как меняются летняя ночь и нижняя точка головы Дракона.';
  }
  latIn.addEventListener('input', draw);
  // с клавиатуры стрелка сдвигает широту на 0,1° (шаг ползунка 0,005° нужен готовым местам; Shift + стрелка — точный шаг)
  latIn.addEventListener('keydown', function (e) {
    var d = { ArrowRight: 1, ArrowUp: 1, ArrowLeft: -1, ArrowDown: -1 }[e.key];
    if (!d || e.shiftKey) return;
    e.preventDefault();
    latIn.value = Math.round((parseFloat(latIn.value) + d * 0.1) * 10) / 10;
    draw();
  });
  draw();
})();
