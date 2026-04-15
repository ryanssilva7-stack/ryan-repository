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

os.system("cls")

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print(f"{F.B}=== {F.LW}SENAI {F.B}===")


# definições de funções
def calculo_do_imc (p, a):
    imc = p / (a * 2)
    return imc


def classificação_e_recomendação (imc):
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


# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
imcs = []
classificações = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input(f"{F.LC}Digite o nome do usuário {F.LW}(ou digite 'sair' para encerrar){F.LC}: {RESET}")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input(f"{F.LM}Digite a idade do usuário: {RESET}"))
    altura = float(input(f"{F.M}Digite a altura do usuário {F.LW}(em metros){F.M}: {RESET}"))
    peso = float(input(f"{F.LG}Digite o peso do usuário {F.LW}(em quilogramas){F.LG}: {RESET}"))
    
    # processo do cálculo e da classificação/recomedação
    imc = calculo_do_imc(peso, altura)
    classificação = classificação_e_recomendação(imc)

    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    imcs.append(imc)
    classificações.append(classificação)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")

for i in range(len(nomes)):
    print(f"{F.LC}Usuário {i+1}:")
    print(f"{F.LC}Nome:{RESET}", nomes[i])
    print(f"{F.LM}Idade:{RESET}", idades[i], f"{F.LM}anos.")
    print(f"{F.M}Altura:{RESET}", alturas[i], f"{F.M}metros")
    print(f"{F.LG}Peso:{RESET}", pesos[i], f"{F.LG}quilogramas")
    print(f"{F.LY}Índice de massa corporal {F.LW}(IMC){F.LY}: {F.LW}{imcs[i]:.2f}")
    print(f"{F.LB}Classificado(a) como: {F.LW}{classificações[i]}\n" )
    print(f"{F.LG}-------------------------------------\n")