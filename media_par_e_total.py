import os
os.system("cls")

# dados
par = 0
impar = 0
soma_par = 0
soma_total_dos_numeros = 0
quantidade_de_numeros = int(input("Quantos números deseja adcionar?\n"))

# processo
for i in range (quantidade_de_numeros):
    numero = int(input(f"\nDigite o {i+1}º número: "))
    soma_total_dos_numeros += numero

# desliga terminal se houver número negativo
    if numero < 0:
        print("Valor inválido!!")
        exit()

# continuação do processo
    if numero % 2 > 0:
        impar += 1
    else:
        par += 1
        soma_par += numero

    print(f"Números pares: {par}; Números impares: {impar}\n")

# cálculo
media_par = soma_par / par
media_geral = soma_total_dos_numeros / quantidade_de_numeros

# Resultado
print(f"""
Média dos números pares: {media_par: .1f}
Média geral dos números: {media_geral: .1f}
""")
