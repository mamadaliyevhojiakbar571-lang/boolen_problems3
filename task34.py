# Boolean34. Shaxmat doskasining x, y koordinatalari berilgan (1-8 oraliqda yotuvchi butun sonlar).
# Doskaning chap pastki maydoni (1,1) oraligini hisobga olib, jumlani rostlikka tekshiring: "Berilgan (x,
# y) maydon oq".
x = int(input("x: "))
y = int(input("y: "))
natija = (x + y) % 2 == 0
print("Natija:", natija)