leiviska = int(input("Anna leiviskat:"))
naula = int(input("Anna naulat:"))
luoti = int(input("Anna luodit:"))


luodit = leiviska * 20 * 32 + naula * 32 + luoti
grammat = luodit * 13.3

kilot = int(grammat // 1000)
grammat = grammat - kilot * 1000

print(f"Massa on {kilot} kilogrammaa ja {grammat} grammaa")