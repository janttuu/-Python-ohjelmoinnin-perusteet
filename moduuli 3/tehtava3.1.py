kuhan_pituus = float(input("Kuinka pitkä kuha on? "))

alamitta = 37

if kuhan_pituus < alamitta:
    puuttuu = alamitta - kuhan_pituus
    print("Kuha on alamittainen, laske takaisin järveen.")
    print(f"Pituudesta puuttuu {int(puuttuu)} cm.")
else:
    print("Kuha on sallittua pyyntikokoa.")

