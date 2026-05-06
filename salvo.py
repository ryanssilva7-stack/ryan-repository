import os 
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")

# classes
@dataclass
class Empresa():
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self, numero):
        print(f"===== {numero+1}ª empresa =====")
        print(f"Nome da empresa: {self.nome}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Telefone: {self.telefone}\n")


# dados
quanti_empresas = 1
lista_empresas = []

# processo
print("=== Coletando dados da empresa ===")
for i in range(quanti_empresas):
    empresa = Empresa(
        nome = input("Digite o nome da empresa: ").title(),
        cnpj = input("Digite o cnpj da empresa: "),
        telefone = input("Digite o telefone da empresa: ")
                   )
    lista_empresas.append(empresa)

# escreve o código em um arquivo
with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo_empresa:
    for empresa in lista_empresas:
        arquivo_empresa.write(f"{empresa.nome}, {empresa.cnpj}, {empresa.telefone}\n")
    print("Dados salvos com sucesso!")

print("= Consultando arquivo =")
lista_contatos = []
with open('contato_empresas.csv', 'r', encoding = 'utf-8') as arquivo_empresa:
    for linha in arquivo_empresa:
        nome, cnpj, telefone = linha.strip().split(', ')
        lista_contatos.append(Empresa(
            nome=nome, 
            cnpj=cnpj, 
            telefone=telefone
            ))

for numero, empresa in enumerate(lista_contatos):
    empresa.mostrar_dados(numero)

print("= Fim do progama =")