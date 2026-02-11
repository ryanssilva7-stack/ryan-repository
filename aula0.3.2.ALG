Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
// Seção de Declarações das variáveis 
nome: caractere
primeira_nota: real
segunda_nota: real
terceira_nota: real
nota_final: real
resultado: caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
//entrada
escreva ("Digite o seu nome: ")
leia(nome)
escreval
escreva ("Digite a nota 1: ")
leia (primeira_nota)
escreval
escreva ("Digite a nota 2: ")
leia (segunda_nota)
escreval
escreva ("Digite a nota 3: ")
leia (terceira_nota)

//processamento
nota_final <- (primeira_nota + segunda_nota + terceira_nota) / 3

se nota_final > 6 então
 resultado <- "Parabéns"
 senao
 resultado <- "Precisa melhorar!!"
  fimse

// saida
escreval
escreval
escreval ("Nota final:", nota_final:2:1)
escreva (resultado)
Fimalgoritmo