def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    maara = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))

    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print("Määrä litroina:", litrat)
