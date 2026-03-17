import os
import time
os.system("cls")

# dados
resultado = 0
quantidade_de_notas = 4
repeticao = quantidade_de_notas + 1

# processo
for i in range (1, repeticao):
    numero = float(input(f"Digite a {i}ª nota: "))
    resultado += (numero / quantidade_de_notas)
    media = round (resultado, 1)

print ("\n--- Carregando ---\n")

time.sleep(2)

print (f"Média:{media}")
if media >= 7:
    print("Aprovado\n")
else:
    print("Reprovado\n")
