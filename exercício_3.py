import os
os.system("cls || clear")

# dados
numero1 = int(input("Digite o primeiro número:" ))
numero2 = int(input("Digite o segundo número:" ))
maior = int
menor = int
# processo
soma = (numero1+numero2)
media = (soma) / 2
produto = (numero1*numero2)

# saída de dados
print(f"Soma: {soma}")
print(f"média: {media}")
print(f"produto: {produto}")

menor = min(numero1, numero2)
maior = max(numero1, numero2) 

print("O maior número é o:", maior)
print("O menor número é o:", menor)


# if numero1>numero2:
#     print(f"O número {numero1} é o maior")
# else: 
#     print(f"O número {numero2} é o maior")

# if numero1<numero2:
#     print(f"O número {numero1} é o menor")
# else: 
#     print(f"O número {numero2} é o menor")
   
print("------Fim------")
