import os
os.system("cls")

# entrada
nota = int(input("Digite a nota: "))
print("\n")

# saida
if nota < 0 or nota > 10:
    print(f"Nota: {nota}.") 
else:
    print("A nota deve ser entre 0 e 10.")
