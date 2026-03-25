import os
import time

# Limpar terminal
os.system("cls")

# Dados

valor_total = 0
contador = 0
quantidade_de_inteiros = int(input("Quantos números deseja colocar?\n"))

# Processamento
for i in range (quantidade_de_inteiros):
    while True:        
        inteiro = int(input(f"\nDigite o {i+1}º número: "))

        if inteiro < 0:
            print("\nERRO!!\nNúmero inteiro inválido\n")
            exit()
        else:
            valor_total += inteiro
            break

media = (valor_total / quantidade_de_inteiros)
media_arredondada = round(media, 2)

# Resultado
print("\n\n===== Carregando =====")
time.sleep(2)

print(f"Soma: {valor_total}")
print(f"Média: {media_arredondada}")