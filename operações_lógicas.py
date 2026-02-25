import os
os.system ("cls")

# entrada
print("Preencha os campo abaixo com os dados correspondentes")

nome = (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

# Processo
if idade >= 65:
    print(f"\nPor possuir {idade} anos, seu voto já não é mais obrigatório.\n")
if idade >= 18:
    print(f"\nPor possuir {idade} anos, seu voto é obrigatório.\n")
if idade == 16:
    print(f"\nPor possuir {idade} anos, seu voto é opcional.\n")
if idade == 17:
    print(f"\nPor possuir {idade} anos, seu voto é opcional.\n")   
if idade < 16:
    print("\nVejamos que você é menor de idade, logo, você não possui permissão para votar.\n")


    
print("=======fim=======")