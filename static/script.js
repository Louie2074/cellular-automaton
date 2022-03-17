function initGrid(plot, boxes, main, maxWidth) {
  for (let i = 0; i < plot.length; i++) {
    let row = document.createElement('div');
    let rowB = [];
    row.className = 'row';
    for (let j = 0; j < plot[i].length; j++) {
      let box = document.createElement('div');
      box.classList.add('grid-box');
      box.textContent = '';
      row.appendChild(box);
      rowB.push(box);
    }
    boxes.push(rowB);
    main.appendChild(row);
  }

  for (let i = 0; i < boxes.length; i++) {
    for (let j = 0; j < boxes[i].length; j++) {
      boxes[i][j].style.width = maxWidth / plot[i].length + 'px';
      boxes[i][j].style.height = maxWidth / plot.length + 'px';
    }
  }
}

function init(data) {
  const main = document.getElementById('container');
  const maxWidth = parseInt(main.getAttribute('width'));
  plot = wrangleData(data);
  let boxes = [];
  initGrid(plot, boxes, main, maxWidth);
  draw(plot, boxes);
}

function wrangleData(data) {
  plot = [];
  const result = data
    .substring(2, data.length - 2)
    .replace(/\[/g, '')
    .replace(/[\r\n]/g, '')
    .replace(/ /g, '')
    .split(']');

  for (let x of result) {
    let row = [];
    for (let y of x) {
      row.push(Number(y));
    }
    plot.push(row);
  }
  return plot;
}

function draw(plot, boxes) {
  for (let i = 0; i < plot.length; i++) {
    for (let j = 0; j < plot[i].length; j++) {
      if (plot[i][j] == 1) {
        boxes[i][j].style.backgroundColor = 'black';
      }
    }
  }
}
