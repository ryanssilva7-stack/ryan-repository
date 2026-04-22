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

# dados
print("""opções:
        Código       função
        opcao 1     Número do avião
        opcao 2     Assentos disponíveis de cada avião
        opcao 3     Reservar passagem aérea
        opcao 4     consulta por avião
        opcao 5     Realizar consulta por passageiro
        opcao 6     Encerrar sistema
""")
quantidade_de_assentos = []
avioes_selecionados = []


# processamento de sistema da Sweet Fight 
while True:
    codigo = int(input("Escolha uma opção por meio dos códigos: "))
    match codigo:
        case 1:
            while True:
                aviao = int(input("Escolha uma numeração de avião: "))

                if aviao in [1, 2, 3, 4]:
                    avioes_selecionados.append(aviao)
                    break
                else:
                    print("Número de avião inválido...")
                    print("Tente novamente.")

        case 2:
            print(""" Avião 1 
            Assentos disponíveis: 11/44
            """)
            print(""" Avião 2 
            Assentos disponíveis: 25/44

            """)
            print(""" Avião 3 
            Assentos disponíveis: 36/44

            """)
            print(""" Avião 4 
            Assentos disponíveis: 22/44
            
            """)
        case 3:
            
            match aviao:
                case 1:
                    while True:
                        assentos = int(input("Escolha quantos assentos deseja comprar: "))
                        if assentos > 11:
                            print("Erro.")
                            print("Quantidade de assentos indisponíveis.")
                        else:
                            quantidade_de_assentos.append(assentos)
                            break
                case 2:
                    while True:
                        assentos = int(input("Escolha quantos assentos deseja comprar: "))
                        if assentos > 25:
                            print("Erro.")
                            print("Quantidade de assentos indisponíveis.")
                        else:
                            quantidade_de_assentos.append(assentos)
                            break
                case 3:
                    while True:
                        assentos = int(input("Escolha quantos assentos deseja comprar: "))
                        if assentos > 36:
                            print("Erro.")
                            print("Quantidade de assentos indisponíveis.")
                        else:
                            quantidade_de_assentos.append(assentos)
                            break
                case 4:
                    while True:
                        assentos = int(input("Escolha quantos assentos deseja comprar: "))
                        if assentos > 36:
                            print("Erro.")
                            print("Quantidade de assentos indisponíveis.")
                        else:
                            break
                case _:
                    print("Nenhum avião foi selecionado ainda...")
                    break

        case 4:

        case 5:

        case 6:

        case _:
        
# Finalização de Sistema