vastaus = input("Anna luku (tyhjä lopettaa): ")

if vastaus == "":
    print("Et syöttänyt lukua.")
else:
    luku = float(vastaus)
    pienin = luku
    suurin = luku

    while True:
        vastaus = input("Anna luku (tyhjä lopettaa): ")

        if vastaus == "":
            break

        luku = float(vastaus)

        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku

    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)
