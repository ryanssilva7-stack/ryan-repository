import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str


fornecedor = Fornecedor(
    nome = input("Digite seu  nome: "),
    email = input("Digite seu  e-mail: "),
    telefone = input("Digite seu  telefone: "),
    endereco = input("Digite seu  endereço: ")
)

print("=== dados ===")
print(f"""Fornecedor: {fornecedor.nome}
E-mail: {fornecedor.email})
Teleforne: {fornecedor.telefone}
Endereço: {fornecedor.endereco}""")