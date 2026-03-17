import os
import time
os.system("cls")

# dados
soma = 0

# processo
for i in range (1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    soma += numero

print (soma)