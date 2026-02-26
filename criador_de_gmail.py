import os
os.system("cls")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
empresa = input("Digite o nome da sua empresa: ")


soma = (nome+"."+sobrenome+"@"+empresa+".com")

print("\n===Dados===")
print(f"Gmail: {soma.lower()}")
