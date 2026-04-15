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
hora_inicial = int(input(f"{F.LR}Digite a hora inicial:{RESET} "))
minuto_inicial = int(input(f"{F.LR}Digite o minuto incial:{RESET} "))
hora_final = int(input(f"{F.LR}Digite a hora final:{RESET} "))
minuto_final = int(input(f"{F.LR}Digite o minuto final:{RESET} "))

# processamento
tempo_inicial = hora_inicial * 60 + minuto_inicial

tempo_final = hora_final * 60 + minuto_final

tempo_total =  tempo_final - tempo_inicial


if tempo_total < 0:
    tempo_total += 24*60

segundos = 0

minutos = tempo_total % 60

horas = tempo_total // 60

# saida
os.system("cls")
print(f"\n{F.LB}==== Resultado ===={RESET}")
print(f"{F.C}Horário inicialização do evento:{RESET} {hora_inicial:02d}:{minuto_inicial:02d}")
print(f"{F.LC}Horário finalização do evento:{RESET} {hora_final:02d}:{minuto_final:02d}")
print(f"\n{F.LY}Duração total do evento em minutos:{RESET} {tempo_total} minutos.")
print(f"{F.LM}Em horas:{RESET} {horas:02d}:{minutos:02d}:{segundos:02d}")
