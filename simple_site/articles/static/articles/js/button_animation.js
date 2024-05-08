
    var buttons = document.querySelectorAll('.animated-button');
    Array.from(buttons).forEach(function(button) {
        button.addEventListener('mouseover', function() {
            button.style.backgroundColor = 'red'; // Цвет при наведении
        });

        button.addEventListener('mouseout', function() {
            button.style.backgroundColor = 'yellow'; // Возвращение к исходному цвету
        });
    });
