print("Поиск обратного значения через расширенный алгоритм Эвклида ")
# from math import gcd as g
q, r, y = "-", "-", "-"
check1, check2 = int(input("Введите число:     ")), int(input("Введите mod:    "))
check = [check1, check2]
a, b = max(check), min(check)
y2, y1 = 0, 1

print()
print("Вы ввели:    ")
print(f"{check1}^(-1) mod {check2}")

def evklid():
    matrix =[]
    matx = []
    matx.append(str("q").ljust(6))
    matx.append(str("r").ljust(6))
    matx.append(str("y").ljust(6))
    matx.append(str("a").ljust(6))
    matx.append(str("b").ljust(6))
    matx.append(str("y2").ljust(6))
    matx.append(str("y1").ljust(6))
    matrix.append(matx)
    return matrix
matrix = evklid()
def evklid(q, r, y, a, b, y2, y1, matrix):
    check = True
    while True:
        if b == 0:
            check = False
        mat = []
        mat.append(str(q).ljust(6))
        mat.append(str(r).ljust(6))
        mat.append(str(y).ljust(6))
        mat.append(str(a).ljust(6))
        mat.append(str(b).ljust(6))
        mat.append(str(y2).ljust(6))
        mat.append(str(y1).ljust(6))
        if b != 0:
            q, r = (a//b), (a%b)

        y = (y2-q*y1)
        a, b, y2, y1 = b, r, y1, y


        matrix.append(mat)
        if check == False:
            return matrix


matrix = evklid(q, r, y, a, b, y2, y1, matrix)
matrix[-1][-1] = "X".ljust(6)
matrix[-1][2] = "X".ljust(6)

for i in (matrix):
    print(*i, sep=" ")

print("Ответ:")
if int(matrix[-1][-4]) == 1:             # g(check1,check2)==1:
    print(f"Так как НОД({max(check)}, {min(check)}) = 1 ,")
    print(f"то {check1}^-1 mod {check2} существует и равно {int(matrix[-1][-2])%check2} (или {int(matrix[-1][-2])})")

else:
    print(f"Так как НОД({max(check)}, {min(check)}) != 1 ,")
    print(f"то {check1}^-1 mod {check2} не существет")

# print(f"{check1}^(-1) mod {check2} = {int(matrix[-1][-2])%check2}")