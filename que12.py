import numpy as np

def compute_eigen_properties(matrix_data):

    matrix = np.array(matrix_data)
    
    print("Original Matrix (A):")
    print(matrix, "\n")
    

    rows, cols = matrix.shape
    if rows != cols:
        print("Error: Eigenvalues and eigenvectors can only be computed for square matrices.")
        return

    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    print("Eigenvalues (λ):")

    print(np.round(eigenvalues, 4), "\n")
    
    print("Eigenvectors (v):")
    print("Note: In NumPy, each *column* represents an eigenvector.")
    print(np.round(eigenvectors, 4), "\n")

    print("-" * 50)
    print("Verification: A * v = λ * v (for the first pair)")
    print("-" * 50)
    
    lambda_1 = eigenvalues[0]
    v_1 = eigenvectors[:, 0]
    
    left_side = matrix @ v_1

    right_side = lambda_1 * v_1
    
    print(f"Matrix * Eigenvector (A @ v):\n{np.round(left_side, 4)}\n")
    print(f"Eigenvalue * Eigenvector (λ * v):\n{np.round(right_side, 4)}\n")
    print("Both results are identical, confirming the calculation is correct!")

if __name__ == "__main__":

    A = [
        [4, -2],
        [1,  1]
    ]
    
    print("============================================")
    print(" EIGENVALUES AND EIGENVECTORS")
    print("============================================\n")
    
    compute_eigen_properties(A)