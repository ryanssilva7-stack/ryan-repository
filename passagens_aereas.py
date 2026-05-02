import os
from colorama import Fore, Back, Style, init
import time
from dataclasses import dataclass

# Initialize colorama
init()

# Atalhos de Estilo
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT
DIM = Style.DIM

# Classes
class F:
    R   = Fore.RED
    G   = Fore.GREEN
    B   = Fore.BLUE
    Y   = Fore.YELLOW
    M   = Fore.MAGENTA
    C   = Fore.CYAN
    W   = Fore.WHITE
    K   = Fore.BLACK
    LR  = Fore.LIGHTRED_EX
    LG  = Fore.LIGHTGREEN_EX
    LB  = Fore.LIGHTBLUE_EX
    LY  = Fore.LIGHTYELLOW_EX
    LM  = Fore.LIGHTMAGENTA_EX
    LC  = Fore.LIGHTCYAN_EX
    LW  = Fore.LIGHTWHITE_EX

@dataclass
class Reservas:
    aviao: int
    nome: str
    
    def mensagem(self):
            print(f"""Passageiro: {self.nome}      Avião: Nº {self.aviao}\n""")


# definições
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def enter():
    enter = input("\nPressione ENTER para continuar\n")


def erro():
    print("Erro. \nDigite apenas números.")
    enter()


def logo():
    print("""
         ~~~~ Sistema ~~~~
      ~~~~ SWEET  FLIGHT ~~~~
          """)


def cadastro_avioes():
    limpar_terminal()
    while True:
        if not avioes_cadastrados:
            print("Aviões não cadastrados")
        else:
            print("Aviões cadastrados:")
            for i in range(4):
                print(f"Avião {i+1}: Nº de identificação: {avioes_cadastrados[i]}")

        opcao = input("\nDeseja cadastrar novos aviões? : ").lower()
        if opcao in ["sim", "não"]:
            limpar_terminal()
            break
        else:
            print("\nDigite apenas sim ou não.")
            enter()
            limpar_terminal()

    if opcao == "sim":
        limpar_terminal()
        for i in range(4):
            while True:
                try:
                    cadastracao_avioes = int(input(f"Digite o numero de identificação do {i+1}º avião: "))
                except ValueError:
                    erro()
                    limpar_terminal()
                else:                       
                    if cadastracao_avioes in avioes_cadastrados:
                        print("\nErro. \nDois aviões não devem possuir o mesmo Nº de identificação.")
                        enter()
                        limpar_terminal()
                    else:
                        avioes_cadastrados.append(cadastracao_avioes)
                        break
        print("\nAviões cadastrados com sucesso!")
        enter()                      


def cadastrar_assento():
    limpar_terminal()
    if not avioes_cadastrados:
        print("Realize o cadastro dos aviões primeiro.")
        enter()
    else:
        while True:
            if not quantidade_de_assentos:
                print("Nenhum assento foi cadastrado ainda.")
            else:
                for i in range(4):
                    print(f"Avião {avioes_cadastrados[i]}: Assenstos: {quantidade_de_assentos[i]}")

            opcao = input("\nDeseja cadastrar novos assentos dos aviões? : ").lower()
            if opcao in ["sim", "não"]:
                break
            else:
                print("\nDigite apenas sim ou não.")  
                enter()
                limpar_terminal()

        if opcao == "sim":
            limpar_terminal()
            for i in range(4):
                while True:
                    try:
                        limpar_terminal()
                        assentos = int(input(f"Digite a quantidade de assentos do avião {avioes_cadastrados[i]}: "))
                    except ValueError:
                        erro()
                    else:
                        if assentos > 20:
                            print("Limite de assentos: 20 \nTente Novamente.\n")
                            enter()
                        elif assentos < 0:
                            print("Erro. \nImpossível colocar números negativos.")
                            enter()
                        else:
                            quantidade_de_assentos.append(assentos)
                            break
            print("\nAssentos cadastrados com sucesso!")
            enter()
                

def reservar_passagem():
    limpar_terminal()
    if not avioes_cadastrados or not quantidade_de_assentos:
        print("Realize os cadastros das opções 1 e 2 primeiro.")
        enter()
    else:
         while True:   
            if len(passagens_registradas) == 20:
                print("Limite excedido de reservas. \nTente novamente mais tarde.")
                enter()
                break
            else:
                while True:
                    try:
                        escolha_aviao = int(input("Digite o ID do avião: "))
                    except ValueError:
                        erro()
                        limpar_terminal()
                    else:
                        break

                if escolha_aviao in avioes_cadastrados:
                    posicao = avioes_cadastrados.index(escolha_aviao)
                    if quantidade_de_assentos[posicao] <= 0:
                        print("\nNão há assentos disponíveis para este avião.")
                        enter()
                        break
    
                    else:
                        limpar_terminal()
                        print(f"\nAvião {posicao+1}: \nNº de identificação: {escolha_aviao} \nNúmero de assentos: {quantidade_de_assentos[posicao]}")
                        time.sleep(1)

                        while True:
                            passageiro = input("\nDigite o nome do passageiro: ").title()
                            if passageiro == "":
                                print("\nDigite um nome.")
                                enter()
                                limpar_terminal()
                            else:
                                break
                        reserva = Reservas(
                            aviao = avioes_cadastrados[posicao],
                            nome =  passageiro
                        )
                        
                        quantidade_de_assentos[posicao] -= 1                        
                        passagens_registradas.append(reserva)
                        print("\nPassagem reservada com sucesso!")
                        enter()
                        break
                        
                else:
                    print("\nNúmero de identificação incorreto... \nTente Novamente.")
                    enter()
                    break


def consulta_aviao():
    limpar_terminal()
    if not passagens_registradas:
        print("Realize as reservas primeiro.")
        enter()
    else:
        while True:
            try:
                consulta = int(input("Digite o número de identificação do avião: "))
            except ValueError:
                erro()
                limpar_terminal()
            else:
                break
        
        limpar_terminal()
        if consulta in avioes_cadastrados:
            encontrado = False
            for procura in passagens_registradas:
                if procura.aviao == consulta:
                    procura.mensagem()
                    print("-" * 35) 
                    encontrado = True
            if encontrado == False:
                print("\nEsse avião não possui registros de reservas.")
                enter()
            else:
                enter()
        else:
            print("Esse avião não existe.")
            enter()


def consulta_passageiro():
    limpar_terminal()
    if not passagens_registradas:
        print("Realize as reservas primeiro.")
        enter()
    else:
        consulta = input("Digite o nome do passageiro: ").title()
        encontrado = False
        count = 1
        limpar_terminal()

        for procura in passagens_registradas:
            if procura.nome == consulta:
                if count == 1:
                    print(f"Passageiro {consulta} encontrado nos aviões:")
                encontrado = True
                print(f"Avião : {procura.aviao}")
                count += 1

        if encontrado == False:
            print("Esse passageiro não possui registros de reservas.")
            enter()
        else:
            print("-" * 36)
            enter() 


# dados
avioes_cadastrados = []
quantidade_de_assentos = []
passagens_registradas = []

# processamento de sistema da Sweet Fight
while True:
    limpar_terminal()
    logo()
    print(f""" Código       função
   1       Acrescentar os número dos aviões
   2       Acrescentar assentos disponíveis de cada avião
   3       Reservar passagem aérea
   4       Realizar consulta por avião
   5       Realizar consulta por passageiro
   6       Encerrar sistema
    """)
    while True:
        try:
            escolha = int(input("Escolha uma das opções(códigos apenas): "))

        except ValueError:
            print("Não permitido Float ou String, integer(int) apenas...\n")
            enter()

        else:
            break
    
    match escolha:
        case 1:
            cadastro_avioes()

        case 2:
            cadastrar_assento()

        case 3:
            reservar_passagem()

        case 4:
            consulta_aviao()

        case 5:
            consulta_passageiro()

        case 6:
            limpar_terminal()
            logo()
            print("Desligando prgrama, volte sempre <3\n")
            time.sleep(3)
            limpar_terminal()
            break

        case _:
            limpar_terminal()
            print("\nCódigo inválido. \nTente novamente.")
            enter()
