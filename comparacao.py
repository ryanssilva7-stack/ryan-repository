import os
os.system ("cls")

# entrada
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite mais um número: "))
# Processo
print(f"\nOs números selecionados foram: {numero1} e {numero2}")
if numero1<numero2:
        print(f"\nO número {numero2} é maior que o {numero1}.")
else:
        print(f"\nO número {numero1} é maior que o {numero2}.")
# saída
print ("\n=====fim=====")