import os
os.system("cls")

def inflacao(p):
    if p < 100:
        inflacao = 0.1
        porcento = "10%"
    else:
        inflacao = 0.2
        porcento = "20%"
    
    resultado = p + (p * inflacao)

    print(f"Produto com {porcento} de inflação: {resultado:.0f}")

    

produto = int(input("Digite o valor do produto: "))
print("\n")
inflacao(produto)