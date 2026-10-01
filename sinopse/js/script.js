// DOM
const imagem = document.querySelector('#troca_img')
const texto = document.querySelector('#troca_texto')
const bt1 = document.querySelector('#bt1')
const bt2 = document.querySelector('#bt2')
const bt3 = document.querySelector('#bt3')
const bt4 = document.querySelector('#bt4')

// Event
bt1.addEventListener('click', el_chapo)
bt2.addEventListener('click', thrones)
bt3.addEventListener('click', peak)
bt4.addEventListener('click', veloses)

// Action
function el_chapo(){
    imagem.src = 'image/el_chapo_menor.jpg'
    texto.textContent = 'A série El Chapo acompanha a história real da ascensão, captura e fuga do famoso traficante mexicano Joaquín "El Chapo" Guzmán.'
}
function thrones(){
    imagem.src = "image/game_thrones_menor.jpg"
    texto.textContent = 'Sucesso entre os livros mais vendidos, a série de obras "A Song of Ice and Fire", de George R.R. Martin, é levada à tela quando HBO decide navegar a fundo pelo gênero e recriar a fantasia medieval épica.'
}
function peak(){
    imagem.src = 'image/peak_blindes._menor.jpg'
    texto.textContent = 'Uma notória gangue da Inglaterra de 1919 ascende no submundo liderada pelo cruel Tommy Shelby, um criminoso disposto a subir na vida a qualquer preço.'
}
function veloses(){
    imagem.src = 'image/Velozes_e_Furiosos_-_Capa._menor.webp'
    texto.textContent = 'A franquia Velozes e Furiosos fala sobre a cultura das corridas de rua ilegais, que evoluiu ao longo dos anos para grandes assaltos e missões globais de ação e espionagem, tendo o valor da família e a lealdade como o seu maior centro emocional.'
}