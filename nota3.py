import os

# limpar o terminal
os.system("cls")

# dados
contador = 0
valor_da_soma = 0

# processo
while True:
    nota = float(input(f"Digite a {contador+1}ª nota:"))
    escolha = input(""""Deseja colocar mais alguma nota? (S ou N)\n""").strip().upper()
    
    valor_da_soma += nota
    contador += 1
    
    if escolha == "N":
        break
    
# saida
media = valor_da_soma / contador
resultado = round(media, 1)
print(f"Média: {resultado}")