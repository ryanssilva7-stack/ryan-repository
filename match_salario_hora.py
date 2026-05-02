import os
os.system("cls")
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init(autoreset=True)

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

# definições
def valor(d, nome, sb):
    # cálculo
    horas_trabalhadas = d * 8
    valor_da_hora = (sb / 30) / 8
    reais_por_hora = horas_trabalhadas * valor_da_hora
    valor_total_reais = f'{reais_por_hora:.2f}'.replace(".",",")
    print(f"Salário do(a) funcionário(a) {nome}: {F.LG}R${RESET}{F.G}{valor_total_reais}")


# dados
print(f"{F.B}{BRIGHT}===== Solicitando Dados =====")
salario_bruto = float(input(f"Valor do salário bruto: {F.LG}R$"))
nome = input(f"{RESET}Nome do funcionário: {F.LY}")
dias = int(input(f"{RESET}Digite quantos dias foram trabalhados no mês: {F.LM}"))

# resultado
os.system("cls")
print(f"{F.B}===== EXibindo Dados =====")
valor(dias, nome, salario_bruto)
