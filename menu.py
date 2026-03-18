import os
os.system

# dados
print("""
============ CARDÁPIO ===========
Código    |   Pratos   |    Valor
---------------------------------
  01         Picanha     R$ 25,00
  02         Lasanha     R$ 20,00
  03        Strogonff    R$ 18,00
  04     Bife acebolado  R$ 15,00
  05       Pão com ovo   R$  5,00      
      """)

# processo
while True:
    codigo = int(input("Escolha um código: "))
    