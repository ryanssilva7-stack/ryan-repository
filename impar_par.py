import os
os.system("cls")

# dados
soma = 0
par = 0
impar = 0
# processo
for i in range (1, 6):
    numero = int(input(f"Digite o {i}º número: "))
   
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    print(f"Números pares: {par}; Números impares: {impar}\n")
