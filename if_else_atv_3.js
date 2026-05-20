let numero = 4

function verificar(n) {
    if (n > 0)
        r = "positivo."
    else if (n < 0)
        r = "negativo."
    else
        r = "neutro."
    return r
}


resultado = verificar(numero)

console.log(`O número ${numero} é ${resultado}`)