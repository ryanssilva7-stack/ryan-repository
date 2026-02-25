import os
os.system ("cls")

# entrada
maca = int(input("Digite quantas maçãs deseja comprar:"))

# processo
macamenos = (maca) * 1.30
macaamais = (maca) * 1
if maca < 12:
    print (f"valor à pagar: R${macamenos}")
else:
    print (f"valor à pagar: R${macaamais}")

# saida

