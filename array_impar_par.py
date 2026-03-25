import os
from colorama import init, Fore
os.system("cls")

# Criando um vetor
numero = []
quantidade_de_numeros = 6
par = 0
impar = 0
#Adcionando números
for i in range(quantidade_de_numeros):
    valor = int(input(f"Digite o {i+1}º número: "))
    
    if valor % 2 ==0:
        par += 1
    else:
        impar += 1
        
    numero.append(valor)
    
# Exibindo os números informados
print("\n\n=== Resultados ===")
print(f"Números: {numero}")
print(f"Par {par} | Impar {impar}\n")
