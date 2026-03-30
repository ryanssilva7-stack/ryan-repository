
import os
import time

# Limpar o terminal
os.system("cls")

# dados
aluno = input("Digite seu nome: ")
soma = 0
quantidade_de_notas = 3

# processo
for i in range (quantidade_de_notas):
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        
    
        if nota < 0 or nota > 10:
            print("\nNota inválida...")
            print("Tente novamente.\n")
        else:
            soma += nota
            break
        
media = soma / quantidade_de_notas
resultado = round(media, 1)

# saida
print ("\n======= CARREGANDO =======\n")

time.sleep(2)

print (f"Média: {resultado}")
