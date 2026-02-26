import os
os.system ("cls")

# 1. Coleta os detalhes do evento (Entrada)
anfitriao = input("Quem é o dono da festa? ")
tipo_festa = input("Qual o motivo da festa? (Ex: Aniversário, Churrasco): ")
data = input("Qual será o dia? ")
hora = input("Qual será o horário? ")
local = input("Onde vai ser? ")

# 2. Criando o convite (Processamento)
# Dica: O \n serve para o Python pular uma linha no texto!
convite = "----------------------------------------\n"
convite += "🎉 VOCÊ FOI CONVIDADO! 🎉\n"
convite += "----------------------------------------\n"
convite += (f"{anfitriao} está te chamando para um(a) {tipo_festa}!\n")
convite += "📅 Data: " + data + "\n"
convite += "⏰ Hora: " + hora + "\n"
convite += "📍 Local: " + local + "\n"
convite += "----------------------------------------"

# 3. Mostrando o convite final (Saída)
print(convite)