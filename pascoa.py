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
ano = int(input(f"{F.LC}Digite o ano:{RESET} "))




# processamento
# a
var_a = ano % 19

# b
var_b = ano // 100

# c
var_c = ano % 100

# d
var_d = var_b // 4

# e
var_e = var_b % 4

# f
var_f = (var_b + 8) // 25

# g
var_g = (var_b - var_f + 1) // 3

# h
var_h = (19 * var_a + var_b - var_d - var_g + 15)

# i
var_i = var_c // 4

# k
var_k = var_c % 4

# l
var_l

# m


# saida