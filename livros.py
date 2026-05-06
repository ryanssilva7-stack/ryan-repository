import os
from dataclasses import dataclass

# classes
@dataclass
class Livros():
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self, n):
        print(f"==== Lista de livros ====")
        print(f"Nome: {self.nome} \nAutor: {self.autor} \nCategoria: {self.categoria} \nPreço: R${self.preco}\n")


# definções
def limpar_terminal():
     os.system("cls" if os.name == 'nt' else "clear")

def enter():
     press = input("\nPressione ENTER para proseguir.\n")

# dados
livros_no_arquivo = []
lista_livros = []
quanti_livros = 3

# processo
while True:
    limpar_terminal()
    print("""----- Sistema de Cadastro -----
    código  |  ações
      1         adcionar livros
      2         listar livros
      3         sair
                  """)
    try:
        escolha = int(input("Digite um código: "))
    except ValueError:
        print("\nErro!!! \nDigite apenas o valor numérico do código.")
        enter()
    else:
        match escolha:
            case 1:
                limpar_terminal()
                print("Sobre o livro:")
                livro_comprar = Livros(
                    nome= input("Digite o nome do livro: ").title(),
                    autor= input("Digite o nome do autor: ").title(),
                    categoria= input("Digite a categoria: ").title(),
                    preco= float(input("Digite o preço do livro: "))
                    )
                livros_no_arquivo.append(livro_comprar)

                with open('catalogo_livros.csv', 'a', encoding='utf-8') as arquivo_livros:
                        arquivo_livros.write(f'{livro_comprar.nome}, {livro_comprar.autor}, {livro_comprar.categoria}, {livro_comprar.preco}\n')
                print("Livro salvo com sucesso!")
                enter()

            case 2:
                limpar_terminal()
                try:
                    with open('catalogo_livros.csv', 'r', encoding='utf-8') as arquivo_livros:
                         for lista in arquivo_livros:
                            nome, autor, categoria, preco = lista.strip().split(', ')
                            lista_livros.append(Livros(
                              nome=nome,
                              autor=autor,
                              categoria=categoria,
                              preco=preco 
                              ))
                    for i, livros in enumerate(lista_livros):
                        livros.mostrar_dados(i)
                except FileNotFoundError:
                    print("Arquivo não encontrado.")
                    enter()
                else:
                    enter()

            case 3:
                limpar_terminal()
                print("--- Desligando terminal ---")
                break
            case _:
                limpar_terminal()
                print("Opção inválida.")
                enter()