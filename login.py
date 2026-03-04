import os
os.system("cls")
from colorama import init, Fore, Back, Style


# entrada
print(Fore.BLUE + "Por favor, faça o login:\n" + Style.RESET_ALL)

login = str(input("Login:\n"))
senha = float(input("\nSenha:\n"))
ryanssilva = str

# processo

print("\n\n===Processando===\n")

if login == "ryanssilva" and senha == 77891:
    print(Fore.GREEN + f"Seja bem-vindo, {login}!!" + Style.RESET_ALL)
else:
    print(Fore.RED + "Login ou senha inválidos, tente novamente." + Style.RESET_ALL) 

