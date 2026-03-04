import math

while True:
    luku = int(input("Anna kokonaisluku: "))

    if luku == 0:
        break
    elif luku < 0:
        print("Virheellinen numero")
    else:
        print("Neliöjuuri:", math.sqrt(luku))