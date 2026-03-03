import os
os.system("cls")

# entrada
nome = input("Digite seu nome: ")
codigo = int(input("Código:"))
print(f"\nOlá, senhor {nome}, por favor, preencha o campo com os dados necessários.\n")
ano_de_nascimento = int(input("digite o ano do seu nascimento:"))
tt = int(input("Digite seu tempo de trabalho (em anos):"))

# processo
idade = (2026-ano_de_nascimento)
print("\n---Dados---\n")
print(f"Nome: {nome}")
print(f"Código:{codigo}")
print(f"Idade:{idade} anos.")
print(f"\nTempo de tarablho:{tt} anos.")

if idade >= 65 or tt >= 30 :
    print("\nRequerer aposentadoria.\n")
else: 
    print("\nNão requerer aposentadoria.\n")

# saída
