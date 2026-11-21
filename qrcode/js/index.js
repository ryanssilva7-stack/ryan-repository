// DOM
const botao = document.querySelector('#botao')
const entrada = document.querySelector('#entrada')
const qrcode = document.querySelector('#qrcode')

// Event
botao.addEventListener('click', gerar)

// ACTION
function gerar(){
    texto = entrada.value
    qrcode.innerHTML = ''
    new QRCode(qrcode, {
        text:texto,
        width: 300,
        height:300,
        colorDark:'rgb(48, 33, 82)',
        colorLight: 'rgb(120, 181, 62)'
    })
}