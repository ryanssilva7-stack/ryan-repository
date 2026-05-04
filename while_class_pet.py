import os
from colorama import Fore, Back, Style, init
from dataclasses import dataclass

# Initialize colorama
init(autoreset = True)

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Pets:
    nome: str
    idade: int
    raca: str

    def dados_pets(self, numeros):
        print(f"==== Exibindo dados do {numeros+1}º Pet ====")
        print(f"Nome do(a) pet: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça do pet: {self.raca}\n")


armazenamento_pets = []
count = 0

print("==== Solicitando dados ====")
while True:
    count += 1
    if count >= 3:
        while True:
            saida = input("\nDeseja adicionar outro pet? \n").lower()

            if saida in ["sim", "não", "s", "n"]:
                break

        if saida in ["não", "n"]:
            break

    pet = Pets(
        nome = input("\nDigite o nome do pet: ").title(),
        idade = int(input("Digite a idade: ")),
        raca = input("Digite a raça: ").title()
                            )
    armazenamento_pets.append(pet)

os.system("cls" if os.name == "nt" else "clear")

for i in range(len(armazenamento_pets)):
    armazenamento_pets[i].dados_pets(i)
