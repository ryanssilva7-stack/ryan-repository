import os
from colorama import init, Fore
os.system("cls")

# Criando um vetor
vetor_notas = []
quantidade_de_notas = 4
# soma = 0

#Adcionando notas
for i in range(quantidade_de_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)
    # soma += nota
media = sum(vetor_notas) / quantidade_de_notas
# media = soma / quantidade_de_notas

# limpar terminal
os.system("cls")

# Exibindo as notas informadas
print("=== Notas informadas ===")
for i in range(quantidade_de_notas):
    print(f"{i+1}ª nota: {vetor_notas[i]}")

print("\n----- Resultados -----")
print(f"|Média: {media:.1f}")

if media >= 7:
    print("| Aprovado\n")
elif media < 7:
    print("| Recuperação\n")
elif media < 5:
    print("| Reprovado\n")