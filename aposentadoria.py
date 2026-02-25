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
print(f"Tempo de tarablho:{tt} anos.")

if idade >= 65 and tt >= 30 :
    print("\nRequerer aposentadoria.")
else: 
    print("\nNão requerer aposentadoria.")
# saída