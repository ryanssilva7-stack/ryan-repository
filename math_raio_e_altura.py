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

# dados
print(f"{F.LC}Sobre o cilindro, informe:{RESET}")
raio = int(input(f"{F.LM}O raio do cilindro: {RESET}"))
altura = int(input(f"{F.LM}A altura do cilindro: {RESET}"))
pi = 3.14159

# processamento
area_da_base = pi * (raio * raio)
volume = pi * (raio * raio) * altura

# saida
print(f"{F.LC}==== Resultado ===={RESET}")
print(f"{F.M}Área da base do cilindro:{RESET} {area_da_base:.2f}")
print(f"{F.M}Volume do cilindro:{RESET} {volume:.2f}")