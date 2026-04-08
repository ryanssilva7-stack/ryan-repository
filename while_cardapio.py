# dados
import os

preco_total = 0
pratos_solicitados = ""

# processo
while True:
    os.system("cls")

    print("""
    ========== Cardápio ==========
      código |  comida   |   valor
    ------------------------------ 
       1      Picanha     R$ 25,00
       2      Lasanha     R$ 20,00
       3     Strogonoff   R$ 18,00
       4   Bife acebolado R$ 15,00
       5    Pão com ovo   R$  5,00
          
        """)

    opcao = int(input("Digite o número da opção desejada: "))

    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case _:
            prato = ""
            preco = 0
            print("Opção inválida.")
            print("Tente novamente... \n")
   
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    while True:
        mais_pedidos = input("Deseja fazer um novo pedido? \nUse S ou N: ").lower()
   
        if mais_pedidos in ["s", "n"]:
            break
        
    if mais_pedidos == "n":
            break

# processo final
print("\n=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos_solicitados}")
print(f"Total da compra: R$ {preco_total}")
    
