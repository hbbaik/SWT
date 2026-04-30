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

def transpose_matrix(A):
    n = len(A)
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[j][i])
        result.append(row)

    return result

def main():
    n = int(input("N을 입력하세요 (2~5): "))

    if n <= 1 or n > 5:
        print("N은 1보다 크고 5보다 작거나 같아야 합니다.")
        return

    A = random_matrix(n)

    print("\n원래 행렬 A")
    print_matrix(A)

    T = transpose_matrix(A)

    print("\nA의 전치 행렬")
    print_matrix(T)

main()
