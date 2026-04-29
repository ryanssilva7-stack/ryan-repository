import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int

# usando uma classe
pessoa1 = Pessoa('Alice', 30)
pessoa2 = Pessoa('Bob', 25)
pessoa3 = Pessoa('Luan', 19)

pet1 = Pet('Totó', 8)
pet2 = Pet('Lulu', 10)
pet3 = Pet('Samuel', 5)

print("Pessoa: dados")
print(f"Nome: {pessoa1.nome} \nIdade: {pessoa1.idade}")
print(f"\nNome: {pessoa2.nome} \nIdade: {pessoa2.idade}")
print(f"\nNome: {pessoa3.nome} \nIdade: {pessoa3.idade}")

print("\nPet: dados")
print(f"Nome: {pet1.nome} \nIdade: {pet1.idade}")
print(f"\nNome: {pet2.nome} \nIdade: {pet2.idade}")
print(f"\nNome: {pet3.nome} \nIdade: {pet3.idade}")