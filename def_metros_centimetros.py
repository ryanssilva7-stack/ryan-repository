import os
os.system("cls")

def formatacao(m):
    centimetro = m * 100
    print(f"{centimetro:.0f} centímetros.")

metro = float(input("Digite uma medida: "))
print("\n")
print(f"{metro} metros.")
formatacao(metro)