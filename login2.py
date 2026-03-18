import os
import time

# Limpar o terminal
os.system("cls")

# dados
login_correto = "Ricardo.souza@gmail.com"
senha_correta = 123456
contador = 0

# processo

while True:
    login = input("Digite seu login:\n")
    senha = int(input("\nDigite sua senha:\n"))
    
    login_esta_correto = login == login_correto
    senha_esta_correta = senha == senha_correta
    contador += 1
    
    if contador == 3:
        break
    
    if login_esta_correto and senha_esta_correta:
        print(f"\nBem vindo {login}\n")
        break
    else:
        print("\nLogin ou senha inválida.")
        print(f"Tente novamente.\n")
        
# saida
print ("fim")