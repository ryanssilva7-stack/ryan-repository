const notas = [10, 10, 10]

const soma = notas.reduce((soma, atual) => soma + atual, 0)
console.log(`Média: ${soma / notas.length}`)   