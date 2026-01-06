# Boolean35. Shaxmat doskasining ikkita turli (x1, y1), (x2, Y2) koordinalan benlgan (1-8 oraliqda
# yotuvchi butun sonlar). Jumlani rostlikka tekshiring: "Berilgan maydonlar bir xil rangda"
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: ")) 
y2 = int(input("y2: "))
natija = (x1 + y1) % 2 == (x2 + y2) % 2
print("Natija:", natija)
