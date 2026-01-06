# Boolean 32. a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c tomonli uchburchak to'g'ri
# burchakli".
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
natija = (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2)
print("Natija:", natija)