// DOM
const peso = document.querySelector('#peso')
const altura = document.querySelector('#altura')
const start = document.querySelector('#button')
const resultado_1 = document.querySelector('#resultado1')
const resultado_2 = document.querySelector('#resultado2')

// Event
start.addEventListener('click', calcular)

// Action
function calcular(){
    p = Number(peso.value)
    a = Number(altura.value)

    imc = p/(a*a)

    if(imc < 18.5){
        result = `é magro.`
    }
    else if(imc >= 18.5 && imc < 25){
        result = `está com o peso ideal`
    }
    else if(imc >= 25 && imc < 30){
        result = `está com sobrepeso`
    }
    else if(imc >= 30){
        result = `está com obesidade`
    }


    resultado_1.textContent = `O seu IMC é ${imc.toFixed(2)}.`
    resultado_2.textContent = `Você ${result}.`
}
