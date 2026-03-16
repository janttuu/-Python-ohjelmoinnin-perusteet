kaupungit = []

# Kysytään 5 kaupunkia
for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

#Tulostetaan kaupungit
print("Kaupungit ovat: ")
for kaupunki in kaupungit:
    print(kaupunki)