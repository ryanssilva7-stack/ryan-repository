import os
import time
os.system("cls")

# dados
resultado = 0
quantidade_de_notas = 3
repeticao = quantidade_de_notas + 1

# processo
for i in range (1, repeticao):
    numero = float(input(f"Digite a {i}ª nota: "))
    resultado += (numero / quantidade_de_notas)
    media = round (resultado, 1)

print ("\n--- Carregando ---\n")

time.sleep(3)

print (f"Média:{media}")
if media >= 7:
    print("Aprovado\n")
elif media < 7:
    print("recuperação\n")
elif media < 4:
    print("Reprovado\n") 