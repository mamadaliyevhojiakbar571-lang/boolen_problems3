# Boolean40. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalan benlgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Ot bir yurishda bir maydondan ikkinchisiga o'ta
# oladi".
x1 = int(input("x1: "))
y1 = int(input("y1: ")) 
x2 = int(input("x2: "))
y2 = int(input("y2: "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
result = (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
print("Natija:", result)
