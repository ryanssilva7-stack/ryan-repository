import os
os.system("cls")
from dataclasses import dataclass

# definindo uma classe
@dataclass
class Endereco:
    logradouro: str
    numero: str


@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        os.system("cls")
        print("==== Exibindo dados do cliente ====")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")

print("==== Solicitando dados do cliente ====")
cliente = Cliente(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    endereco = Endereco(
        logradouro = input("Digite seu endereço: "),
        numero = input("Digite o número do seu endereço: ")
    )
)

cliente.mostrar_dados()