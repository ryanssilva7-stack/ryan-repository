import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self, numero):
        print(f"===== {numero+1}ª empresa =====")
        print(f"Nome da empresa: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Telefone: {self.telefone}\n")

lista_empresas = []

with open('contato_empresas.csv', 'r') as arquivo_empresa:
    for linha in arquivo_empresa:
        nome, cnpj, telefone = linha.strip().split(',')
        lista_empresas.append(Empresa(
            nome=nome, 
            cnpj=cnpj, 
            telefone=telefone
            ))

for i, empresa in enumerate(lista_empresas):
    empresa.mostrar_dados(i)