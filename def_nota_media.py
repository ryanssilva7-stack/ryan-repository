import os

os.system("cls")

# definições
def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma



def media(soma, quantidade_de_notas):
    media = soma / quantidade_de_notas
    return media



# dados
armazenamento_de_notas = []
quantidade_de_notas = 3

# processo
for i in range(quantidade_de_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    armazenamento_de_notas.append(nota)

soma = somar(armazenamento_de_notas[0], armazenamento_de_notas[1], armazenamento_de_notas[2])
media = media(soma, quantidade_de_notas)

print(f"Média: {media:.1f}")