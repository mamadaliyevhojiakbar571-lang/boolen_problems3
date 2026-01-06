# Boolean31. a, b, c butun sonlari berilgan. Jumlani rostlikka tekshiring: "a, b, c tomonli uchburchak teng
# yonli bo'ladi"
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
natija = a == b or b == c or a == c
print("Natija:", natija)