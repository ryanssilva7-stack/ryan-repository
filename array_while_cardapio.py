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
valor_total = 0
contador = 0
pratos_solicitados = []
print(f"""
    {F.LC}========== Cardápio ==========
     Código |  Prato    |   Valor
    ------------------------------ 
       1      Picanha     R$ 25,00
       2      Lasanha     R$ 20,00
       3     Strogonoff   R$ 18,00
       4   Bife acebolado R$ 15,00
       5    Pão com ovo   R$  5,00
    ------------------------------{RESET}
""")

# processo
while True:
    codigo = int(input(f"{F.R}Digite um código:{RESET} "))

    match codigo:
        case 1:
            prato = "Picanha"
            valor = 25
            contador += 1
        case 2:
             prato = "Lasanha"
             valor = 20
             contador += 1
        case 3:
            prato = "Strogonoff"
            valor = 18
            contador += 1
        case 4:
             prato = "Bife acebolado"
             valor = 15
             contador += 1
        case 5:
             prato = "Pão com ovo"
             valor = 5
             contador += 1
        case _:
            print("\nNão é uma opção válida\n")
            time.sleep(0.75)
            continue

    valor_total += valor
    pratos_solicitados.append(prato)

    repeat = input(f"\n{F.G}Deseja solicitar outro prato?{RESET} (S/N): ").upper()
    
    if repeat == "N":
        break

    if repeat in ["S", "N"]:
        continue
    else:
        print(f"{F.R}Resposta inválida! Digite apenas S ou N.{RESET}")

# resultaado
os.system("cls")

print(f"{F.LG}=== Carregando conta ==={RESET}")
time.sleep(2)
os.system("cls")

print(f"{F.LC}==== Conta ===={RESET}\n")

if contador == 1:
    print(f"{F.LY}Prato Solicitado:{RESET} {', '.join(pratos_solicitados)}.")
else:
    print(f"{F.LY}Pratos Solicitados:{RESET} {', '.join(pratos_solicitados)}.")
print(f"{F.LM}Valor a pagar:{RESET} R${valor_total:.0f},00")