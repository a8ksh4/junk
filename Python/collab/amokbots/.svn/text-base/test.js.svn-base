/*
TODO:
show cursor movement path
animate across movement path
*/

var canvas = null;
var ctx = null;
var boxX = 0;
var boxY = 0;
var shapeValid = true;
var gridSize = 20;
var canvasSize = 600;
var gridWidth = canvasSize / gridSize;
var dragging = false;
var border = 5;

function init() {
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d");
    drawScene();
}

function drawSceneGrid() {
    ctx.beginPath();
    var spacing = canvasSize / gridSize;
    for (var x = 0; x < gridSize; x++) {
        ctx.moveTo(spacing * x, 0);
        ctx.lineTo(spacing * x, canvasSize);
    }
    for (var y = 0; y < gridSize; y++) {
        ctx.moveTo(0, spacing * y);
        ctx.lineTo(canvasSize, spacing * y);
    }
    ctx.stroke();
}

function drawSceneShape() {
    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.fillRect(boxX - border, boxY - border, gridWidth + border * 2, gridWidth + border * 2);
    ctx.fillStyle = "black";

	var img = new Image();
	img.onload = function() {
		ctx.drawImage(img, boxX, boxY);
	}
	img.src = 'smallbot.png';

    ctx.stroke();
}

function drawScene() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawSceneGrid();
    if (shapeValid)
        drawSceneShape();
}

function updateShapeLocation(evt) {
	var gridX = Math.floor((evt.clientX - canvas.offsetLeft) / gridWidth);
    var gridY = Math.floor((evt.clientY - canvas.offsetTop) / gridWidth);
    boxX = gridX * gridWidth;
    boxY = gridY * gridWidth;
    shapeValid = gridX >= 0 && gridX < gridSize && gridY >= 0 && gridY < gridSize;
    drawScene();
}

function handleMousedown(evt) {
    updateShapeLocation(evt);
}
