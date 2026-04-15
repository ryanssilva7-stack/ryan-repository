import os
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init()

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
def acrescimo_de_valor(numero, real):
    acrescimo = 1 + numero / 100
    total = real * acrescimo 
    return total


def desconto_de_acrescimo(numero, total):
    desconto = 1 - numero / 100
    total_desconto = total * desconto
    return total_desconto


def virgula(a):
    resultado = f'{a:.2f}'.replace('.', ',')
    return resultado


# dados
valor = float(input(f"{F.LM}Digite um valor: {RESET}"))
acrescimo = int(input(f"{F.LM}Digite o valor do acrescimo: {RESET}"))
desconto = int(input(f"{F.LM}Digite o valor do desconto: {RESET}"))
reais = f"{F.G}R${RESET}"

# processamento
valor_acrescimo = acrescimo_de_valor(acrescimo, valor)
valor_desconto = desconto_de_acrescimo(desconto, valor_acrescimo)

# saida
os.system("cls")
print(f"\n{F.LY}==== Valor da Compra ===={RESET}")
print(f"{F.LB}Valor original: {reais}{virgula(valor)}")
print(f"{F.LR}Valor com acréscimo de {acrescimo}%: {reais}{virgula(valor_acrescimo)}")
print(f"{F.LC}Valor com desconto de {desconto}%: {reais}{virgula(valor_desconto)}")