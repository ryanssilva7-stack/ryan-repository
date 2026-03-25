import os
import time


salario_total = 0
quantidade_de_pessoas = 0
quantidade_de_mulheres_recebendo_5k_ou_mais = 0

# Inicialização
while True:
    os.system("cls")
    print("""
  Código | Descrição
    1    | Adcionar pessoa
    2    | Exibir resultados
    3    | Sair
    """)
    escolha = int(input("Escolha um dos códigos: "))
    match escolha:
        case 1:
            os.system ("cls")
            # pedido de dados
            pessoa = (input("\nAdcione uma pessoa: "))
            idade = int(input("Digite a idade: "))
            sexo = input("Digite o sexo (M e F): ").upper()
            salario = float(input("Digite o salário: "))
            
            # Acúmulo de conteúdo
            quantidade_de_pessoas += 1
            salario_total += salario

            # Cálculo de maior/menor idade
            if quantidade_de_pessoas == 1:
                maior_idade = menor_idade = idade
            else:
                if idade > maior_idade: maior_idade = idade
                if idade < menor_idade: menor_idade = idade

            # Cálculo do salário feminino
            if sexo == "F" and salario >= 5000:
                quantidade_de_mulheres_recebendo_5k_ou_mais += 1

            print("\n=== Processando ===")
            time.sleep(2)
            
        case 2:
            if quantidade_de_pessoas > 0:
                print("--- Resultado atual ---")
                media_salarial = salario_total / quantidade_de_pessoas
                print(f"Média salarial total do grupo: R${media_salarial:.0f}")
                print(f"Maior idade grupal: {maior_idade}\nMenor idade grupal: {menor_idade}")
                print(f"Quantidade de mulheres recebendo 5 mil ou mais: {quantidade_de_mulheres_recebendo_5k_ou_mais}")
                enter = input("\nEnter para sair ")
            else:
                print("Nenhum dado cadastrado ainda.")
                enter = input("\nEnter para sair ")
        case 3:
            print("\n==== Desligando terminal ====")
            time.sleep(2)
            break
        case _:
            print("Não é uma opção válida")
            enter = input("\nEnter para sair ")