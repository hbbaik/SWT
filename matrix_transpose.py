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

    result = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[j][i])
        result.append(row)

    print("A")
    def4(A)

    print("Transpose of A")
    def4(result)

else:
    print("input error")
