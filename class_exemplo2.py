import os
os.system("cls")
from dataclasses import dataclass

# definindo uma classe
@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

@dataclass
class Funcionario:
    nome: str
    matricula: int
    email: str
    setor: str

funcionario1 = Funcionario('Rusberto',40300 , 'RusBertO@gmail.com'.lower(), 'Atendimento ao cliente')
cliente1 = Cliente('Maria', 'MarIa@gmAiL.com'.lower(), '71 99432-5576')

print("Cliente(s)")
print(f"Nome: {cliente1.nome}")
print(f"E-mail: {cliente1.email}")
print(f"Nº de telefone: {cliente1.telefone}")

print("\nFuncionários(s)")
print(f"Nome: {funcionario1.nome}")
print(f"Matricula: {funcionario1.matricula}")
print(f"E-mail: {funcionario1.email}")
print(f"Setor: {funcionario1.setor}")