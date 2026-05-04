import random

def num(p):
    matrix = []
    for i in range(p):
        row = []
        for j in range(p):
            row.append(random.randint(1, p * p * 10 - 1))
        matrix.append(row)
    return matrix

def show(square):
    for row in square:
        for value in row:
            print(f"{value:5}", end="")
        print()

N = int(input("N을 입력하세요 (2~5): "))

if N <= 1 or N > 5:
    print("N은 1보다 크고 5보다 작거나 같아야 합니다.")
else:
    A = num(N)

    print("A")
    show(A)

    # 전치 행렬 계산
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(A[j][i])
        result.append(row)

    print("Transpose of A")
    show(result)
