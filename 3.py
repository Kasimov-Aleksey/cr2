print("Решение сравнений")
q, r = "-", "-",
check1, check2, check3 = int(input("Введите число перед х:     ")),int(input("Введите число перед mod:     ")),  int(input("Введите mod:    "))
check = [check1, check3]
a, b = max(check), min(check)
y2, y1 = 0, 1


print()
print("Вы ввели:    ")
print(f"{check1}x = {check2} (mod {check3})")


print()
print("Вы будет расчет :    ")
print(f"{check1}^(-1) mod {check2}")
print()
def evklid1():
    matrix =[]
    matx = []
    matx.append(str("q").ljust(6))
    matx.append(str("r").ljust(6))
    matx.append(str("a").ljust(6))
    matx.append(str("b").ljust(6))

    matrix.append(matx)
    return matrix
matrix = evklid1()
def evklid(q, r, a, b, matrix):
    check = True
    while True:
        if b == 0:
            check = False
        mat = []
        mat.append(str(q).ljust(6))
        mat.append(str(r).ljust(6))
        mat.append(str(a).ljust(6))
        mat.append(str(b).ljust(6))
        if b != 0:
            q, r = (a//b), (a%b)

        a, b  = b, r


        matrix.append(mat)
        if check == False:
            return matrix


matrix = evklid(q, r, a, b, matrix)


for i in (matrix):
    print(*i, sep=" ")

print()

m = int(matrix[-1][-2]) # количество делителей

print(f"НОД({a},{b}) = {m}")

print()
print("Делиние на m:    ")
print(f"({check1}/{m})x = ({check2}/{m}) (mod ({check3}/{m}))")


check1, check2, check3 = check1//m, check2//m, check3//m

print(f"{check1}x = {check2} (mod {check3})")


print()
print()
print()
check1_new, check2_new = check1, check3
check = [check1_new, check2_new]


q, r, y = "-", "-", "-"
a, b = max(check), min(check)
y2, y1 = 0, 1
def evklid_2():
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
matrix = evklid_2()




q, r, y = "-", "-", "-"
a, b = max(check), min(check)
y2, y1 = 0, 1
def evklid_2(q, r, y, a, b, y2, y1, matrix):
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


matrix = evklid_2(q, r, y, a, b, y2, y1, matrix)
matrix[-1][-1] = "X".ljust(6)
matrix[-1][2] = "X".ljust(6)

for i in (matrix):
    print(*i, sep=" ")

print()
u = int(matrix[-1][-2])
print(f"y2 = u = {u}")


print(f"{check1}^(-1) mod {check3} = {u}")
print()
x_f = (u*check2)%check3
print(f"{check1}^(-1) * {check2} mod {check3} = {x_f}")
print()


for i in range(m):
    x = x_f + i*check3
    print(f"x{i+1} = {x_f} + {i} * {check3} = {x}")
