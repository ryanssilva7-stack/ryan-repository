import os
os.system ("cls")

compra = float(input("Valor da compra:"))
pago = float(input("Valor pago:"))

troco = (pago-compra)

print(f"Troco:{troco}")