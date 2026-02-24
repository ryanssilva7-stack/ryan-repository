import os

# limpa o terminal.
os.system("cls")

print("- Solicitando dados -")
nome = input("Digite seu nome: ")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

# calcule
media = (primeira_nota+segunda_nota) / 2

# mostre o nome e a média
print ("\n- Exibindo dados -")
print (f"Nome:, {nome}")
print (f"Média: {media}")