# Boolean33. a, b, c butun sonlar berilgan. Jumlani rostlikka teksiring: "a, b, c tomonli uchburchak
# yasash mumkin".
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
natija = (a + b > c) and (a + c > b) and (b + c > a)
print("Natija:", natija)