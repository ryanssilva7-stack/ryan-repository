import os

palavra = input("Palavra: ")
numero = 1
ao_contrario = ""

for total in palavra:
    numero += 1

for i in range(1, numero):
    ao_contrario += palavra[-i]

os.system("cls")
print("Palavra:", palavra.title())
print("Ao contrário:", ao_contrario.title())

