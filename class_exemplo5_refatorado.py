import os
os.system("cls")
from dataclasses import dataclass

def limpar_terminal():
    os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    def mostrar_dados(self):
        limpar_terminal()
        print("===== Exibindo dados do paciente =====")
        print(f""" Paciente: {self.nome}
 {self.idade} anos  |  {self.peso}KG  |  {self.altura} Metros""")
        print("="*38)

limpar_terminal()
print("===== Solicitando dados do paciente =====")
paciente = Paciente(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: "))
)

paciente.mostrar_dados()