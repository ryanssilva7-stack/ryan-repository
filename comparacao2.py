import os
os.system ("cls")

# entrada
numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))
# Processo
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
# saída
print(f"\nOs números selecionados foram: {numero1}; {numero2} e {numero3}.\n")
print(f"O maior número é o:{maior}")
print(f"O menor número é o:{menor}\n")

print ("=====fim=====")