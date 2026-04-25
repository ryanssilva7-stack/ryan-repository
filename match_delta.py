import os
os.system("cls")

while True:
    try:
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
    except ValueError:
        print("Digite apenas números inteiros")

    else:
        break
delta = (b*b) - (4*a*c)

os.system("cls")
print(f"{a}x² + {b}x + {c} = 0\n")
print(f"Delta = b² - 4ac")
print(f"Delta = {b}² - 4 * {a} * {c}")
print(f"Delta = {b*b} - {4*a*c}")
print(f"Delta = {delta}")