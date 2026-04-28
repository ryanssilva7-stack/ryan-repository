import os
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init(autoreset=True)

# Atalhos de Estilo
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT
DIM = Style.DIM

# Atalhos de Cores de Fonte (Texto)
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

os.system("cls")
# definições
def limpar_tela():
    os.system("cls")

def depositar():
    global saldo
    limpar_tela()
    print(f"{F.C} === DEPÓSITO DO BANCO CALOTE === {Style.RESET_ALL}")

    if len(usuario) == 0:
        print(f"{F.R} BLOQUEADO: Você prescisa criar um usuário antes de depósitar! ")
        input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
    else:
        try:
            valor = float(input("Digite  o valor para depósito: R$ "))
            if valor > 0:
                saldo += valor
                historico_depositos.append(valor)
                print(f"\n {F.G} Depósito de R${reais(valor)} realizado com sucesso!")
            else:
                print(f"\n {F.R} Valor inválido!")

        except ValueError:
            print(f"\n {F.R} Erro: {RESET} para voltar...")

        input (f"\nPressione {F.Y} Enter {RESET} para voltar...")


def ver_saldo():
    limpar_tela()
    if len(usuario) == 0:
        print(f"{F.R} BLOQUEADO: Você prescisa criar um usuário antes de ver o saldo! ")
        input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
    else:
        print(f"{F.C} === EXTRATO E SALDO DO BANCO CALOTE === {RESET}")

        print(f"{F.R} Histórico do Depósito:")
        if not historico_depositos:
            print(f"{F.R} Nenhum Depósito realizado.")
        else:
            for i, valor in enumerate(historico_depositos, 1):
                print(f"{F.W} {i}° Depósito: {F.G} R${reais(valor)}")

        print(f"\n{F.LR} Histórico do Saque:")
        if not historico_saque:
            print(f"{F.R} Nenhum Saque realizado.")
        else:
            for i, valor_saque in enumerate(historico_saque, 1):
                print(f"{F.W} {i}° Saque: {F.R} R$-{reais(valor_saque)}")
            print ("-" * 25)
            print(f"Saldo Total: {F.Y} R${reais(saldo)}")
        input(f"\nPressione {F.Y} Enter {RESET} para voltar...")

def reais(real):
    return f'{real:.2f}'.replace(".", ",")

def sair():
    limpar_tela()
    print(f"{F.M} Saindo do Banco Calote...até logo! {RESET}")
    time.sleep(3)


# dados
saldo = 0.0
historico_depositos = []
historico_saque = []
usuario = []

# processamento
while True:
    limpar_tela()
    print(f"""{F.LB}   ================ BANCO CALOTE  ==============={RESET} 
    {F.LC}Opção 1  -  Criar usuário
    Opção 2  -  Sacar dinheiro
    Opção 3  -  Depositar dinheiro
    Opção 4  -  Saldo da conta
    Opção 5  -  Sair


    """)
    while True:
        try:
            escolha = int(input("Escolha uma opção por meio dos códigos: "))
        except ValueError:
            print(f"{F.R}Digite apenas números inteiros.\n")
            input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
        else:
            break
    match escolha:
        case 1:
            limpar_tela()
            if not usuario:
                print(f"{F.R}Usuário não cadastrado")
                nome = str(input("Crie um nome do usuário: "))
                usuario.append(nome)
                while True:
                    try:
                        idade = int(input("Digite sua idade: "))
                    except ValueError:
                        print(f"{F.R}Digite apenas números inteiros.\n")
                        input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
                    else:
                        break
                senha_do_usuario = input("Crie uma senha: ")
            else:
                limpar_tela()
                print("==== Dados ====")
                print(f"Usuário: {nome} \nIdade: {idade}")
                input(f"\nPressione {F.Y} Enter {RESET} para voltar...")

        case 2:
            limpar_tela()
            if not saldo or not usuario:
                print(f"{F.R}BLOQUEADO: Deposite um valor ou crie um usuário primeiro para sacar.")
                input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
            else:
                while True:
                    try:
                        sacar = float(input("Digite quantos reais você deseja retirar: "))
                    except ValueError:
                        print("Digite apenas números inteiros.\n")
                        input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
                    else:
                        if sacar > saldo:
                            print("Erro. \nSaldo insuficiente para realizar o saque.")
                            input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
                            break
                        elif sacar <= 0:
                            print("Erro. \nSaque deve ser maior que 0.")
                            input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
                            break
                        else:
                            senha = input("Digite sua senha: ")
                            if senha == senha_do_usuario:
                                saldo -= sacar
                                historico_saque.append(sacar)
                                print("Saque realizado com sucesso.")
                                input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
                                break
                            else:
                                print(f"{F.R}BLOQUEADO: Senha incorreta.")
                                input(f"\nPressione {F.Y} Enter {RESET} para voltar...")
                                break
        case 3:
            depositar ()

        case 4:
            ver_saldo ()

        case 5:
            sair()
            break

        case _:
            print(f"{F.R}Não é uma opção.")
            input(f"\nPressione {F.Y} Enter {RESET} para voltar...")