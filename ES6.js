const VetorNumeros = [10, 20, 30, 40, 50]

console.log("Exibindo todos os elementos do vetor:")
console.log(VetorNumeros)

console.log("Multiplicando cada elemento do vetor por 2:")
const dobrados = VetorNumeros.map( n => n * 2)
console.log(dobrados)

console.log("Filtrando elementos impares:")
VetorNumeros.push(1)
VetorNumeros.push(3)
const impares = VetorNumeros.filter( n => n % 2 == 1)
console.log(impares)

console.log("Filtrando elementos pares:")
const pares = VetorNumeros.filter( n => n % 2 == 0)
console.log(pares)

console.log("Filtrando elementos negativos:")
VetorNumeros.push(-3)
VetorNumeros.push(-2)
VetorNumeros.push(-8)
const negativos = VetorNumeros.filter(n => n < 0)
console.log(negativos)

console.log("Somando todos os elementos do vetor:")
const total = VetorNumeros.reduce((soma, atual) => soma + atual, 0)
console.log(total)