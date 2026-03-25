import os
import time


salario_total = 0
quantidade_de_familias = 0
filhos_no_total = 0

# Inicialização
while True:
    os.system("cls")
    print("""
  Código | Descrição
    1    | Adcionar família
    2    | Sair e exibir resultados
    """)
    escolha = int(input("Escolha um dos códigos: "))
    match escolha:
        case 1:
            os.system ("cls")
            # pedido de dados
            quantidade_de_filhos = int(input("\nAdcione quantos filhos a família possui: "))
            salario = float(input("Digite o salário: "))
            
            # Acúmulo de conteúdo
            quantidade_de_familias += 1
            filhos_no_total += quantidade_de_filhos
            salario_total += salario

            # Cálculo de maior/menor salário
            if quantidade_de_familias == 1:
                maior_salario = menor_salario = salario
            else:
                if salario > maior_salario: maior_salario = salario
                if salario < menor_salario: menor_salario = salario

            print("\n=== Processando ===")
            time.sleep(2)
            
        case 2:
            if quantidade_de_familias > 0:
                os.system ("cls")
                print("=== Resultados ===\n")
                media_salarial = salario_total / quantidade_de_familias
                media_de_filhos = filhos_no_total / quantidade_de_familias
                print(f"Quantidade de famílias que responderam: {quantidade_de_familias}")
                print(f"Média do número de filhos: {media_de_filhos:.0f}")
                print(f"Média salarial da população: R${media_salarial:.0f}")
                print(f"Maior salário grupal: {maior_salario:.0f}\nMenor salário grupal: {menor_salario:.0f}")
                enter = input("\nEnter para sair ")

                print("\n==== Desligando terminal ====")
                time.sleep(2)
                break  
                
            else:
                print("Nenhum dado cadastrado ainda.")
                enter = input("\nEnter para sair ")

        case _:
            print("Não é uma opção válida")
            enter = input("\nEnter para sair ")