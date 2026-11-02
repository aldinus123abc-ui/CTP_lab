import numpy as np


def print_matrix(matrix, name):
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()

def add_matrices(A, B):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for j in range(len(A[0])):
        for i in range(len(A)):
            result[i][j] = A[i][j] + B[i][j]
    return result


def subtract_matrices(A, B):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for j in range(len(A[0])):
        for i in range(len(A)):
            result[i][j] = A[i][j] - B[i][j]
    return result

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose_matrix(A):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[j][i]

    return result


if __name__ == "__main__":
    
    A_list = [
        [1, 2],
        [3, 4]
    ]
    
    B_list = [
        [5, 6],
        [7, 8]
    ]

    print("=" * 40)
    print("=== PURE PYTHON (WITHOUT NUMPY) ===")
    print("=" * 40)
    
    print_matrix(add_matrices(A_list, B_list), "Addition (A + B)")
    print_matrix(subtract_matrices(A_list, B_list), "Subtraction (A - B)")
    print_matrix(multiply_matrices(A_list, B_list), "Multiplication (A * B)")
    print_matrix(transpose_matrix(A_list), "Transpose of A (A^T)")

    A_np = np.array(A_list)
    B_np = np.array(B_list)

    print("=" * 40)
    print("=== USING NUMPY ===")
    print("=" * 40)

    print("Addition (A + B):\n", A_np + B_np, "\n")
    
    print("Subtraction (A - B):\n", A_np - B_np, "\n")

    print("Multiplication (A @ B):\n", A_np @ B_np, "\n")

    print("Transpose of A (A^T):\n", A_np.T, "\n")