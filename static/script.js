
let test = '[[0 0 0 0 1 0 0 0 0 0]\n[1 1 1 0 0 0 1 1 1 1]\n[1 1 0 0 1 0 0 1 1 1]\n[1 0 0 0 0 0 0 0 1 1]\n[0 0 1 1 1 1 1 0 0 1]\n[0 0 0 1 1 1 0 0 0 0]\n[1 1 0 0 1 0 0 1 1 0]\n[0 0 0 0 0 0 0 0 0 0]\n[1 1 1 1 1 1 1 1 1 1]\n[1 1 1 1 1 1 1 1 1 1]]'

let boxes = [];
function initGrid(size,main) {
  const maxWidth = parseInt(main.getAttribute('width'));
  for (let i = 0; i < size; i++) {
    let row = document.createElement('div');
    row.className = 'row';
    for (let j = 0; j < size; j++) {
      let box = document.createElement('div');
      box.classList.add('grid-box');
      box.textContent = '';
      row.appendChild(box);
      boxes.push(box);
    }
    main.appendChild(row);
  }

  for (let box of boxes) {
    box.style.width = maxWidth / size + 'px';
    box.style.height = maxWidth / size + 'px';
  }
}

function init(data,main){
  
  clear()
  let plot = []
  const result = data.replace(/\[/g, '').replace(/]/g, '').replace(/ /g,'').split(/\r?\n/);
  for(let x of result){
    let row = []
    for(let y of x){
      row.push(Number(y))
    }
    plot.push(row)
  }
  initGrid(plot[0].length,main);
  draw(plot);
 
}



function draw(plot) {
  for(let i = 0; i<plot.length; i++){
    for(let j = 0; j<plot[i].length; j++){
      if(plot[i][j]==1){
        boxes[i][j].style.backgroundColor = 'black';
      }
    }
  }
}

function clear(){
   boxes.forEach(function (box) {
     box.style.backgroundColor = 'white';
   });
}
