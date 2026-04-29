import os
os.system("cls")
from dataclasses import dataclass

# definindo uma classe
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

print("==== Solicitando dados do cliente ====")
cliente = Cliente(
    nome = input("Nome: "),
    email = input("E-mail: ").lower(),
    telefone = input("Telefone: ")
                   )

os.system("cls")
print("==== Exibindo dados do cliente ====")
print(f"Nome: {cliente.nome}")
print(f"E-mail: {cliente.email}")
print(f"Nº de telefone: {cliente.telefone}")
