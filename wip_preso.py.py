import os
import time
from dataclasses import dataclass

# definições
def limpar_terminal():
    os.system("cls")


def enter():
    input("\nPressione ENTER para continuar.\n")


# classes
@dataclass
class Prisioneiro():
    identificacao: int
    nome: str
    idade: int
    infracao: str
    tempo_preso: int
    
    def dados(self):
        print(f"Nº de idnetificação {self.identificacao} \nNome: {self.nome}  Idade: {self.idade}")
        print(f"Motivo da condenação: {self.infracao} \nTempo de prisão: {self.tempo_preso}")


# dados
arquivando_presos = []
lista_de_presos = []

nome_arquivo = 'Arquivo_dos_presos.txt'

# processo
while True:
    print("""
===== Sistema de prisão =====
Códigos  |  Ações
   1         Cadastrar prisioneiro
   2         Olhar registro dos prisioneiros
   3         Sair

""")
    try:
        escolha = int(input("Escolha uma ação por meio de códigos: "))
    except ValueError:
        print("Erro!! \Digite apenas número inteiro.")

    match escolha:
        case 1:
            while True:
                try:
                    prisioneiro = Prisioneiro(
                    identificacao = int(input("Digite o númerto de identificação: ")),
                    nome = input("Digite o nome: "),
                    idade = int(input("Digite a idade: ")),
                    infracao = input("Digite o motivo da prisão: "),
                    tempo_preso = int(input("Digite o tempo de cadeia: "))
                                        )
                except ValueError:
                    print("Erro!! \Digite apenas número inteiro.")
                else:
                    break

            arquivando_presos.append(prisioneiro)
            with open (nome_arquivo, 'a', encoding='utf-8') as arquivo_presos:
                for prisioneiros in arquivando_presos:
                    arquivo_presos.write(f'{prisioneiros.identificacao}, {prisioneiros.nome}, {prisioneiros.idade}, {prisioneiros.infracao}, {prisioneiros.tempo_preso}')
        
        case 2:
            with open (nome_arquivo, 'r', encoding='utf-8') as arquivo_presos:
                for lista in arquivo_presos:
                    identificacao, nome, idade, infracao, tempo_preso = lista.strip().split(', ')
                    lista_de_presos.append(Prisioneiro
                        identificacao = identificacao,
                        nome = nome,
                        idade = idade,
                        infracao = infracao,
                        tempo_preso = tempo_preso
                                           )
                    
            for i in range(len(lista_de_presos)):
                lista_de_presos[i-1].dados()
        # case 3:

        case _:
            print("Código incorreto!")