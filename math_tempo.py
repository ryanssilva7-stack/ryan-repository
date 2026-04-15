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
print(f"{F.LB}==== conversão de segundos para horas ===={RESET}")
tempo = int(input(f"{F.LC}Digite um tempo em segundos: {RESET}"))

# processamento
minutos = (tempo % 3600) // 60
horas = tempo // 3600
segundos = tempo % 60

time.sleep(1)
# saida
os.system("cls")
print(f"{F.LB}=== Processando ==={RESET}")
time.sleep(3)

os.system("cls")
print(f"{F.LB}==== Resultado ===={RESET}")
print(f"{F.LC}{tempo} segundos equivalem à:\n{F.LW}{horas:02d}{F.K}:{F.LW}{minutos:02d}{F.K}:{F.LW}{segundos:02d}{RESET}")