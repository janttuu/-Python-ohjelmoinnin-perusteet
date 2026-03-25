import random


def heita_noppaa(tahkot):
    return random.randint(1,tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))

while True:
    tulos = heita_noppaa(tahkot)
    print("Heitto:", tulos)

    if tulos == tahkot:
        break