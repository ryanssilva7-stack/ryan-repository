import os
os.system("cls")
from colorama import init, Fore, Back, Style

# entrada
print(Fore.BLUE + "- Seção de alistamento -\n" + Style.RESET_ALL)

nome = str(input("Digite seu nome: "))
ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))
genero = str(input("Digite sua sexualidade: ")).lower()

#processo
idade = 2026 - ano_de_nascimento

# saida
print("\n")
print(f"idade:{idade}")
print(f"sexo: {genero}")
print("\n")

if idade >= 18 and genero == "masculino":
    print(Fore.GREEN + "Deve se apresentar para o serviço militar obrigatório." + Style.RESET_ALL)
else:
    print(Fore.GREEN + "Não deve apresentar-se." + Style.RESET_ALL)