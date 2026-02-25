import os
os.system ("cls || clear")

# entrada
print("Carregando...\n")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))

# processo
soma = (numero1+numero2)
produto = (soma) * 2
media = (soma) / 2

# saída
print("\n Processando...\n")

if numero1 == numero2:
    print(f"Os números {numero1} e {numero2} são iguais.")
    
if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}.")
    
if numero2 > numero1:
    print(f"O número {numero2} é maior que o número {numero1}.")

print(f"\nValor da soma:{soma}")
print(f"valor do produto:{produto}")
print(f"Média:{media}")


