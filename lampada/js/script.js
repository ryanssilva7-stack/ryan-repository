const imagem = document.querySelector('#alvo_troca')
const ligar = document.querySelector('#turn_on')
const desligar = document.querySelector('#turn_off')

ligar.addEventListener('click', acao_ligar)
desligar.addEventListener('click', acao_desligar)

function acao_ligar(){
    imagem.src = "images/lampada-acesa.png"
}
function acao_desligar(){
    imagem.src = 'images/lampada-apagada.png'
}
