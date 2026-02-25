import os
os.system ("cls")

# entrada
nota1 = float(input("Primeira nota:"))
nota2 = float(input("segunda nota:"))

# processo
media = (nota1+nota2) / 2

# saida
print(f"\nMédia: {media}\n")

if media >= 9:
    print("Aprovado")
elif media < 9:
    print("Aprovado")
elif media < 7.5:
    print("Aprovado")
elif media < 6:
    print("Reprovado")
else:
    print("Reprovado")

print("\n===FIM===")
