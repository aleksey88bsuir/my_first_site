document.querySelector('.animated').onclick = function () {
    this.style.backgroundColor = 'tomato';
}

document.querySelector('button').onclick = function () {
    document.querySelector('.move0').style.left = '0px'
    document.querySelector('.move1').style.left = '0px'
    document.querySelector('.move2').style.left = '0px'
    document.querySelector('.move3').style.left = '0px'
    document.querySelector('.move4').style.left = '0px'
}

document.querySelectorAll('button')[1].onclick = function () {
    document.querySelector('.move0').style.left = '1000px'
    document.querySelector('.move1').style.left = '1000px'
    document.querySelector('.move2').style.left = '1000px'
    document.querySelector('.move3').style.left = '1000px'
    document.querySelector('.move4').style.left = '1000px'
}
