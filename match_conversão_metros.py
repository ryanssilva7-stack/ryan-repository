import os
os.system("cls")

metros = float(input("Digite uma distância em metros: "))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f"A distância de: {metros}m corresponde a:")
print(f"""
{km}km              {dm}dm
{hm}hm              {cm}cm
{dam}dam            {mm}mm

""")