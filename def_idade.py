import os
from datetime import date


os.system("cls")

def ano_idade(a):
    ano_atual = date.today().year
    i = ano_atual - a
    return i

ano_de_nascimento =int(input("digite o ano de seu nascimento:\n"))

idade = ano_idade(ano_de_nascimento)

print(f"O usuário possui {idade} anos de idade.")
