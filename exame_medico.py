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
exame_contador = 0
armazenamento_de_exames = []
quantidade_de_precos = []

# processo pedido
while True:
    
    
    print(f"""{F.LC}
Código   |     Exames     |      Valor

  1      Hemograma Completo    R$100,00
  2          Raio-X            R$145,00
  3      Ultrassonografia      R$ 80,00
  4      Eletrocardiograma     R$100,00
  5        Tomografia          R$300,00
  6   Ressonância Magnética    R$350,00
  7     Exame de Glicose       R$ 70,00
      {RESET}""")
    codigo = int(input(f"{F.LB}Escolha um dos exames por meio dos códigos: {RESET}"))
    
    match codigo:
        case 0:
            break
        case 1:
            nome = "Hemograma Completo"
            preco = 100
            exame_contador +=1
        case 2:
            nome = "Raio-X"
            preco = 145
            exame_contador +=1
        case 3:
            nome = "Ultrassonografia"
            preco = 80
            exame_contador +=1
        case 4:
            nome = "Eletrocardiograma"
            preco = 100
            exame_contador +=1
        case 5:
            nome = "Tomografia"
            preco = 300
            exame_contador +=1
        case 6:
            nome = "Ressonância Magnética"
            preco = 350
            exame_contador +=1
        case 7:
            nome = "Exame de Glicose"
            preco = 70
            exame_contador +=1
        case _:
            print(f"{F.R}Não é uma opção válida...")
            print(f"Tente novamente.{RESET}\n")
            time.sleep(1.25)
            continue
    
    armazenamento_de_exames.append(nome)
    quantidade_de_precos.append(preco)
    soma = sum(quantidade_de_precos)
    
    while True:
        escolha = input(f"{F.LB}Deseja marcar mais algum exame? {RESET}(S/N)\n").upper()

        if escolha in ["S", "N"]:
            break
        else:
            print(f"{F.LR}Não é uma escolha válida...")
    
    if escolha == "N":
        break

# processo pagamento
while True:
    os.system("cls")
    print(f"""{F.LC}
    Qual será a forma de pagamento?
   
    Código:
     (C)  Convênio;
     (P)  Particular;
     (CC) Cartão de crédito.\n""")

    forma_de_pagamento = input().lower()

    match forma_de_pagamento:
        case "c":
            pagamento = soma - (soma * 0.15)
            desconto = 15
            break
        case "cc":
            pagamento = soma + (soma * 0.08)
            acrescimo = 8
            break
        case "p":
            pagamento = soma
            break
        case _:
            print(f"{F.R}Não é uma opção válida...")
            print(f"Tente novamente.{RESET}")
            continue

# resultado
os.system("cls")

for i in range(exame_contador):   
    print(f"{F.C}Exame:{RESET} {armazenamento_de_exames[i]}")
    print(f"{F.LB}Preço:{RESET}{F.G}R${F.LG}{quantidade_de_precos[i]},00{RESET}\n")

if forma_de_pagamento == "c":
    print(f"{F.LM}Valor original:{RESET} {F.G}R${F.LG}{soma},00{RESET}")
    print(f"{F.LY}Valor a pagar com desconto: {F.G}R${F.LG}{pagamento:.0f},00{RESET}")

elif forma_de_pagamento == "cc":
    print(f"{F.LM}Valor original:{RESET} {F.G}R${F.LG}{soma},00{RESET}")
    print(f"{F.LY}Valor a pagar com acréscimo: {F.G}R${F.LG}{pagamento:.0f},00{RESET}")

elif forma_de_pagamento == "p":
    print(f"{F.LY}Valor a pagar:{RESET} {F.G}R${F.LG}{pagamento:.0f},00{RESET}")
