import os
os.system("cls")

# definicões de funções
def media_aritmetica(armazena_nota, quantidade_notas):
    media = sum(armazena_nota) / quantidade_notas
    return media


# dados
armazenamento_notas = []
quantidade_notas = 2

# processamento
for i in range(quantidade_notas):
    os.system("cls")

    print("\n=== Solicitando dados ===")
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        if nota < 0 or nota > 10:
            print("\nA nota deve ser entre 0 e 10. Digite novamente.\n")
        else:
            armazenamento_notas.append(nota)
            break

# saida de dados
os.system("cls")
print("=== Exibindo dados ===")
for i in range(quantidade_notas):
    print(f"{i + 1}ª nota: {armazenamento_notas[i]}")
print("\nMédia: ", media_aritmetica(armazenamento_notas, quantidade_notas))