# Boolean37. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalan benlgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Shoh bir yurishda bir maydondan ikkinchisiga o'ta
# oladi."
x1 = int(input("x1: "))
y1 = int(input("y1: ")) 
x2 = int(input("x2: "))
y2 = int(input("y2: "))
natija = abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
print("Natija:", natija)