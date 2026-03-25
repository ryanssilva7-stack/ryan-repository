import os
from colorama import init, Fore
os.system("cls")

# Criando um vetor
vetor_notas = []
quantidade_de_notas = 3

#Adcionando notas
for i in range(quantidade_de_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)

# Exibindo as notas informadas
for i in range(3):
    print(f"{i+1}ª nota: {vetor_notas[i]}")
