# Quick Start Guide

## Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python matrix_operations_tool.py
```

---

## Basic Tutorial

### Getting Started

When you run the application, you'll see:
```
======================================================================
                    MATRIX OPERATIONS TOOL
               Powered by NumPy - Matrix Mathematics
======================================================================

----------------------------------------------------------------------
MAIN MENU - Select an operation:
----------------------------------------------------------------------
1.  Input Matrix A
2.  Input Matrix B
3.  View Current Matrices
4.  Matrix Addition (A + B)
5.  Matrix Subtraction (A - B)
6.  Matrix Multiplication (A × B)
7.  Matrix Transpose (A^T or B^T)
8.  Determinant (A or B)
9.  Matrix Inverse (A^-1 or B^-1)
10. Matrix Trace (A or B)
11. View Operation History
12. Clear All Data
13. Exit
----------------------------------------------------------------------

Enter your choice (1-13):
```

---

## Step-by-Step Examples

### Example 1: Basic Matrix Addition

**Goal**: Add two 2×2 matrices

1. **Select Option 1** to input Matrix A
   ```
   Enter number of rows: 2
   Enter number of columns: 2
   Enter elements of the 2×2 matrix:
   Row 1: 1 2
   Row 2: 3 4
   ✓ Matrix A input successfully (2×2)
   ```

2. **Select Option 2** to input Matrix B
   ```
   Enter number of rows: 2
   Enter number of columns: 2
   Enter elements of the 2×2 matrix:
   Row 1: 5 6
   Row 2: 7 8
   ✓ Matrix B input successfully (2×2)
   ```

3. **Select Option 4** for Addition
   ```
   Matrix A:
   ─────────────────────────────────────────
   │        1.0000 │        2.0000 │
   │        3.0000 │        4.0000 │
   ─────────────────────────────────────────
   Shape: 2 × 2

   Matrix B:
   ─────────────────────────────────────────
   │        5.0000 │        6.0000 │
   │        7.0000 │        8.0000 │
   ─────────────────────────────────────────
   Shape: 2 × 2

   Result (A + B):
   ─────────────────────────────────────────
   │        6.0000 │        8.0000 │
   │       10.0000 │       12.0000 │
   ─────────────────────────────────────────
   Shape: 2 × 2

   ✓ Operation completed successfully!
   ```

---

### Example 2: Matrix Multiplication

**Goal**: Multiply a 2×3 matrix by a 3×2 matrix

1. **Input Matrix A** (2×3):
   ```
   Enter number of rows: 2
   Enter number of columns: 3
   Row 1: 1 2 3
   Row 2: 4 5 6
   ```

2. **Input Matrix B** (3×2):
   ```
   Enter number of rows: 3
   Enter number of columns: 2
   Row 1: 7 8
   Row 2: 9 10
   Row 3: 11 12
   ```

3. **Select Option 6** for Multiplication
   ```
   Result (A × B):
   ─────────────────────────────────────────
   │       58.0000 │       64.0000 │
   │      139.0000 │      154.0000 │
   ─────────────────────────────────────────
   Shape: 2 × 2
   ```

---

### Example 3: Matrix Determinant

**Goal**: Calculate determinant of a 3×3 matrix

1. **Input a 3×3 Square Matrix**:
   ```
   Row 1: 1 2 3
   Row 2: 0 1 4
   Row 3: 5 1 0
   ```

2. **Select Option 8** for Determinant
   ```
   Enter choice (1 or 2): 1
   
   Determinant of A: 1.000000
   
   ✓ Operation completed successfully!
   ```

---

### Example 4: Matrix Transpose

**Goal**: Transpose a 2×3 matrix

1. **Input a 2×3 Matrix**:
   ```
   Row 1: 1 2 3
   Row 2: 4 5 6
   ```

2. **Select Option 7** for Transpose
   ```
   Choose matrix to transpose:
   1. Matrix A
   2. Matrix B
   Enter choice (1 or 2): 1
   
   Original Matrix A:
   ─────────────────────────────────────────
   │        1.0000 │        2.0000 │        3.0000 │
   │        4.0000 │        5.0000 │        6.0000 │
   ─────────────────────────────────────────
   Shape: 2 × 3

   Transposed Matrix A (A^T):
   ─────────────────────────────────────────
   │        1.0000 │        4.0000 │
   │        2.0000 │        5.0000 │
   │        3.0000 │        6.0000 │
   ─────────────────────────────────────────
   Shape: 3 × 2
   ```

---

### Example 5: Matrix Inverse

**Goal**: Find the inverse of a 2×2 matrix

1. **Input a 2×2 Invertible Matrix**:
   ```
   Row 1: 4 7
   Row 2: 2 6
   ```

2. **Select Option 9** for Inverse
   ```
   Choose matrix for inverse calculation:
   1. Matrix A
   2. Matrix B
   Enter choice (1 or 2): 1
   
   Original Matrix A:
   ─────────────────────────────────────────
   │        4.0000 │        7.0000 │
   │        2.0000 │        6.0000 │
   ─────────────────────────────────────────
   Shape: 2 × 2

   Inverse of A (A^-1):
   ─────────────────────────────────────────
   │        0.6000 │       -0.7000 │
   │       -0.2000 │        0.4000 │
   ─────────────────────────────────────────
   Shape: 2 × 2
   
   ✓ Operation completed successfully!
   ```

---

### Example 6: Matrix Trace

**Goal**: Calculate trace of a 3×3 matrix

1. **Input a 3×3 Square Matrix**:
   ```
   Row 1: 1 2 3
   Row 2: 4 5 6
   Row 3: 7 8 9
   ```

2. **Select Option 10** for Trace
   ```
   Choose matrix for trace calculation:
   1. Matrix A
   2. Matrix B
   Enter choice (1 or 2): 1
   
   Matrix A:
   ─────────────────────────────────────────
   │        1.0000 │        2.0000 │        3.0000 │
   │        4.0000 │        5.0000 │        6.0000 │
   │        7.0000 │        8.0000 │        9.0000 │
   ─────────────────────────────────────────
   Shape: 3 × 3

   Trace of A (sum of diagonal elements): 15.000000
   Diagonal elements: [1. 5. 9.]
   
   ✓ Operation completed successfully!
   ```

---

## Common Input Formats

### Valid Input Examples
```
Row with integers:
1 2 3 4

Row with decimals:
1.5 2.3 3.7 4.2

Row with mixed:
1 2.5 3 4.7

Row with negative numbers:
-1 2 -3 4
```

### Input Tips
- **Separate values with spaces** (not commas)
- **Press Enter after each row**
- **Use decimals where needed** (automatic conversion)
- **Negative numbers are supported**

---

## Error Handling Guide

### Error: "Matrices must have the same dimensions for addition!"
**What went wrong**: Matrix A and B have different sizes
**Solution**: Input matrices with matching dimensions

### Error: "Incompatible dimensions for multiplication!"
**What went wrong**: Number of columns in A ≠ number of rows in B
**Solution**: For A × B, A's columns must equal B's rows

### Error: "Determinant only works on square matrices!"
**What went wrong**: Matrix is not n×n
**Solution**: Input a square matrix (same rows and columns)

### Error: "Matrix is singular (inverse doesn't exist)!"
**What went wrong**: Determinant is zero
**Solution**: The matrix cannot be inverted (try a different matrix)

### Error: "Expected 3 elements, got 2!"
**What went wrong**: Row has wrong number of elements
**Solution**: Enter exactly the number of elements specified for columns

---

## Tips & Tricks

1. **View Stored Matrices**: Use Option 3 anytime to see your matrices
2. **Check History**: Use Option 11 to see all operations performed
3. **Multiple Operations**: Keep matrices and perform different operations
4. **Reset Everything**: Use Option 12 to clear and start fresh
5. **Precise Output**: Results show 4 decimal places for readability

---

## Practice Exercises

### Exercise 1: Vector Dot Product
Create two 1×3 matrices and multiply them:
- A = [1 2 3]
- B^T = [4; 5; 6]
- Result = A × B^T = 32

### Exercise 2: Identity Matrix Verification
Create an invertible 2×2 matrix and its inverse:
- Check that A × A^-1 ≈ Identity Matrix

### Exercise 3: Matrix Properties
Input a 3×3 matrix and verify:
- Transpose of transpose = original matrix
- Trace calculation manually vs. tool result

### Exercise 4: Determinant Calculation
Test determinant with:
- Singular matrix (det = 0)
- Non-singular matrix (det ≠ 0)
- Observe the relationship with invertibility

---

## Keyboard Shortcuts

- **Ctrl+C**: Exit the application at any time
- **Enter**: Confirm input or continue from menu

---

## Troubleshooting

**Q: Application crashes after input**
A: Check that all values are numbers. Letters or special characters (except minus sign) will cause errors.

**Q: Matrix displays are misaligned**
A: This is normal for very large numbers. Values are formatted with 4 decimal places.

**Q: Can I use very large matrices (1000×1000)?**
A: The tool limits matrices to 100×100 for performance. Larger matrices will be rejected.

**Q: How do I input a matrix with decimal values?**
A: Just type the numbers with decimals separated by spaces: `1.5 2.3 3.7`

---

## Advanced Usage

### Chaining Operations
1. Input two matrices
2. Perform addition (save result mentally)
3. Perform multiplication with same matrices
4. Compare results

### Verifying Mathematical Properties
- Verify associativity: (A + B) + C = A + (B + C)
- Check commutativity: A + B = B + A (addition is commutative)
- Note: A × B ≠ B × A (multiplication is NOT commutative)

---

For detailed documentation, see **README.md**

Happy calculating! 🔢
