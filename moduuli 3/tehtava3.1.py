kuha = float(input("Kuinka pitkä kuha on? "))

alamitta = 37

if kuha < alamitta:
    puuttuu = alamitta - kuha
    print("Kuha on alamittainen, laske takaisin järveen.")
    print(f"Pituudesta puuttuu {int(puuttuu)} cm.")
else:
    print("Kuha on sallittua pyyntikokoa.")

