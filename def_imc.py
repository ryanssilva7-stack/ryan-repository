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

# definições de funções
def calculo_do_imc (p, a):
    imc = p / (a * 2)
    return imc



def classificação (imc):
    if imc < 18.5:
        return f"{F.R}Abaixo do peso.\n{F.W}Consulte um nutricionista para orientação.{RESET}"
    
    elif 18.5 <= imc < 25:
        return f"{F.C}Peso normal.\n{F.W}Mantenha hábitos saudáveis.{RESET}"

    elif 25 <= imc < 30:
        return f"{F.R}sobrepeso.\n{F.W}Considere uma dieta balanceada e atividade física.{RESET}"

    elif 30 <= imc < 35:
        return f"{F.LR}Obesidade grau I.\n{F.W}Procure orientação de um profissional de saúde.{RESET}"

    elif 35 <= imc < 40:
        return f"{F.LR}Obesidade grau II.\n{F.W}Consulte um médico para avalição e orientação.{RESET}"

    elif 40 <= imc:
        return f"{F.LR}Obesidade grau III.\n{F.W}Busque assistênicia médica imediatamente.{RESET}"



# dados
print(f"{F.LB}==== Solicitando dados ==={RESET}")
peso = float(input(f"{F.LY}Digite o peso: {RESET}"))
altura =float(input(f"{F.M}Digite o altura: {RESET}"))

# processo
imc = calculo_do_imc(peso, altura)
classificação = classificação(imc)

# saida
os.system("cls")
print(f"\n{F.LC}==== Exibindo dados ==={RESET}")
print(f"{F.LB}Dados:\n{F.LY}Peso:{RESET} {peso}Kg\n{F.LY}Altura:{RESET} {altura}m")
print(f"\n{F.LM}Índice de massa corporal (IMC):{RESET} {imc:.2f}")
print(f"{F.LG}Classificado(a) como:{RESET} {classificação}" )