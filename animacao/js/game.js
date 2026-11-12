// DOM
const bola = document.querySelector('#caixa')

// Event
document.addEventListener('keydown', move)

// Action
function move(evento){
    
    if(evento.key == 'Space'){
        bola.classList.add('bolaPular')
    }
    
    if(evento.key == 'ArrowDown'){
        bola.classList.remove('bolaPular')
    }

    if(evento.key == 'ArrowRight'){
        posicao = posicao + 10
        bola.style.left = posicao + "px"
    }

    if(evento.key == 'ArrowLeft'){
        posicao = posicao + 10
        bola.style.left = posicao + "px"
    }
}