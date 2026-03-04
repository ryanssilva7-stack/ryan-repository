import os 
os.system("cls")

# entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a sergunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
faltas = int(input("Diigite a quantidade de faltas: "))
print("\n")

# processo
media = (nota1 + nota2 + nota3 +nota4) /4
media_aprovada = media >= 7.0
faltas_permitidas = faltas <= 40
arredondada = round(media, 1)

# saida
print(f"Média: {arredondada}")
print(f"Faltas: {faltas}/40.")
if media_aprovada and faltas_permitidas:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")
