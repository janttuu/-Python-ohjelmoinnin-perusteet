import random

# Tietokone arpoo luvun vain kerran
luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa numero väliltä 1-10: "))

    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein!")
        break