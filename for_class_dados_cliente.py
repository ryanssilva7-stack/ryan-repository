import os
os.system("cls")
from dataclasses import dataclass

# definindo uma classe
@dataclass
class Cliente:
    nome: str
    idade: int
    peso: float
    altura: float
    
    def dados(self):
        print("==== Exibindo dados do cliente ====")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso}KG")
        print(f"Altura: {self.altura} metros\n")

clientes = []
for i in range(2):
    print("\n==== Solicitando dados do cliente ====")
    cliente = Cliente(
        nome = input("Digite seu nome: ").title(),
        idade = int(input("Idigte sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
                       )
    clientes.append(cliente)

os.system("cls")
for i in range(2):
    clientes[i].dados()
