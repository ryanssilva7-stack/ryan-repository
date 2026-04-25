import os
from colorama import Fore, Back, Style, init
import time

# Initialize colorama
init(autoreset = True)

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

# definições
def folha():
    os.system("cls")
    print("==== Folha de Pagamento ====")


def real(dinheiro):
    return f'{dinheiro:.2f}'.replace(".", ",")


def desconto_transporte(s):
    return s * 6 / 100


def desconto_dependente(d):
    return d * 150


def desconto_refeicao(vale):
    return vale * 20 / 100


def inss(salario):
    if salario <= 1518:
        desconto = 7.5 / 100

    elif salario > 1518 and salario < 2793.89:
        desconto = 9 / 100

    elif salario >= 2793.89 and salario < 4190.84:
        desconto = 12 / 100

    elif salario >= 4190.84:
        desconto = 14 / 100

    return salario * desconto


def irrf(salario):
    if salario <= 2428.81:
        desconto = 0

    elif salario > 2428.81 and salario < 2826.66:
        desconto = 7.5 / 100

    elif salario >= 2826.66 and salario < 3751.06:
        desconto = 15 / 100

    elif salario >= 3751.06 and salario < 4664.68:
        desconto = 22.5 / 100

    elif salario > 4664.69:
        desconto = 27.5 / 100

    return salario * desconto


# dados
folha()
matricula = input("Digite a matrícula do funcionário: ")
senha = int(input("Digite a senha da matrícula do funcionário: "))

folha()
salario = float(input("Digite o valor do salário: "))
print("O funcionário:")
transporte = input("Possui ou deseja vale transporte? (digite apenas sim ou não)\n").upper()
vale_refeicao = float(input("Digite o valor do vale refeição: "))
dependentes = int(input("Quantos dependentes o funcionário possui? (números apenas)\n"))
acrescimo = float(input("Porcentagem do acréscimo sobre o salário (se houver): "))

# processamento
if transporte == "SIM":
    resultado_transporte = desconto_transporte(salario)
    reposta_transporte = f"SIM | {F.LR}R${real(resultado_transporte)}{RESET}"
else:
    resultado_transporte = 0
    reposta_transporte = "NÃO"


if vale_refeicao > 0:
    resultado_refeicao = desconto_refeicao(vale_refeicao)
    resposta_refeicao = f"{F.LR}R${real(resultado_refeicao)}{RESET}"
else:
    resultado_refeicao = 0
    resposta_refeicao = "inexistente"


if dependentes > 0:
    resultado_dependente = desconto_dependente(dependentes)
    resposta_dependente = f"{dependentes} | Plano de saúde: {F.LR}R${real(resultado_dependente)}{RESET}"
else:
    resultado_dependente = 0
    resposta_dependente = "0"


# INSS e IRRF
resultado_inss = inss(salario)
resultado_irrf = irrf(salario)

if resultado_irrf <= 0:
    resposta_irrf = f"{F.LG}Isento{RESET}"
else:
    resposta_irrf = f"{F.LR}R${real(resultado_irrf)}{RESET}"

# Cálculo do salário final
if acrescimo < 0:
    salario_final = salario - resultado_transporte - resultado_dependente - resultado_inss - resultado_irrf - resultado_refeicao
else:
    salario_final = (salario - resultado_transporte - resultado_dependente - resultado_inss - resultado_irrf - resultado_refeicao) * (acrescimo / 100 + 1)

# saida de dados
folha()
print(f"""Salário Bruto: R${real(salario)}

Possui vale transporte?
{reposta_transporte}
dependente(s):
{resposta_dependente}
Desconto do vale refeição: {resposta_refeicao}

INSS: {F.LR}R${real(resultado_inss)}{RESET}
IRRF: {resposta_irrf}
""")

if acrescimo > 0:
    print(f"Acréscimo: {acrescimo}% | {F.LG}R${real(salario_final*(acrescimo/100))}{RESET}\n")

print(f"Salário final: {F.LG}R${real(salario_final)}{RESET}")
print("="*28)