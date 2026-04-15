# Limpeza de terminal
import os
os.system("cls")

# quantidade de numeros
quantidade_de_numeros = 5

# Variáveis para armazenar os números
numeros_gerais = []
soma_pares = []
soma_impares = []

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0

# Processando e armazenando cada número
for i in range(quantidade_de_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros_gerais.append(numero)

# Pares e impares
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares.append(numero)
    else:
        quantidade_impares += 1
        soma_impares.append(numero)
        
# Positivos e negativos
    if numero >= 0:
        quantidade_positivos += 1
    else:
        quantidade_negativos += 1
        
# Maior e menor
maior_numero = max(numeros_gerais)
menor_numero = min(numeros_gerais)

# Calculando as médias
media_geral = sum(numeros_gerais) / len(numeros_gerais)
media_par = sum(soma_pares) / quantidade_pares
media_impar = sum(soma_impares) / quantidade_impares

# Limpeza de terminal
os.system("cls")

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de numeros inseridos: {len(numeros_gerais)}")
print(f"Números na ordem inversa: {numeros_gerais[::-1]}")
print("-" * 45)
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print("-" * 30)
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print("-" * 30)
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print("-" * 30)
print(f"Média dos números pares: {media_par:.0f}")
print(f"Média dos números impares: {media_impar:.0f}")
print(f"Média geral: {media_geral:.0f}")