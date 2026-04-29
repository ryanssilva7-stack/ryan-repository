import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        os.system("cls")
        print("=== dados ===")
        print(f"""Fornecedor: {self.nome}
E-mail: {self.email})
Teleforne: {self.telefone}
Endereço: {self.endereco}""")

fornecedor = Fornecedor(
    nome = input("Digite seu  nome: "),
    email = input("Digite seu  e-mail: "),
    telefone = input("Digite seu  telefone: "),
    endereco = input("Digite seu  endereço: ")
)

fornecedor.mostrar_dados()