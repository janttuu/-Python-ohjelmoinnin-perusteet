leiviska = int(input("Anna leiviskat: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))

#muunnokset:
luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviska_grammoina = 20 * naula_grammoina

massa_grammoina = (leiviska * leiviska_grammoina + naula * naula_grammoina + luoti * luoti_grammoina)
kilot = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000

print(f"Massa on {kilot} kilogrammaa ja {grammat} grammaa")