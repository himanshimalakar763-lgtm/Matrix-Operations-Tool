"""
Example Usage and Test Cases for Matrix Operations Tool

This script demonstrates various use cases and provides examples of:
1. Direct NumPy operations for reference
2. Mathematical validation
3. Example matrices and expected results

Run this separately to verify NumPy functionality and understand outputs.
"""

import numpy as np

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(title.center(70))
    print("="*70 + "\n")

def print_matrix(matrix, label="Matrix"):
    """Print a matrix in formatted table."""
    print(f"{label}:")
    print("-" * (15 * matrix.shape[1] + 2))
    for row in matrix:
        print("│ " + " │ ".join(f"{val:>10.4f}" for val in row) + " │")
    print("-" * (15 * matrix.shape[1] + 2))

# ============================================================================
# EXAMPLE 1: MATRIX ADDITION
# ============================================================================

print_section("EXAMPLE 1: MATRIX ADDITION (A + B)")

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

result = np.add(A, B)

print_matrix(A, "Matrix A (2×3)")
print()
print_matrix(B, "Matrix B (2×3)")
print()
print_matrix(result, "Result (A + B)")

print("\nCalculation (element-wise):")
print("A[0,0] + B[0,0] = 1 + 7 = 8")
print("A[0,1] + B[0,1] = 2 + 8 = 10")
print("A[1,2] + B[1,2] = 6 + 12 = 18")

# ============================================================================
# EXAMPLE 2: MATRIX SUBTRACTION
# ============================================================================

print_section("EXAMPLE 2: MATRIX SUBTRACTION (A - B)")

A = np.array([[10, 20],
              [30, 40]])

B = np.array([[1, 2],
              [3, 4]])

result = np.subtract(A, B)

print_matrix(A, "Matrix A (2×2)")
print()
print_matrix(B, "Matrix B (2×2)")
print()
print_matrix(result, "Result (A - B)")

print("\nCalculation (element-wise):")
print("A - B = [[10-1, 20-2], [30-3, 40-4]]")
print("      = [[9, 18], [27, 36]]")

# ============================================================================
# EXAMPLE 3: MATRIX MULTIPLICATION
# ============================================================================

print_section("EXAMPLE 3: MATRIX MULTIPLICATION (A × B)")

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

result = np.matmul(A, B)

print_matrix(A, "Matrix A (2×3)")
print()
print_matrix(B, "Matrix B (3×2)")
print()
print_matrix(result, "Result (A × B) - (2×2)")

print("\nCalculation (dot product for each element):")
print("Result[0,0] = (1×7) + (2×9) + (3×11) = 7 + 18 + 33 = 58")
print("Result[0,1] = (1×8) + (2×10) + (3×12) = 8 + 20 + 36 = 64")
print("Result[1,0] = (4×7) + (5×9) + (6×11) = 28 + 45 + 66 = 139")
print("Result[1,1] = (4×8) + (5×10) + (6×12) = 32 + 50 + 72 = 154")

# ============================================================================
# EXAMPLE 4: MATRIX TRANSPOSE
# ============================================================================

print_section("EXAMPLE 4: MATRIX TRANSPOSE (A^T)")

A = np.array([[1, 2, 3],
              [4, 5, 6]])

result = np.transpose(A)

print_matrix(A, "Original Matrix A (2×3)")
print()
print_matrix(result, "Transposed Matrix A^T (3×2)")

print("\nExplanation:")
print("- Rows become columns")
print("- Columns become rows")
print("- A[i,j] becomes A^T[j,i]")
print("- Dimensions: (2×3) → (3×2)")

# ============================================================================
# EXAMPLE 5: MATRIX DETERMINANT
# ============================================================================

print_section("EXAMPLE 5: MATRIX DETERMINANT")

print("\n--- Case 1: 2×2 Matrix ---\n")

A = np.array([[4, 7],
              [2, 6]])

det = np.linalg.det(A)

print_matrix(A, "Matrix A (2×2)")
print(f"\nDeterminant: {det:.6f}")

print("\nCalculation:")
print("det(A) = (4×6) - (7×2)")
print("       = 24 - 14")
print("       = 10")

print("\n--- Case 2: 3×3 Matrix ---\n")

B = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 1, 0]])

det_b = np.linalg.det(B)

print_matrix(B, "Matrix B (3×3)")
print(f"\nDeterminant: {det_b:.6f}")

print("\nNote: 3×3 and larger determinants are calculated using")
print("LU decomposition for numerical stability and efficiency.")

print("\n--- Case 3: Singular Matrix (Determinant = 0) ---\n")

C = np.array([[1, 2],
              [2, 4]])

det_c = np.linalg.det(C)

print_matrix(C, "Matrix C (Singular - 2×2)")
print(f"\nDeterminant: {det_c:.6f}")
print("\nExplanation: Rows are linearly dependent (Row 2 = 2 × Row 1)")
print("This matrix is NOT invertible!")

# ============================================================================
# EXAMPLE 6: MATRIX INVERSE
# ============================================================================

print_section("EXAMPLE 6: MATRIX INVERSE (A^-1)")

print("\n--- Case 1: Invertible 2×2 Matrix ---\n")

A = np.array([[4.0, 7.0],
              [2.0, 6.0]])

inv_A = np.linalg.inv(A)

print_matrix(A, "Original Matrix A")
print()
print_matrix(inv_A, "Inverse Matrix A^-1")

# Verify: A × A^-1 = I
identity = np.matmul(A, inv_A)
print()
print_matrix(identity, "Verification: A × A^-1 (should be Identity)")

print("\n2×2 Matrix Inverse Formula:")
print("For A = [[a, b], [c, d]]")
print("A^-1 = (1/det(A)) × [[d, -b], [-c, a]]")
print(f"\nFor our matrix: det(A) = {np.linalg.det(A):.0f}")
print(f"A^-1 = (1/{np.linalg.det(A):.0f}) × [[6, -7], [-2, 4]]")

print("\n--- Case 2: Non-invertible (Singular) Matrix ---\n")

B = np.array([[1, 2],
              [2, 4]])

det_b = np.linalg.det(B)
print_matrix(B, "Singular Matrix B")
print(f"\nDeterminant: {det_b:.6f}")
print("\n❌ This matrix is singular!")
print("Cannot calculate inverse (determinant = 0)")

# ============================================================================
# EXAMPLE 7: MATRIX TRACE
# ============================================================================

print_section("EXAMPLE 7: MATRIX TRACE")

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

trace = np.trace(A)
diagonal = np.diag(A)

print_matrix(A, "Matrix A (3×3)")

print(f"\nTrace of A: {trace:.6f}")
print(f"Diagonal elements: {diagonal}")

print("\nCalculation:")
print("trace(A) = sum of diagonal elements")
print(f"         = {diagonal[0]} + {diagonal[1]} + {diagonal[2]}")
print(f"         = {trace:.0f}")

print("\nProperties:")
print(f"- trace(A) = trace(A^T)")
trace_t = np.trace(np.transpose(A))
print(f"  trace(A^T) = {trace_t:.0f} ✓")

# ============================================================================
# EXAMPLE 8: DIMENSIONAL COMPATIBILITY
# ============================================================================

print_section("EXAMPLE 8: DIMENSIONAL COMPATIBILITY")

print("\n--- Addition/Subtraction (must be same dimensions) ---\n")
print("✓ (2×3) + (2×3) = (2×3)     [VALID]")
print("✓ (4×4) - (4×4) = (4×4)     [VALID]")
print("✗ (2×3) + (3×2) = ERROR     [INVALID - Different shapes]")
print("✗ (2×2) - (3×3) = ERROR     [INVALID - Different shapes]")

print("\n--- Multiplication (columns of A must equal rows of B) ---\n")
print("✓ (2×3) × (3×2) = (2×2)     [VALID: 3 columns = 3 rows]")
print("✓ (3×4) × (4×5) = (3×5)     [VALID: 4 columns = 4 rows]")
print("✗ (2×3) × (2×3) = ERROR     [INVALID: 3 ≠ 2]")
print("✗ (5×4) × (3×2) = ERROR     [INVALID: 4 ≠ 3]")

print("\n--- Determinant/Inverse/Trace (must be square) ---\n")
print("✓ (3×3) determinant         [VALID - Square]")
print("✓ (4×4) inverse             [VALID - Square]")
print("✓ (2×2) trace               [VALID - Square]")
print("✗ (2×3) determinant = ERROR [INVALID - Not square]")
print("✗ (3×2) inverse = ERROR     [INVALID - Not square]")
print("✗ (4×3) trace = ERROR       [INVALID - Not square]")

# ============================================================================
# EXAMPLE 9: SPECIAL MATRICES
# ============================================================================

print_section("EXAMPLE 9: SPECIAL MATRICES")

print("\n--- Identity Matrix ---\n")
I = np.eye(3)
print_matrix(I, "3×3 Identity Matrix (I)")
print("Properties:")
print("- Square matrix with 1s on diagonal, 0s elsewhere")
print("- A × I = A (multiplication by identity gives original matrix)")

print("\n--- Zero Matrix ---\n")
Z = np.zeros((2, 3))
print_matrix(Z, "2×3 Zero Matrix")
print("Properties:")
print("- All elements are 0")
print("- A + Z = A (adding zero doesn't change matrix)")

print("\n--- Diagonal Matrix ---\n")
D = np.diag([2, 5, 8])
print_matrix(D, "3×3 Diagonal Matrix")
print("Properties:")
print("- Non-zero only on diagonal")
print("- trace(D) = sum of diagonal elements")

# ============================================================================
# EXAMPLE 10: PRACTICAL APPLICATION
# ============================================================================

print_section("EXAMPLE 10: PRACTICAL APPLICATION - Linear System")

print("\nSolving: 2x + 3y = 8")
print("         4x + 5y = 14\n")

# Coefficient matrix
A = np.array([[2, 3],
              [4, 5]])

# Constants
b = np.array([[8],
              [14]])

print_matrix(A, "Coefficient Matrix A")
print()
print_matrix(b, "Constants Vector b")

# Solve using matrix inverse: Ax = b  =>  x = A^-1 × b
x = np.matmul(np.linalg.inv(A), b)

print()
print_matrix(x, "Solution x = A^-1 × b")

print(f"\nSolution: x = {x[0, 0]:.1f}, y = {x[1, 0]:.1f}")

# Verification
result = np.matmul(A, x)
print()
print_matrix(result, "Verification: A × x (should equal b)")

# ============================================================================
# SUMMARY TABLE
# ============================================================================

print_section("SUMMARY TABLE - All Operations")

print("""
Operation               | Formula      | NumPy Function     | Input Requirement
────────────────────────┼──────────────┼────────────────────┼─────────────────────────
Addition                | A + B        | np.add()           | Same dimensions
Subtraction             | A - B        | np.subtract()      | Same dimensions
Multiplication          | A × B        | np.matmul()        | A.cols = B.rows
Transpose               | A^T          | np.transpose()     | Any rectangular matrix
Determinant             | det(A)       | np.linalg.det()    | Square matrix
Inverse                 | A^-1         | np.linalg.inv()    | Square non-singular
Trace                   | tr(A)        | np.trace()         | Square matrix

Time Complexity (n = matrix dimension):
────────────────────────────────────────────────────────────
Addition/Subtraction    | O(n²)
Matrix Multiplication   | O(n³) [or faster with optimized algorithms]
Transpose               | O(n²)
Determinant             | O(n³)
Inverse                 | O(n³)
Trace                   | O(n)
""")

print("\n" + "="*70)
print("End of Examples")
print("="*70 + "\n")

print("\nNOTE: To use the interactive tool, run:")
print("      python matrix_operations_tool.py")
