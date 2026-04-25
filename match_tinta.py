import os
os.system("cls")

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura

tinta = area / 2

print(f"Será necessário {tinta:.0f} baldes de tinta para pintar {area}m² de parede.")