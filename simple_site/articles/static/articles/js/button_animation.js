document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.animated-button');

    buttons.forEach(function(button) {
        button.addEventListener('mouseover', function() {
            this.style.backgroundColor = 'white'; // Цвет при наведении
        });

        button.addEventListener('mouseout', function() {
            this.style.backgroundColor = ''; // Возвращение к исходному цвету
        });
    });
});
