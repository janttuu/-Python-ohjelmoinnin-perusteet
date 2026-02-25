tuumat = 0

while tuumat >= 0:
    tuumat = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

    if tuumat >= 0:
        senttimetrit = tuumat * 2.54
        print("Senttimetreinä: ", round(senttimetrit, 2))

print("Ohjelma lopetetaan.")