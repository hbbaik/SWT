import random

# N x N 행렬을 랜덤한 정수값으로 만드는 함수
def num(p):
    matrix = []
    for i in range(p):
        row = []
        for j in range(p):
            row.append(random.randint(1, p * p * 10 - 1))
        matrix.append(row)
    return matrix

# 행렬을 보기 좋게 출력하는 함수
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
    B = num(N)
    C = num(N)

    print("A")
    show(A)
    print("B")
    show(B)
    print("C")
    show(C)

    # A x B 계산
    ab = []
    for i in range(N):
        row = []
        for j in range(N):
            s = 0
            for k in range(N):
                s += A[i][k] * B[k][j]
            row.append(s)
        ab.append(row)

    # (A x B) + C 계산
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(ab[i][j] + C[i][j])
        result.append(row)

    print("A x B + C")
    show(result)
