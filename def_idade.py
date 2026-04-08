import os

os.system("cls")

def ano_idade(a):
    i = 2026 - a
    return i

ano_de_nascimento =int(input("digite o ano de seu nascimento:\n"))

idade = ano_idade(ano_de_nascimento)

print(f"O usuário possui {idade} anos de idade.")