luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    luku = int(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

suurimmat = luvut[:5]

print("Viisi suurinta lukua: ")
for luku in suurimmat:
    print(luku)