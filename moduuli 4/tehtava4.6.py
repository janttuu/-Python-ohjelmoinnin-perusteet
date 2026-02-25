import random

N = int(input("Kuinka monta pistettä arvotaan? "))

laskuri = 0
ympyrassa = 0

while laskuri < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        ympyrassa += 1

    laskuri += 1

pi_arvio = 4 * ympyrassa / N

print("Piin likiarvo on:", pi_arvio)