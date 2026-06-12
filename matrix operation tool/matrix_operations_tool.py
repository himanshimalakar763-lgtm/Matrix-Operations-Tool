"""
Matrix Operations Tool - A NumPy-based Interactive Application

This application provides an interactive interface for performing various matrix operations.
Users can input matrices and perform operations such as addition, subtraction, multiplication,
transpose, determinant calculation, matrix inverse, and trace calculation.

Author: Matrix Operations Tool
Date: 2026
"""

import numpy as np
import sys
from typing import Tuple, Optional, Union
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


class MatrixOperationsTool:
    """
    A class to handle matrix operations using NumPy.
    
    This class provides methods for inputting matrices, validating dimensions,
    and performing various matrix mathematical operations.
    """
    
    def __init__(self):
        """Initialize the Matrix Operations Tool."""
        self.matrix_a = None
        self.matrix_b = None
        self.operation_history = []
    
    def clear_screen(self) -> None:
        """Clear the console screen."""
        import os
        os.system('cls' if sys.platform == 'win32' else 'clear')
    
    def display_header(self) -> None:
        """Display the application header."""
        print("\n" + "="*70)
        print(" "*15 + "MATRIX OPERATIONS TOOL")
        print(" "*10 + "Powered by NumPy - Matrix Mathematics")
        print("="*70 + "\n")
    
    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\n" + "-"*70)
        print("MAIN MENU - Select an operation:")
        print("-"*70)
        print("1.  Input Matrix A")
        print("2.  Input Matrix B")
        print("3.  View Current Matrices")
        print("4.  Matrix Addition (A + B)")
        print("5.  Matrix Subtraction (A - B)")
        print("6.  Matrix Multiplication (A × B)")
        print("7.  Matrix Transpose (A^T or B^T)")
        print("8.  Determinant (A or B)")
        print("9.  Matrix Inverse (A^-1 or B^-1)")
        print("10. Matrix Trace (A or B)")
        print("11. View Operation History")
        print("12. Clear All Data")
        print("13. Exit")
        print("-"*70)
    
    def get_matrix_input(self) -> Tuple[int, int, np.ndarray]:
        """
        Get matrix dimensions and elements from user input.
        
        Returns:
            Tuple containing (rows, columns, matrix as numpy array)
            
        Raises:
            ValueError: If input dimensions or values are invalid
        """
        print("\n" + "="*70)
        print("MATRIX INPUT")
        print("="*70)
        
        try:
            # Get matrix dimensions
            while True:
                try:
                    rows = int(input("Enter number of rows: "))
                    cols = int(input("Enter number of columns: "))
                    
                    if rows <= 0 or cols <= 0:
                        print("❌ Error: Dimensions must be positive integers!")
                        continue
                    
                    if rows > 100 or cols > 100:
                        print("❌ Error: Maximum matrix size is 100x100 for performance!")
                        continue
                    
                    break
                except ValueError:
                    print("❌ Error: Please enter valid integer values!")
            
            # Get matrix elements
            print(f"\nEnter elements of the {rows}×{cols} matrix:")
            print("(Enter row by row, separated by spaces)")
            print("Example for 2x2 matrix: 1 2 (enter) 3 4 (enter)\n")
            
            matrix_data = []
            for i in range(rows):
                while True:
                    try:
                        row_input = input(f"Row {i+1}: ").strip()
                        
                        if not row_input:
                            print("❌ Error: Row cannot be empty!")
                            continue
                        
                        row = list(map(float, row_input.split()))
                        
                        if len(row) != cols:
                            print(f"❌ Error: Expected {cols} elements, got {len(row)}!")
                            continue
                        
                        matrix_data.append(row)
                        break
                    except ValueError:
                        print("❌ Error: Please enter valid numbers!")
            
            matrix = np.array(matrix_data, dtype=float)
            return rows, cols, matrix
        
        except KeyboardInterrupt:
            print("\n❌ Input cancelled by user")
            return None, None, None
    
    def display_matrix(self, matrix: np.ndarray, label: str = "Matrix") -> None:
        """
        Display a matrix in a formatted table.
        
        Args:
            matrix: NumPy array to display
            label: Label for the matrix
        """
        print(f"\n{label}:")
        print("-" * (15 * matrix.shape[1] + 2))
        
        # Format matrix for display
        np.set_printoptions(precision=4, suppress=True, linewidth=200)
        
        for row in matrix:
            print("│ " + " │ ".join(f"{val:>10.4f}" for val in row) + " │")
        
        print("-" * (15 * matrix.shape[1] + 2))
        print(f"Shape: {matrix.shape[0]} × {matrix.shape[1]}")
    
    def matrix_addition(self) -> None:
        """Perform matrix addition (A + B)."""
        if self.matrix_a is None or self.matrix_b is None:
            print("❌ Error: Both matrices must be input first!")
            return
        
        try:
            if self.matrix_a.shape != self.matrix_b.shape:
                print("❌ Error: Matrices must have the same dimensions for addition!")
                print(f"   Matrix A: {self.matrix_a.shape}, Matrix B: {self.matrix_b.shape}")
                return
            
            result = np.add(self.matrix_a, self.matrix_b)
            
            print("\n" + "="*70)
            print("MATRIX ADDITION: A + B")
            print("="*70)
            
            self.display_matrix(self.matrix_a, "Matrix A")
            print()
            self.display_matrix(self.matrix_b, "Matrix B")
            print()
            self.display_matrix(result, "Result (A + B)")
            
            self.operation_history.append(("Addition", self.matrix_a.copy(), self.matrix_b.copy(), result))
            print("\n✓ Operation completed successfully!")
        
        except Exception as e:
            print(f"❌ Error during addition: {str(e)}")
    
    def matrix_subtraction(self) -> None:
        """Perform matrix subtraction (A - B)."""
        if self.matrix_a is None or self.matrix_b is None:
            print("❌ Error: Both matrices must be input first!")
            return
        
        try:
            if self.matrix_a.shape != self.matrix_b.shape:
                print("❌ Error: Matrices must have the same dimensions for subtraction!")
                print(f"   Matrix A: {self.matrix_a.shape}, Matrix B: {self.matrix_b.shape}")
                return
            
            result = np.subtract(self.matrix_a, self.matrix_b)
            
            print("\n" + "="*70)
            print("MATRIX SUBTRACTION: A - B")
            print("="*70)
            
            self.display_matrix(self.matrix_a, "Matrix A")
            print()
            self.display_matrix(self.matrix_b, "Matrix B")
            print()
            self.display_matrix(result, "Result (A - B)")
            
            self.operation_history.append(("Subtraction", self.matrix_a.copy(), self.matrix_b.copy(), result))
            print("\n✓ Operation completed successfully!")
        
        except Exception as e:
            print(f"❌ Error during subtraction: {str(e)}")
    
    def matrix_multiplication(self) -> None:
        """Perform matrix multiplication (A × B)."""
        if self.matrix_a is None or self.matrix_b is None:
            print("❌ Error: Both matrices must be input first!")
            return
        
        try:
            # Check if dimensions are compatible for multiplication
            if self.matrix_a.shape[1] != self.matrix_b.shape[0]:
                print("❌ Error: Incompatible dimensions for multiplication!")
                print(f"   Matrix A: {self.matrix_a.shape}, Matrix B: {self.matrix_b.shape}")
                print(f"   For A × B: A's columns ({self.matrix_a.shape[1]}) must equal B's rows ({self.matrix_b.shape[0]})")
                return
            
            result = np.matmul(self.matrix_a, self.matrix_b)
            
            print("\n" + "="*70)
            print("MATRIX MULTIPLICATION: A × B")
            print("="*70)
            
            self.display_matrix(self.matrix_a, "Matrix A")
            print()
            self.display_matrix(self.matrix_b, "Matrix B")
            print()
            self.display_matrix(result, "Result (A × B)")
            
            self.operation_history.append(("Multiplication", self.matrix_a.copy(), self.matrix_b.copy(), result))
            print("\n✓ Operation completed successfully!")
        
        except Exception as e:
            print(f"❌ Error during multiplication: {str(e)}")
    
    def matrix_transpose(self) -> None:
        """Perform matrix transpose operation."""
        print("\n" + "="*70)
        print("MATRIX TRANSPOSE")
        print("="*70)
        
        print("\nChoose matrix to transpose:")
        print("1. Matrix A")
        print("2. Matrix B")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        try:
            if choice == '1':
                if self.matrix_a is None:
                    print("❌ Error: Matrix A has not been input!")
                    return
                
                result = np.transpose(self.matrix_a)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_a, "Original Matrix A")
                print()
                self.display_matrix(result, "Transposed Matrix A (A^T)")
                
                self.operation_history.append(("Transpose A", self.matrix_a.copy(), None, result))
                print("\n✓ Operation completed successfully!")
            
            elif choice == '2':
                if self.matrix_b is None:
                    print("❌ Error: Matrix B has not been input!")
                    return
                
                result = np.transpose(self.matrix_b)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_b, "Original Matrix B")
                print()
                self.display_matrix(result, "Transposed Matrix B (B^T)")
                
                self.operation_history.append(("Transpose B", self.matrix_b.copy(), None, result))
                print("\n✓ Operation completed successfully!")
            
            else:
                print("❌ Error: Invalid choice!")
        
        except Exception as e:
            print(f"❌ Error during transpose: {str(e)}")
    
    def matrix_determinant(self) -> None:
        """Calculate matrix determinant."""
        print("\n" + "="*70)
        print("MATRIX DETERMINANT")
        print("="*70)
        
        print("\nChoose matrix for determinant calculation:")
        print("1. Matrix A")
        print("2. Matrix B")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        try:
            if choice == '1':
                if self.matrix_a is None:
                    print("❌ Error: Matrix A has not been input!")
                    return
                
                if self.matrix_a.shape[0] != self.matrix_a.shape[1]:
                    print("❌ Error: Determinant only works on square matrices!")
                    print(f"   Matrix A is {self.matrix_a.shape[0]}×{self.matrix_a.shape[1]}")
                    return
                
                det = np.linalg.det(self.matrix_a)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_a, "Matrix A")
                print(f"\nDeterminant of A: {det:.6f}")
                
                self.operation_history.append(("Determinant A", self.matrix_a.copy(), None, det))
                print("\n✓ Operation completed successfully!")
            
            elif choice == '2':
                if self.matrix_b is None:
                    print("❌ Error: Matrix B has not been input!")
                    return
                
                if self.matrix_b.shape[0] != self.matrix_b.shape[1]:
                    print("❌ Error: Determinant only works on square matrices!")
                    print(f"   Matrix B is {self.matrix_b.shape[0]}×{self.matrix_b.shape[1]}")
                    return
                
                det = np.linalg.det(self.matrix_b)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_b, "Matrix B")
                print(f"\nDeterminant of B: {det:.6f}")
                
                self.operation_history.append(("Determinant B", self.matrix_b.copy(), None, det))
                print("\n✓ Operation completed successfully!")
            
            else:
                print("❌ Error: Invalid choice!")
        
        except np.linalg.LinAlgError:
            print("❌ Error: Singular matrix (determinant cannot be calculated)!")
        except Exception as e:
            print(f"❌ Error during determinant calculation: {str(e)}")
    
    def matrix_inverse(self) -> None:
        """Calculate matrix inverse."""
        print("\n" + "="*70)
        print("MATRIX INVERSE")
        print("="*70)
        
        print("\nChoose matrix for inverse calculation:")
        print("1. Matrix A")
        print("2. Matrix B")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        try:
            if choice == '1':
                if self.matrix_a is None:
                    print("❌ Error: Matrix A has not been input!")
                    return
                
                if self.matrix_a.shape[0] != self.matrix_a.shape[1]:
                    print("❌ Error: Inverse only works on square matrices!")
                    print(f"   Matrix A is {self.matrix_a.shape[0]}×{self.matrix_a.shape[1]}")
                    return
                
                det = np.linalg.det(self.matrix_a)
                if abs(det) < 1e-10:
                    print("❌ Error: Matrix is singular (determinant is zero, inverse doesn't exist)!")
                    return
                
                result = np.linalg.inv(self.matrix_a)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_a, "Original Matrix A")
                print()
                self.display_matrix(result, "Inverse of A (A^-1)")
                
                self.operation_history.append(("Inverse A", self.matrix_a.copy(), None, result))
                print("\n✓ Operation completed successfully!")
            
            elif choice == '2':
                if self.matrix_b is None:
                    print("❌ Error: Matrix B has not been input!")
                    return
                
                if self.matrix_b.shape[0] != self.matrix_b.shape[1]:
                    print("❌ Error: Inverse only works on square matrices!")
                    print(f"   Matrix B is {self.matrix_b.shape[0]}×{self.matrix_b.shape[1]}")
                    return
                
                det = np.linalg.det(self.matrix_b)
                if abs(det) < 1e-10:
                    print("❌ Error: Matrix is singular (determinant is zero, inverse doesn't exist)!")
                    return
                
                result = np.linalg.inv(self.matrix_b)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_b, "Original Matrix B")
                print()
                self.display_matrix(result, "Inverse of B (B^-1)")
                
                self.operation_history.append(("Inverse B", self.matrix_b.copy(), None, result))
                print("\n✓ Operation completed successfully!")
            
            else:
                print("❌ Error: Invalid choice!")
        
        except np.linalg.LinAlgError:
            print("❌ Error: Matrix is singular (inverse cannot be calculated)!")
        except Exception as e:
            print(f"❌ Error during inverse calculation: {str(e)}")
    
    def matrix_trace(self) -> None:
        """Calculate matrix trace."""
        print("\n" + "="*70)
        print("MATRIX TRACE")
        print("="*70)
        
        print("\nChoose matrix for trace calculation:")
        print("1. Matrix A")
        print("2. Matrix B")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        
        try:
            if choice == '1':
                if self.matrix_a is None:
                    print("❌ Error: Matrix A has not been input!")
                    return
                
                if self.matrix_a.shape[0] != self.matrix_a.shape[1]:
                    print("❌ Error: Trace only works on square matrices!")
                    print(f"   Matrix A is {self.matrix_a.shape[0]}×{self.matrix_a.shape[1]}")
                    return
                
                trace = np.trace(self.matrix_a)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_a, "Matrix A")
                print(f"\nTrace of A (sum of diagonal elements): {trace:.6f}")
                
                diagonal_elements = np.diag(self.matrix_a)
                print(f"Diagonal elements: {diagonal_elements}")
                
                self.operation_history.append(("Trace A", self.matrix_a.copy(), None, trace))
                print("\n✓ Operation completed successfully!")
            
            elif choice == '2':
                if self.matrix_b is None:
                    print("❌ Error: Matrix B has not been input!")
                    return
                
                if self.matrix_b.shape[0] != self.matrix_b.shape[1]:
                    print("❌ Error: Trace only works on square matrices!")
                    print(f"   Matrix B is {self.matrix_b.shape[0]}×{self.matrix_b.shape[1]}")
                    return
                
                trace = np.trace(self.matrix_b)
                
                print("\n" + "-"*70)
                self.display_matrix(self.matrix_b, "Matrix B")
                print(f"\nTrace of B (sum of diagonal elements): {trace:.6f}")
                
                diagonal_elements = np.diag(self.matrix_b)
                print(f"Diagonal elements: {diagonal_elements}")
                
                self.operation_history.append(("Trace B", self.matrix_b.copy(), None, trace))
                print("\n✓ Operation completed successfully!")
            
            else:
                print("❌ Error: Invalid choice!")
        
        except Exception as e:
            print(f"❌ Error during trace calculation: {str(e)}")
    
    def view_matrices(self) -> None:
        """Display current input matrices."""
        print("\n" + "="*70)
        print("CURRENT MATRICES")
        print("="*70)
        
        if self.matrix_a is not None:
            self.display_matrix(self.matrix_a, "Matrix A")
        else:
            print("\nMatrix A: Not input yet")
        
        print()
        
        if self.matrix_b is not None:
            self.display_matrix(self.matrix_b, "Matrix B")
        else:
            print("\nMatrix B: Not input yet")
    
    def view_history(self) -> None:
        """Display operation history."""
        print("\n" + "="*70)
        print("OPERATION HISTORY")
        print("="*70)
        
        if not self.operation_history:
            print("\nNo operations performed yet.")
            return
        
        for idx, (operation, *_) in enumerate(self.operation_history, 1):
            print(f"{idx}. {operation}")
    
    def clear_data(self) -> None:
        """Clear all stored matrices and history."""
        confirm = input("\nAre you sure you want to clear all data? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            self.matrix_a = None
            self.matrix_b = None
            self.operation_history = []
            print("✓ All data cleared successfully!")
        else:
            print("Operation cancelled.")
    
    def run(self) -> None:
        """Main application loop."""
        while True:
            self.display_header()
            self.display_menu()
            
            choice = input("\nEnter your choice (1-13): ").strip()
            
            if choice == '1':
                self.clear_screen()
                rows, cols, matrix = self.get_matrix_input()
                if matrix is not None:
                    self.matrix_a = matrix
                    print(f"\n✓ Matrix A input successfully ({rows}×{cols})")
            
            elif choice == '2':
                self.clear_screen()
                rows, cols, matrix = self.get_matrix_input()
                if matrix is not None:
                    self.matrix_b = matrix
                    print(f"\n✓ Matrix B input successfully ({rows}×{cols})")
            
            elif choice == '3':
                self.clear_screen()
                self.view_matrices()
            
            elif choice == '4':
                self.clear_screen()
                self.matrix_addition()
            
            elif choice == '5':
                self.clear_screen()
                self.matrix_subtraction()
            
            elif choice == '6':
                self.clear_screen()
                self.matrix_multiplication()
            
            elif choice == '7':
                self.clear_screen()
                self.matrix_transpose()
            
            elif choice == '8':
                self.clear_screen()
                self.matrix_determinant()
            
            elif choice == '9':
                self.clear_screen()
                self.matrix_inverse()
            
            elif choice == '10':
                self.clear_screen()
                self.matrix_trace()
            
            elif choice == '11':
                self.clear_screen()
                self.view_history()
            
            elif choice == '12':
                self.clear_screen()
                self.clear_data()
            
            elif choice == '13':
                print("\n" + "="*70)
                print("Thank you for using Matrix Operations Tool!")
                print("="*70 + "\n")
                sys.exit(0)
            
            else:
                print("❌ Error: Invalid choice! Please try again.")
            
            input("\n[Press Enter to continue...]")
            self.clear_screen()


def main():
    """Entry point for the application."""
    try:
        tool = MatrixOperationsTool()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n✓ Application terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
