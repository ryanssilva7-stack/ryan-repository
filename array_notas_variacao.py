import os
from colorama import init, Fore
os.system("cls")

# Criando um vetor
vetor_notas = []
quantidade_de_notas = 3

print(f"===== Adcionando {quantidade_de_notas} nota(s) =====\n")
for i in range(quantidade_de_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)

print("\n\n==== Exibindo as notas informadas ====")
for inumerar, uma_nota in enumerate(vetor_notas, start = 1):
    print(f"{inumerar}ª nota: {uma_nota}")