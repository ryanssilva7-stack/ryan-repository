import os
os.system("cls")

def valor(d, nome):
    horas_trabalhadas = d * 8
    reais_por_hora = horas_trabalhadas * 25
    valor_total_reais = f'{reais_por_hora:.2f}'.replace(",", ".")
    print(f"Salário do(a) funcionário(a) {nome}: R${valor_total_reais}")

nome = input("Nome do funcionário: ")
dias = int(input("Digite quantos dias foram trabalhados no mês: "))

valor(dias, nome)