import random

def random_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, n * n * 10 - 1))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(f"{num:4}", end="")
        print()

def multiply_matrix(A, B):
    n = len(A)
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result

def add_matrix(A, B):
    n = len(A)
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result

def main():
    n = int(input("N을 입력하세요 (2~5): "))

    if n <= 1 or n > 5:
        print("N은 1보다 크고 5보다 작거나 같아야 합니다.")
        return

    A = random_matrix(n)
    B = random_matrix(n)
    C = random_matrix(n)

    print("\nA 행렬")
    print_matrix(A)

    print("\nB 행렬")
    print_matrix(B)

    print("\nC 행렬")
    print_matrix(C)

    AB = multiply_matrix(A, B)
    result = add_matrix(AB, C)

    print("\nA x B")
    print_matrix(AB)

    print("\nA x B + C")
    print_matrix(result)

main()
