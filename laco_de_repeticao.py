import os
import time
os.system("cls")

# dados
pares = 0
impares = 0

# processo
for i in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
 
#saída 
print(f"\nPares: {pares}")
print(f"\nImpares: {impares}")