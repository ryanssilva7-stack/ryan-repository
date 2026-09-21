// dom
km = document.querySelector('#distancia')
consumo = document.querySelector('#veic_consumo')
preco = document.querySelector('#preco_combustivel')
bt = document.querySelector('#bt_calculo') 
result = document.querySelector('#result') 

// event
bt.addEventListener('click', calculo)

// action
calculo