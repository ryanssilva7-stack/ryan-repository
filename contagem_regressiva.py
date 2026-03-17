import os
import time
os.system("cls")

# dados
numero = int(input("Digite um número: "))

# processo
for i in range (numero, 0, -1):
    print (i)
    time.sleep(1)