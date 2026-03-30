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
armazenamento_de_numeros = []
quantidade_de_numeros = 5
negativo = 0

# processo
for i in range(quantidade_de_numeros):
    numero = int(input(f"{F.LM}Digite o {i+1}º número:{RESET} "))

    if numero < 0:
        negativo += 1
    elif numero > 0:
        armazenamento_de_numeros.append(numero)
        soma = sum(armazenamento_de_numeros)

print(f"\n {F.LB}===== Resultado ====={RESET}")
print(f"{F.Y}Soma:{RESET} {soma}")

if negativo == 0:
    print(f"{F.LG}Não há números negativos.{RESET}")
elif negativo == 1:
    print(f"{F.LG}Há {RESET}{negativo}{F.LG} número negativo.{RESET}")
elif negativo > 1:
    print(f"{F.LG}Há {RESET}{negativo}{F.LG} números negativos.{RESET}")