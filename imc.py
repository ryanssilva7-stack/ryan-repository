import os
os.system ("cls")

# entrada
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

# processo
imc = peso / (altura * altura)
# saída
if imc < 18.5:
    print(f"\n{imc}: Abaixo do peso.")
elif imc <= 24.9:
    print(f"\n{imc}: Peso ideal (parabéns!)")
elif imc <= 29.9:
    print(f"\n{imc}: Levemente acima do peso.")
elif imc <= 34.9:
    print(f"\n{imc}: Obesidade grua I.")
elif imc <= 39.9:
    print(f"\n{imc}: Obesidade grua II (severa).")
elif imc > 40:
    print(f"\n{imc}: Obesidade grua III (mórbida).")
    
print("=====fim=====")
