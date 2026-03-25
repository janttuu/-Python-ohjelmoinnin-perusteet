import math

def pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m ** 2
    return hinta_euro / pinta_ala

h1 = float(input("Anna pizzan 1 halkaisija (cm): "))
p1 = float(input("Annan pizzan 1 hinta (€): "))

h2 = float(input("Anna pizzan 2 halkaisija (cm): "))
p2 = float(input("Annan pizzan 2 hinta (€): "))

y1 = pizzan_yksikkohinta(h1, p1)
y2 = pizzan_yksikkohinta(h2, p2)

print(f"Pizzan 1 yksikköhinta: {y1:.2f} €/m2")
print(f"Pizzan 2 yksikköhinta: {y2:.2f} €/m2")

if y1 < y2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif y2 < y1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä hyviä hinnaltaan.")