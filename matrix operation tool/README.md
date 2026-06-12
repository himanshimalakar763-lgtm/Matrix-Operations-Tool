# Matrix Operations Tool

## Project Overview

The **Matrix Operations Tool** is a comprehensive, interactive Python application built with NumPy that enables users to perform various matrix mathematical operations efficiently. The tool provides a user-friendly, menu-driven interface for inputting matrices and executing complex linear algebra computations with clear, formatted output.

---

## Features

### 1. Matrix Input
- **Flexible Input**: Users can input matrices of any dimension (up to 100×100)
- **Validation**: Comprehensive error checking for invalid dimensions or values
- **User-Friendly**: Clear prompts and error messages guide users through the process
- **Support for Multiple Matrices**: Store and work with two matrices simultaneously (A and B)

### 2. Matrix Operations

The tool implements the following operations using NumPy:

#### **Matrix Addition (A + B)**
- Adds two matrices of identical dimensions element-wise
- Uses NumPy's `np.add()` function for efficient computation
- **Requirements**: Both matrices must have the same shape (m × n)

#### **Matrix Subtraction (A - B)**
- Subtracts Matrix B from Matrix A element-wise
- Uses NumPy's `np.subtract()` function
- **Requirements**: Both matrices must have the same shape (m × n)

#### **Matrix Multiplication (A × B)**
- Performs standard matrix multiplication (dot product)
- Uses NumPy's `np.matmul()` function for optimal performance
- **Requirements**: Column count of A must equal row count of B
  - A (m × n) × B (n × p) = Result (m × p)

#### **Matrix Transpose (A^T or B^T)**
- Flips a matrix along its diagonal (rows become columns and vice versa)
- Uses NumPy's `np.transpose()` function
- **Requirements**: Works on any rectangular matrix
- **Result**: An (n × m) matrix from an (m × n) input

#### **Determinant Calculation**
- Calculates the scalar determinant value of a matrix
- Uses NumPy's `np.linalg.det()` function
- **Requirements**: Matrix must be square (n × n)
- **Mathematical Significance**: Indicates if matrix is singular (det=0) or invertible (det≠0)

#### **Matrix Inverse (A^-1 or B^-1)**
- Computes the multiplicative inverse of a matrix
- Uses NumPy's `np.linalg.inv()` function
- **Requirements**: Matrix must be:
  - Square (n × n)
  - Non-singular (determinant ≠ 0)
- **Property**: A × A^-1 = I (Identity Matrix)

#### **Matrix Trace**
- Calculates the sum of diagonal elements
- Uses NumPy's `np.trace()` function
- **Requirements**: Matrix must be square (n × n)
- **Formula**: trace(A) = Σ a_ii (sum of diagonal elements)
- **Property**: trace(A) = trace(A^T)

### 3. Interactive Interface
- **Menu-Driven Navigation**: Simple numbered menu system for all operations
- **Multiple Operations**: Perform unlimited operations without restarting
- **Error Handling**: Graceful error messages with guidance for resolution
- **Operation History**: Track all performed operations during the session
- **Status Feedback**: Clear confirmation messages for successful operations

### 4. Output Formatting
- **Tabular Display**: Matrices displayed in clean, aligned table format
- **Precision Control**: Values displayed with 4 decimal places for readability
- **Dimension Information**: Shows matrix shape (rows × columns)
- **Label Clarity**: Each matrix clearly labeled (Matrix A, Matrix B, Result, etc.)
- **Error Indicators**: Visual indicators (✓ for success, ❌ for errors)

### 5. Robust Error Handling
- **Input Validation**: Checks for valid matrix dimensions and numeric values
- **Dimension Verification**: Ensures operations work with compatible matrix sizes
- **Singular Matrix Detection**: Identifies non-invertible matrices
- **Boundary Checks**: Limits matrix size to 100×100 for performance
- **User Guidance**: Helpful error messages explaining what went wrong and why

---

## Program Design

### Architecture Overview

```
MatrixOperationsTool (Main Class)
│
├── __init__()                    # Initialize application state
├── UI Methods:
│   ├── display_header()          # Show application banner
│   ├── display_menu()            # Display operation menu
│   ├── display_matrix()          # Format and show matrices
│   ├── clear_screen()            # Clear console
│   └── view_history()            # Display operation history
│
├── Input Methods:
│   └── get_matrix_input()        # Collect and validate matrix input
│
├── Operation Methods:
│   ├── matrix_addition()         # A + B
│   ├── matrix_subtraction()      # A - B
│   ├── matrix_multiplication()   # A × B
│   ├── matrix_transpose()        # A^T or B^T
│   ├── matrix_determinant()      # det(A) or det(B)
│   ├── matrix_inverse()          # A^-1 or B^-1
│   └── matrix_trace()            # trace(A) or trace(B)
│
├── Utility Methods:
│   ├── view_matrices()           # Display current matrices
│   └── clear_data()              # Reset application state
│
└── run()                         # Main application loop
```

### Key Classes and Methods

#### **MatrixOperationsTool Class**
The central class managing all application functionality:

- **Attributes**:
  - `matrix_a`: NumPy array storing first input matrix
  - `matrix_b`: NumPy array storing second input matrix
  - `operation_history`: List tracking performed operations

- **Methods**: 13 public methods + helper functions for complete functionality

### Data Flow

```
User Input → Validation → NumPy Operation → Formatted Output → Display
                ↓
            Error Check → Error Message or Proceed
```

---

## Implementation Details

### NumPy Usage

The tool leverages NumPy for efficient matrix computations:

| Operation | NumPy Function | Complexity |
|-----------|----------------|-----------|
| Addition | `np.add()` | O(mn) |
| Subtraction | `np.subtract()` | O(mn) |
| Multiplication | `np.matmul()` | O(mnp) |
| Transpose | `np.transpose()` | O(mn) |
| Determinant | `np.linalg.det()` | O(n³) |
| Inverse | `np.linalg.inv()` | O(n³) |
| Trace | `np.trace()` | O(n) |

### Input Validation Strategy

1. **Dimension Check**: Verify rows and cols are positive integers ≤ 100
2. **Element Count Check**: Ensure each row has correct number of elements
3. **Type Conversion**: Convert all inputs to float for numerical operations
4. **Dimension Compatibility**: Check operations work with input matrix sizes
5. **Singularity Check**: Detect singular matrices before inverse calculation

### Error Handling Approach

- **Try-Except Blocks**: Catch NumPy-specific exceptions (LinAlgError)
- **Pre-Operation Validation**: Check dimensions before performing operations
- **Singular Matrix Detection**: Check determinant before calculating inverse
- **User-Friendly Messages**: Clear explanation of what went wrong

---

## Sample Inputs and Outputs

### Example 1: Matrix Addition

**Input:**
```
Matrix A (2×2):
2 3
4 5

Matrix B (2×2):
1 1
2 1
```

**Operation:** Addition (A + B)

**Output:**
```
──────────────────────────────────────────────────────
MATRIX ADDITION: A + B
──────────────────────────────────────────────────────

Matrix A:
─────────────────────────────────────────
│        2.0000 │        3.0000 │
│        4.0000 │        5.0000 │
─────────────────────────────────────────
Shape: 2 × 2

Matrix B:
─────────────────────────────────────────
│        1.0000 │        1.0000 │
│        2.0000 │        1.0000 │
─────────────────────────────────────────
Shape: 2 × 2

Result (A + B):
─────────────────────────────────────────
│        3.0000 │        4.0000 │
│        6.0000 │        6.0000 │
─────────────────────────────────────────
Shape: 2 × 2

✓ Operation completed successfully!
```

### Example 2: Matrix Multiplication

**Input:**
```
Matrix A (2×3):
1 2 3
4 5 6

Matrix B (3×2):
7 8
9 10
11 12
```

**Operation:** Multiplication (A × B)

**Output:**
```
──────────────────────────────────────────────────────
MATRIX MULTIPLICATION: A × B
──────────────────────────────────────────────────────

Result (A × B):
─────────────────────────────────────────
│       58.0000 │       64.0000 │
│      139.0000 │      154.0000 │
─────────────────────────────────────────
Shape: 2 × 2

✓ Operation completed successfully!

Calculation: (1×7 + 2×9 + 3×11), (1×8 + 2×10 + 3×12)
           = (58), (64)
           (4×7 + 5×9 + 6×11), (4×8 + 5×10 + 6×12)
           = (139), (154)
```

### Example 3: Determinant Calculation

**Input:**
```
Matrix A (2×2):
4 7
2 6
```

**Operation:** Determinant of A

**Output:**
```
──────────────────────────────────────────────────────
MATRIX DETERMINANT
──────────────────────────────────────────────────────

Matrix A:
─────────────────────────────────────────
│        4.0000 │        7.0000 │
│        2.0000 │        6.0000 │
─────────────────────────────────────────
Shape: 2 × 2

Determinant of A: 4.000000

✓ Operation completed successfully!

Calculation: (4×6) - (7×2) = 24 - 14 = 10
```

### Example 4: Error Handling

**Scenario:** Attempting matrix multiplication with incompatible dimensions

**Input:**
```
Matrix A: 2×3
Matrix B: 2×2
```

**Output:**
```
❌ Error: Incompatible dimensions for multiplication!
   Matrix A: (2, 3), Matrix B: (2, 2)
   For A × B: A's columns (3) must equal B's rows (2)
```

---

## How to Run

### Prerequisites
- Python 3.7 or higher
- NumPy library (version ≥ 1.21.0)

### Installation

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the Application:**
```bash
python matrix_operations_tool.py
```

### Usage Flow

1. **Start the application** - Main menu appears
2. **Input matrices** - Select option 1 or 2 to input matrices A and B
3. **Select operation** - Choose from menu options 4-10
4. **View results** - Formatted output displays with clear labeling
5. **Repeat or exit** - Continue with more operations or select option 13 to exit

---

## Key Features Explained

### Menu Structure
```
1. Input Matrix A          - Add or modify first matrix
2. Input Matrix B          - Add or modify second matrix
3. View Current Matrices   - Display stored matrices A and B
4. Matrix Addition         - A + B
5. Matrix Subtraction      - A - B
6. Matrix Multiplication   - A × B
7. Matrix Transpose        - A^T or B^T
8. Determinant             - det(A) or det(B)
9. Matrix Inverse          - A^-1 or B^-1
10. Matrix Trace           - trace(A) or trace(B)
11. View Operation History - See all performed operations
12. Clear All Data         - Reset matrices and history
13. Exit                   - Quit application
```

### Validation Checks

| Check | Condition | Error Message |
|-------|-----------|---------------|
| Dimension Size | > 100 | "Maximum matrix size is 100×100" |
| Element Count | Row elements ≠ cols | "Expected X elements, got Y" |
| Matrix Compatibility | Different shapes for +/- | "Matrices must have same dimensions" |
| Matrix Type | Non-square for det/inv/trace | "Only works on square matrices" |
| Multiplication | A.cols ≠ B.rows | "Incompatible dimensions for multiplication" |
| Singularity | det = 0 | "Matrix is singular (inverse doesn't exist)" |

---

## Code Quality

### Comments and Documentation
- **Header Documentation**: File-level docstring explaining purpose
- **Class Documentation**: Class docstrings with purpose and functionality
- **Method Documentation**: Detailed docstrings for each method
- **Inline Comments**: Key sections explained with comments
- **Type Hints**: Function signatures include parameter and return types

### Error Handling
- Comprehensive try-except blocks
- Pre-operation validation
- User-friendly error messages
- Graceful degradation on errors

### Code Organization
- Modular design with single-responsibility methods
- Clear separation of UI, input, and computation logic
- Consistent naming conventions
- Proper encapsulation within class

---

## Technical Specifications

### Matrix Dimensions
- **Minimum**: 1×1
- **Maximum**: 100×100 (for performance)
- **Storage**: NumPy arrays (efficient C-backed arrays)

### Numerical Precision
- **Display Format**: 4 decimal places
- **Internal Precision**: Float64 (NumPy default)
- **Rounding**: Automatic via NumPy functions

### Performance Characteristics
- **Matrix Addition/Subtraction**: O(m×n)
- **Matrix Multiplication**: O(m×n×p)
- **Determinant**: O(n³) using LU decomposition
- **Inverse**: O(n³) using Gaussian elimination
- **Trace**: O(n)

---

## Future Enhancements

Potential features for expansion:
1. **File I/O**: Save/load matrices from files
2. **Batch Operations**: Perform multiple operations in sequence
3. **Advanced Operations**: Eigenvalues, QR decomposition, SVD
4. **Visualization**: Plot matrices using Matplotlib
5. **Linear Systems**: Solve Ax = b systems
6. **Matrix Decomposition**: LU, Cholesky, eigenvalue decomposition
7. **Export Results**: Save results to CSV or PDF

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'numpy'"
**Solution**: Install NumPy using `pip install numpy`

### Issue: "Matrix is singular"
**Solution**: The matrix's determinant is zero, so it cannot be inverted. Choose a different matrix.

### Issue: "Incompatible dimensions"
**Solution**: Check that matrix dimensions are compatible for the selected operation. Refer to the operation requirements in the features section.

### Issue: Input not accepting numbers
**Solution**: Ensure you're entering numbers separated by spaces for matrix elements, not commas.

---

## Conclusion

The Matrix Operations Tool provides a comprehensive, user-friendly interface for performing linear algebra operations using NumPy. With robust error handling, clear output formatting, and an intuitive menu system, it serves as both a practical computational tool and an educational resource for understanding matrix mathematics.

The modular design allows for easy extension and modification, while the comprehensive documentation makes the code maintainable and understandable for future developers.

---

## References

- **NumPy Documentation**: https://numpy.org/doc/
- **Linear Algebra Concepts**: https://en.wikipedia.org/wiki/Linear_algebra
- **Matrix Operations**: https://numpy.org/doc/stable/reference/routines.linalg.html

---

**Version**: 1.0  
**Author**: Matrix Operations Tool Development Team  
**Date**: 2026  
**License**: Open Source
