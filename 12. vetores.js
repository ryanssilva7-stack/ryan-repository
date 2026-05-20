const VetorNomes = ['Marta', 'José', 'Maria']

console.log("Exibindo todos os elementos:")
console.log(VetorNomes)

console.log("Exibindo o primeiro  elemento:")
console.log(VetorNomes[0])

console.log("Adcionado um elemento no início:")
VetorNomes.unshift('Fabiana')
console.log(VetorNomes)

console.log("Removendo o primeiro elemento do vetor:")
VetorNomes.shift()
console.log(VetorNomes)

console.log("Adcionando um elemento no final:")
VetorNomes.push('Mariana')
console.log(VetorNomes)

console.log("Removendo o último elemento do vetor:")
VetorNomes.pop()
console.log(VetorNomes)

console.log('\nLaço de repetição para percorrer todo o vetor: ')
console.log('Índice: Nome')
VetorNomes.forEach((nome, index) => {
    console.log(`  ${index}   :  ${nome}`)
})