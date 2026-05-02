import os
import time
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init()

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
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# dados
limpar_terminal()
palavra = "sinuoso".lower()
letras_usadas = []
tentativas = 8

# processo/jogo
while True:
    # fim de jogo: caso perca
    if tentativas == 0:
        limpar_terminal()
        print(f"Você perdeu, a palavra era {palavra}.")
        break

    print(f"Você possui {tentativas} tentativas.")

    while True:
        letra = input("\nLetra: ").lower()
        if letra in letras_usadas:
            print("Você ja escreveu essa letra.")
        else:
            letras_usadas.append(letra)
            break
    resultado = ""

     

    for l in palavra:
        resultado += l if l in letras_usadas else "_"
    print(resultado)
    print("")

    if not letra in palavra:
        print("Letra incorreta.\n")
        tentativas -= 1
    
    # fim de jogo: caso ganhe
    if not "_" in resultado:
        limpar_terminal()
        print(f"Você venceu! \nA palavra era {palavra}!")
        break