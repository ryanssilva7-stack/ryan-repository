let numero = 60
let resto = (numero % 2)

function verificar(n, r) {
    if (r == 0)
        console.log(`O número ${n} é par.`)
    else
        console.log(`O número ${n} é impar.`)
}

verificar(numero, resto)