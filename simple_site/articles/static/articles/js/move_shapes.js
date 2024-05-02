var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');

// Функция для рисования круга
function drawCircle(x, y, radius, color) {
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2, true); // Рисуем полный круг
    ctx.fillStyle = color;
    ctx.fill();
}

// Функция для перемещения фигуры
function moveShape(shape, dx, dy) {
    // Обновляем позицию фигуры
    shape.x += dx;
    shape.y += dy;

    // Очищаем холст перед перерисовкой
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Рисуем фигуру в новой позиции
    drawCircle(shape.x, shape.y, shape.radius, shape.color);
}

// Инициализация фигуры
var circle = {
    x: 100,
    y: 100,
    radius: 50,
    color: 'red'
};

// Запускаем анимацию
setInterval(function() {
    moveShape(circle, 1, 1

); // Перемещаем фигуру на 1 пиксель вправо и вниз
}, 100); // Анимация происходит каждые 100 миллисекунд
