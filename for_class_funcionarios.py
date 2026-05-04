import os
from dataclasses import dataclass
os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Funcionarios:
    nome: str
    email: int
    telefone: str

    def dados_funcionarios(self, numeros):
        print(f"==== Exibindo dados do {numeros+1}º funcionário ====")
        print(f"Funcionário(a): {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Nº de telefone do funcionário: \n{self.telefone}\n")


armazenamento_funcionarios = []
quantidade_fucnionarios = 3

print("==== Solicitando dados ====")
for i in range(quantidade_fucnionarios):
    funcionario = Funcionarios(
        nome = input("Digite o nome do funcionário: ").title(),
        email = input("Digite o e-mail: "),
        telefone = input("Digite o telefone: ")
                            )
    armazenamento_funcionarios.append(funcionario)

os.system("cls" if os.name == "nt" else "clear")

for i in range(quantidade_fucnionarios):
    armazenamento_funcionarios[i].dados_funcionarios(i)

