import os 
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Empresa():
    nome: str
    cnpj: str
    telefone: str

quanti_empresas = 3
lista_empresas = []

print("=== Coletando dados da empresa ===")
for i in range(quanti_empresas):
    empresa = Empresa(
        nome = input("Digite o nome da empresa: ").title(),
        cnpj = input("Digite o cnpj da empresa: "),
        telefone = input("Digite o telefone da empresa: ")
                   )
    lista_empresas.append(empresa)

with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo_empresa:
        for empresa in lista_empresas:
            arquivo_empresa.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n")
print("Dados salvos com sucesso!")