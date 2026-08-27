//DOM
const alvo = document.querySelector('#alvo')
const bt_yamal = document.querySelector('#bt1')
const bt_cr7 = document.querySelector('#bt2')
const bt_messi = document.querySelector('#bt3')

//Eventos
bt_yamal.addEventListener('click', acao_yamal)
bt_cr7.addEventListener('click', acao_cr7)
bt_messi.addEventListener('click', acao_messi)

//Ação
function acao_yamal(){
    alvo.src = 'images/yamal.jpg'
}
function acao_cr7(){
    alvo.src = 'images/cr7.jpg'
}
function acao_messi(){
    alvo.src = 'images/messi.webp'
}