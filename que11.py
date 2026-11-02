import numpy as np

def compute_matrix_properties(matrix_data):
    matrix = np.array(matrix_data)
    
    print("Original Matrix:")
    print(matrix, "\n")
    
    rank = np.linalg.matrix_rank(matrix)
    print(f"Rank of the Matrix: {rank}\n")
    

    rows, cols = matrix.shape
    if rows != cols:
        print("Note: Determinant and Inverse can only be computed for square matrices.")
        return

    det = np.linalg.det(matrix)
    print(f"Determinant: {round(det, 4)}\n")

    if round(det, 4) != 0:
        try:
            inverse = np.linalg.inv(matrix)
            print("Inverse of the Matrix:")
            print(np.round(inverse, 4))
        except np.linalg.LinAlgError:
            print("Error: Could not compute the inverse.")
    else:
        print("Inverse of the Matrix: Does not exist (Matrix is singular because determinant is 0).")


if __name__ == "__main__":

    A = [
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ]
    
    print("============================================")
    print(" MATRIX DETERMINANT, INVERSE, AND RANK")
    print("============================================\n")
    
    compute_matrix_properties(A)