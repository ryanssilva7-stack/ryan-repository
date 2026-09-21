// dom
const km = document.querySelector('#distancia')
const consumo = document.querySelector('#veic_consumo')
const preco = document.querySelector('#preco_combustivel')
const bt = document.querySelector('#bt_calculo') 
const result = document.querySelector('#result') 

// event
bt.addEventListener('click', calculo)

// action
function calculo(){
    d = Number(km.value)
    c = Number(consumo.value)
    p = Number(preco.value)

    r = (d/c)*p

    result.textContent = `R$ ${r.toFixed(2)}`
}