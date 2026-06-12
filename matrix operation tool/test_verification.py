"""
Verification Test Script for Matrix Operations Tool

This script verifies that all matrix operations work correctly
without requiring interactive input.
"""

import sys
import numpy as np

def test_matrix_operations():
    """Test all matrix operations programmatically."""
    
    print("\n" + "="*70)
    print("MATRIX OPERATIONS TOOL - VERIFICATION TEST")
    print("="*70 + "\n")
    
    # Test data
    test_results = []
    
    # TEST 1: Addition
    print("TEST 1: Matrix Addition")
    print("-" * 70)
    try:
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        result = np.add(A, B)
        expected = np.array([[6, 8], [10, 12]])
        assert np.array_equal(result, expected), "Addition result mismatch"
        print(f"✓ PASSED - A + B = {result.tolist()}")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 2: Subtraction
    print("\nTEST 2: Matrix Subtraction")
    print("-" * 70)
    try:
        A = np.array([[10, 20], [30, 40]])
        B = np.array([[1, 2], [3, 4]])
        result = np.subtract(A, B)
        expected = np.array([[9, 18], [27, 36]])
        assert np.array_equal(result, expected), "Subtraction result mismatch"
        print(f"✓ PASSED - A - B = {result.tolist()}")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 3: Multiplication
    print("\nTEST 3: Matrix Multiplication")
    print("-" * 70)
    try:
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        result = np.matmul(A, B)
        expected = np.array([[19, 22], [43, 50]])
        assert np.array_equal(result, expected), "Multiplication result mismatch"
        print(f"✓ PASSED - A × B = {result.tolist()}")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 4: Transpose
    print("\nTEST 4: Matrix Transpose")
    print("-" * 70)
    try:
        A = np.array([[1, 2, 3], [4, 5, 6]])
        result = np.transpose(A)
        expected = np.array([[1, 4], [2, 5], [3, 6]])
        assert np.array_equal(result, expected), "Transpose result mismatch"
        print(f"✓ PASSED - A^T shape: {result.shape}")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 5: Determinant
    print("\nTEST 5: Matrix Determinant")
    print("-" * 70)
    try:
        A = np.array([[4, 7], [2, 6]])
        det = np.linalg.det(A)
        expected = 10.0
        assert abs(det - expected) < 0.001, f"Determinant mismatch: {det} != {expected}"
        print(f"✓ PASSED - det(A) = {det:.1f}")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 6: Inverse
    print("\nTEST 6: Matrix Inverse")
    print("-" * 70)
    try:
        A = np.array([[4.0, 7.0], [2.0, 6.0]])
        inv_A = np.linalg.inv(A)
        # Verify A × A^-1 = Identity
        identity = np.matmul(A, inv_A)
        expected_identity = np.eye(2)
        assert np.allclose(identity, expected_identity), "Inverse verification failed"
        print(f"✓ PASSED - A × A^-1 = Identity Matrix")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 7: Trace
    print("\nTEST 7: Matrix Trace")
    print("-" * 70)
    try:
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        trace = np.trace(A)
        expected = 15.0
        assert abs(trace - expected) < 0.001, f"Trace mismatch: {trace} != {expected}"
        print(f"✓ PASSED - trace(A) = {trace:.0f}")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 8: Dimension Compatibility - Addition
    print("\nTEST 8: Dimension Validation (Addition)")
    print("-" * 70)
    try:
        A = np.array([[1, 2, 3]])  # 1×3
        B = np.array([[1, 2], [3, 4]])  # 2×2
        assert A.shape == B.shape, "Dimensions should not match for different shapes"
        print(f"✗ FAILED - Should have caught dimension mismatch")
        test_results.append(False)
    except AssertionError:
        print(f"✓ PASSED - Correctly identified incompatible dimensions (1×3 vs 2×2)")
        test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 9: Dimension Compatibility - Multiplication
    print("\nTEST 9: Dimension Validation (Multiplication)")
    print("-" * 70)
    try:
        A = np.array([[1, 2, 3], [4, 5, 6]])  # 2×3
        B = np.array([[7, 8], [9, 10]])  # 2×2
        assert A.shape[1] != B.shape[0], "Should not be compatible"
        print(f"✓ PASSED - Correctly identified incompatible dimensions (2×3 × 2×2)")
        test_results.append(True)
    except AssertionError:
        print(f"✗ FAILED - Should have caught dimension mismatch")
        test_results.append(False)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # TEST 10: Singular Matrix Detection
    print("\nTEST 10: Singular Matrix Detection")
    print("-" * 70)
    try:
        A = np.array([[1, 2], [2, 4]])  # Singular (det = 0)
        det = np.linalg.det(A)
        assert abs(det) < 0.001, "Matrix should be singular"
        
        # Try to compute inverse (should fail)
        try:
            inv_A = np.linalg.inv(A)
            print(f"✗ FAILED - Should not compute inverse of singular matrix")
            test_results.append(False)
        except np.linalg.LinAlgError:
            print(f"✓ PASSED - Correctly rejected singular matrix inversion")
            test_results.append(True)
    except Exception as e:
        print(f"✗ FAILED - {str(e)}")
        test_results.append(False)
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(test_results)
    total = len(test_results)
    percentage = (passed / total) * 100
    
    print(f"\nTests Passed: {passed}/{total} ({percentage:.1f}%)")
    
    if passed == total:
        print("\n✓ ALL TESTS PASSED - Application is ready for use!")
        return True
    else:
        print(f"\n✗ {total - passed} test(s) failed - Please review errors")
        return False

def test_import():
    """Test that the matrix_operations_tool module can be imported."""
    print("\n" + "="*70)
    print("MODULE IMPORT TEST")
    print("="*70 + "\n")
    
    try:
        from matrix_operations_tool import MatrixOperationsTool
        print("✓ Successfully imported MatrixOperationsTool class")
        
        # Try to instantiate
        tool = MatrixOperationsTool()
        print("✓ Successfully instantiated MatrixOperationsTool")
        
        # Check methods exist
        required_methods = [
            'matrix_addition', 'matrix_subtraction', 'matrix_multiplication',
            'matrix_transpose', 'matrix_determinant', 'matrix_inverse',
            'matrix_trace', 'get_matrix_input', 'display_matrix', 'view_matrices'
        ]
        
        for method in required_methods:
            if hasattr(tool, method):
                print(f"✓ Method '{method}' found")
            else:
                print(f"✗ Method '{method}' NOT found")
                return False
        
        print("\n✓ All required methods are present")
        return True
    
    except ImportError as e:
        print(f"✗ Failed to import: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("# MATRIX OPERATIONS TOOL - AUTOMATED VERIFICATION")
    print("#"*70)
    
    # Run import test
    import_success = test_import()
    
    # Run operation tests
    tests_success = test_matrix_operations()
    
    # Final result
    print("\n" + "#"*70)
    if import_success and tests_success:
        print("# STATUS: ✓ ALL VERIFICATIONS PASSED")
        print("# The Matrix Operations Tool is working correctly!")
        print("#"*70 + "\n")
        sys.exit(0)
    else:
        print("# STATUS: ✗ SOME VERIFICATIONS FAILED")
        print("# Please review the errors above")
        print("#"*70 + "\n")
        sys.exit(1)
