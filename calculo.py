import os
os.system("cls")

# entarda
numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite outro número:"))
simbolo = input("Escolha um caractere: ")
print("\n")

# processo
match simbolo:
    case "*":
        resultado = numero1*numero2
    case "/":
        resultado = numero1/numero2
    case "+":
        resultado = numero1+numero2
    case "-":
        resultado = numero1-numero2
    case _:
        print("Caractere inválido.")
        resultado = 0
  
# saída
print(f"Números escolhidos: {numero1} e {numero2}.")
print(f'Caractere: " {simbolo} "')
        
print("\nResultado:", (resultado))
print("\n")
print("===-=FIM====")


