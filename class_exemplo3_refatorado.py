import os
os.system("cls")
from dataclasses import dataclass

# definindo uma classe
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        os.system("cls")
        print("==== Exibindo dados do cliente ====")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Nº de telefone: {self.telefone}")

print("==== Solicitando dados do cliente ====")
cliente = Cliente(
    nome = input("Nome: "),
    email = input("E-mail: ").lower(),
    telefone = input("Telefone: ")
                   )

cliente.mostrar_dados()