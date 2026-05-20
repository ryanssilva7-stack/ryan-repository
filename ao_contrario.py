import os

massa = input("Massa: ")
numero = 1
maneiro = ""

for total in massa:
    numero += 1

for i in range(1, numero):
    maneiro += massa[-i]

os.system("cls")
print("Palavra:", massa.title())
print("Ao contrário:", maneiro.title())

