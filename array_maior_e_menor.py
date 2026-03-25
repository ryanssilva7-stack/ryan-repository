import os
from colorama import init, Fore
os.system("cls")

# Criando um vetor
numero = []
quantidade_de_numeros = 5
#Adcionando números
for i in range(quantidade_de_numeros):
    valor = float(input(f"Digite o {i+1}º número: "))
    numero.append(valor)
    maior_numero = max(numero)
    menor_numero = min(numero)
    

# Exibindo os números informados
for i in range(quantidade_de_numeros):
    print(f"{i+1}º número: {numero[i]}")
print("\nMaior número:", maior_numero)
print("Menor número:", menor_numero)
    