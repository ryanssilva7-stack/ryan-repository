import os
os .system("cls")

# exemplo de uso da função
# função com retorno
def somar(n1 , n2):
    soma = n1 + n2
    return soma

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

resultado = somar(primeiro_numero, segundo_numero)

print(f" Soma: {resultado}")