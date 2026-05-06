import os
from colorama import Fore, Back, Style, init
from dataclasses import dataclass
import time

# Initialize colorama
init(autoreset = True)

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Funcionarios:
    nome: str
    email: str
    telefone: str

    def dados_funcionario(self):
        print(f"==== Exibindo dados do funcionário ====")
        print(f"Funcionário(a): {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Nº de telefone do funcionário: \n{self.telefone}\n")

    def dados_funcionarios(self, numeros):
        print(f"==== Exibindo dados do {numeros+1}º funcionário ====")
        print(f"Funcionário(a): {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Nº de telefone do funcionário: \n{self.telefone}\n")


armazenamento_funcionarios = []
count = 0

print("==== Solicitando dados ====")
while True:
    count += 1
    while True:
        if count == 1:
            saida = input("\nDeseja adicionar um funcionário? \n").lower()
        else:
            saida = input("\nDeseja adicionar outro funcionário? \n").lower()

        if saida in ["sim", "não", "s", "n"]:
            os.system("cls" if os.name == "nt" else "clear")
            break

    if saida in ["não", "n"]:
        break

    funcionario = Funcionarios(
        nome = input("Digite o nome do funcionário: ").title(),
        email = input("Digite o e-mail: "),
        telefone = input("Digite o telefone: ")
                            )
    armazenamento_funcionarios.append(funcionario)

with open('dados_funcionarios.txt', 'a', encoding='utf-8') as arquivo_funcionarios:
    for funcionario in armazenamento_funcionarios:
        arquivo_funcionarios.write(f'{funcionario.nome}, {funcionario.email}, {funcionario.telefone}\n')

print('Arquivo salvo com sucesso!')

os.system("cls" if os.name == "nt" else "clear")

if len(armazenamento_funcionarios) > 1:
    for i in range(len(armazenamento_funcionarios)):
        armazenamento_funcionarios[i].dados_funcionarios(i)
else:
    for i in range(len(armazenamento_funcionarios)):
        armazenamento_funcionarios[i].dados_funcionario()
