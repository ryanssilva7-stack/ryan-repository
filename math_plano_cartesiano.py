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
def carregamento():
    os.system("cls")
    print(f"{F.C}~~~~ Carregando informações ~~~~\n Por favor, aguarde...{RESET}")
    time.sleep(2)
    os.system("cls")


# dados
x1 = int(input(f"{F.LY}Digite a posição do 1º ponto x:{RESET} "))
y1 = int(input(f"{F.LY}Digite a posição do 1º ponto y:{RESET} "))
x2 = int(input(f"\n{F.LY}Digite a posição do 2º ponto x:{RESET} "))
y2 = int(input(f"{F.LY}Digite a posição do 2º ponto y:{RESET} "))

carregamento()

x = int(input(f"\n{F.LY}Digite o valor de x:{RESET} "))

# processamento
carregamento()

print("\n")
if x2 - x1 == 0:
    print(f"{F.R}Erro: Não é possível calcular com x1 igual a x2 (reta vertical)...{RESET}")
    time.sleep(2)
    y = y1
    carregamento()

else:
    resultado = (y2 - y1) / (x2 - x1)
    y = y1 + (x - x1) * resultado

# saida
print(f"{F.M}==== Resultado ===={RESET}\n")
print(f"{F.B}Pontos: ({F.W}{x1}{F.B},{F.W}{y1}{F.B}); ({F.W}{x2}{F.B},{F.W}{y2}{F.B}){RESET}")
print(f"{F.Y}O valor de y é{RESET} {y:.0f}")
