print("Решение системы уравнений ")



def evklid():
    matrix =[]
    matx = []
    matx.append(str("q").ljust(6))
    matx.append(str("r").ljust(6))
    matx.append(str("x").ljust(6))
    matx.append(str("a").ljust(6))
    matx.append(str("b").ljust(6))
    matx.append(str("x2").ljust(6))
    matx.append(str("x1").ljust(6))
    matrix.append(matx)
    return matrix
matrix = evklid()


n_oper = int(input("Введите количество переменных:  "))
def inputi(n_oper):

    maxi = {}
    for i in range(n_oper):
        ad = int(input("Введите число:     "))
        mod = int(input("Введите mod:    "))

        maxi[i+1] = [ad, mod]
        print(f"x = {ad} (mod{mod})")
    N = 1
    for n in maxi.keys():
        N *= maxi[n][-1]
    print()
    print()
    print()

    print(f"N = {N}")
    for k in maxi.keys():
        # print(N/maxi[k][-1])
        maxi[k].append(int(N/maxi[k][-1]))



    return maxi

maxi = inputi(n_oper)
# print(maxi, sep="\n")


print()
print()
print(f"                   a   n    N ")
def cod(maxi, n_oper):
    for i in range(1,n_oper+1):
        print(f"{i}) x = {maxi[i][0]} (mod{maxi[i][1]})  {maxi[i]} ")


cod(maxi, n_oper)
print()

data_matrix = []
def evklid( matrix,maxi, data_matrix):
    # print(f"   a   n    N ")
    for k in maxi.values():
        # print(f"{k}) {maxi[k]}")
        check = True
        a, b = min(k), max(k)
        print(a, b)
        q, r, x = "-", "-", "-"
        x2, x1 = 1, 0

        matrix_1 = matrix.copy()

        while True:
            if b == 0:
                check = False
            mat = []
            mat.append(str(q).ljust(6))
            mat.append(str(r).ljust(6))
            mat.append(str(x).ljust(6))
            mat.append(str(a).ljust(6))
            mat.append(str(b).ljust(6))
            mat.append(str(x2).ljust(6))
            mat.append(str(x1).ljust(6))
            if b != 0:
                q, r = (a//b), (a%b)

            x = (x2-q*x1)
            a, b, x2, x1 = b, r, x1, x


            matrix_1.append(mat)
            if check == False:
                break

        matrix_1[-1][-1] = "X".ljust(6)
        matrix_1[-1][2] = "X".ljust(6)
        data_matrix.append(matrix_1)


    return data_matrix

data_matrix = evklid( matrix,maxi, data_matrix)

for j in data_matrix:
    print()
    print("########################################")
    print()
    for i in j:
        print(*i, sep=" ")

print()
print()
print()

def end():
    summer = 0
    N = 1
    for i in range(n_oper):
        # maxi[i+1] = data_matrix[i][-1][-2]
        print(f"u{i+1} = {data_matrix[i][-1][-2]}")
        summer += int(data_matrix[i][-1][-2]) * maxi[i+1][0] * maxi[i+1][-1]
        N *= maxi[i+1][-1]

    summer = summer%(maxi[i+1][-1]*N)

    ret = 1
    for i in maxi.values():
        ret *= i[1]



    summer = summer%ret
    return summer
# print(maxi)
summer = end()
print()
print(f"a = {summer}")
print()

for i in range(1, n_oper+1):
    if summer%(maxi[i][1]) == maxi[i][0]:
        print(f"{summer} mod{maxi[i][1]} = {maxi[i][0]}     +")
    else:
        print(f"{summer} mod{maxi[i][1]} != {maxi[i][0]}     -")