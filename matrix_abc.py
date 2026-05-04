import random

def def3(n):
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, n * n * 10 - 1))
        a.append(row)
    return a

def def4(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(f"{a[i][j]:6d}", end=" ")
        print()

n = int(input())

if 1 < n <= 5:
    A = def3(n)
    B = def3(n)
    C = def3(n)

    result = []

    for i in range(n):
        row = []
        for j in range(n):
            value = 0
            for k in range(n):
                value += A[i][k] * B[k][j]
            value += C[i][j]
            row.append(value)
        result.append(row)

    print("A")
    def4(A)

    print("B")
    def4(B)

    print("C")
    def4(C)

    print("A x B + C")
    def4(result)

else:
    print("input error")
