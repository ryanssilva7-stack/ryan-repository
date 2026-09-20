// DOM
const nota1 = document.querySelector('#nota1')
const nota2 = document.querySelector('#nota2')
const nota3 = document.querySelector('#nota3')
const acao = document.querySelector('acao')
const media = document.querySelector('media')
const situacao = document.querySelector('situacao')

// event
acao.addEventListener('click', calcular)

// action
function calcular(){
    n1 = Number(nota1.value)
    n2 = Number(nota2.value)
    n3 = Number(nota3.value)

    const Total = [n1, n2, n3]
    const soma = n1+n2+n3
    // if (n1 > 10)
    m = soma / length(total)

    if (m > 5){
        s = `Aprovado`
    }
    else {
        s = `Reprovado`
    }

    media.textContent = m
    situacao.textContent = s
}
