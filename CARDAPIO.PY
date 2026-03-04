import os
os.system("cls")

# menu
print("""
      =============== MENU ===============
       CÓDIGO        PRATO          PREÇO
       
       01          Macarronada   R$ 20,00
       02           Acebolada    R$ 15,00
       03             Pizza      R$ 34,99
       04             Filé       R$ 48,00
       05            Lasanha     R$ 27,99
       06          Pão com ovo   R$ 10,00
      
      
      """)

# entrada
codigo = input("Digite o código do prato: ")
print("\n")

#proceso
match codigo:
    case "01":
     print("Macarronada R$ 20,00")
    case "02":
     print("Acebolada R$ 15,00")
    case "03":
     print("Pizza R$ 34,99")
    case "04":
     print("Filé R$ 48,00")
    case "05":
     print("Lasanha R$ 27,99")
    case "06":
     print("Pão com ovo R$ 10,00")
    case _:
     print("Código incorreto.")
        
# saida
