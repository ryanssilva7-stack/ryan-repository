import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionarios():
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self, posicao):
        print(f"{posicao+1}º funcionário")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}\n")

armazenamento_funcionarios = []

with open ('dados_funcionarios.txt', 'r') as arquivo_funcionarios:
    for lista in arquivo_funcionarios:
        nome, email, telefone = lista.strip().split(',')
        armazenamento_funcionarios.append(Funcionarios(
            nome = nome,
             email = email,
             telefone = telefone
        ))

for i, funcionarios in enumerate(armazenamento_funcionarios):
    funcionarios.mostrar_dados(i)