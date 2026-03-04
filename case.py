import os
os.system

# entrada
dia = input("Digite o dia da semana: ").lower()

match dia:
    case "segunda":
        print("Hoje é segunda-feira.")
    case "terça":
        print("Hoje é terça-feira.")
    case "quarta":
        print("Hoje é quarta-feira.")
    case "quinta":
        print("Hoje é quinta-feira.")
    case "sexta":   
        print("Hoje é sexta-feira.")
    case "sábado" | "domingo":
        print("Hoje é final de semana!")
    case _:
        print("dia invalido.")
        
print(dia)
