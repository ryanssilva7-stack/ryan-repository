import os 
# limpar o terminal
os.system("cls || clear")

idade = int(input("Digite sua idade: "))

# condicional composta
if idade <= 18:
        print("Acesso negado.")
else:
        print("Acesso permitido.")

        
print("Progama encerrado")