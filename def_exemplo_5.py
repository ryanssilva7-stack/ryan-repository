import os

os.system("cls")

# definições
def logo_senai():
    os.system("cls")
    print("===== =====")
    print("   SENAI")
    print("===== =====")

def somar(a):
    soma = sum(a)
    return soma

def subtrair(n1 , n2):
    subtracao = n1 - n2
    return subtracao


def multiplicar(n1 , n2):
    print(f"Multiplicação: {n1 * n2}")
    


def dividir(n1 , n2):
    print(f"divisão: {n1 / n2}")



# dados
quantidade_de_numeros = 2
armazenamento_de_numeros = []

# PROCESSO
print("==== solicitando dados ====")
for i in range(quantidade_de_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    armazenamento_de_numeros.append(numero)

soma = somar(armazenamento_de_numeros)
subtracao = subtrair(armazenamento_de_numeros[0], armazenamento_de_numeros[1])


print("==== exibindo dados ====") 
print(f"soma: {soma}")
print(f"subtração: {subtracao}")
multiplicar(armazenamento_de_numeros[0], armazenamento_de_numeros[1])
dividir(armazenamento_de_numeros[0], armazenamento_de_numeros[1])