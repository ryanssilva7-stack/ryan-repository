# entrada
import os
os.system("cls || clear")

# processo
def tabuada(n1):
    os.system("cls")

    print(f"==== Tabuada de {n1} ====")
    for i in range(1, 11):
        resultado = n1 * i
        print(f"{n1} x {i} = {resultado}")

# saida
numero = int(input("Digite um  número pra tabuada: "))
tabuada(numero)