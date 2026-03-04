tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Montako tuntia teit?: "))
paiva = input("Minä päivänä?: ")

if paiva == "sunnuntai":
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print("Päiväpalkkasi on ", paivapalkka, "euroa")
