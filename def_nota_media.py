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

# dados
def soma_media(n1):
    soma = sum(n1)
    media = soma / 2
    return media

def aprovacacao(media):
    if media >= 7:
        situacao = f"Aprovado"
    else:
        situacao = f"Desaprovado"
    return situacao

quantidade_de_numeros = 2
armazenamento_de_numeros = []

# processamento
for i in range(quantidade_de_numeros):
    numero = float(input(f"{F.M}Digite um número: {F.W}"))
    armazenamento_de_numeros.append(numero)

media = soma_media(armazenamento_de_numeros)
resultado = aprovacacao(media)

# saida
os.system("cls")
print(f"{F.LC}==== Resultado ===={RESET}")
print("\n")
print(f"Média: {media}")
print(f"Situação: {resultado}")