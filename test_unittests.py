import unittest
from main import format_equation, solve_equation
import sympy

class TestEquationSolver(unittest.TestCase):
    
    def test_format_equation(self):
        self.assertEqual(format_equation('2x + 3 = 5'),  '2**x+3=-2')
        self.assertEqual(format_equation('3x - 4 = 10'), '3**x-4=-6')
        self.assertEqual(format_equation('-5x + 2 = 3'), '-5**x+2=-1')
    
    def test_solve_equation(self):
        x = sympy.Symbol('x')
        
        # Test a simple equation
        solution = solve_equation('2x + 3 = 5')
        expected_solution = f"Solution:\n\n   2 x + 3 = 5\n\n1. Move all terms to the left-hand side:\n   2 x - 2 = 0\n\n2. Simplify:\n   2 x - 2 = 0\n\n   3. Solve for x:\n   x = 1"
        self.assertEqual(solution, expected_solution)
        
        # Test another equation
        solution = solve_equation('-5x + 2 = 3')
        expected_solution = f"Solution:\n\n   -5 x + 2 = 3\n\n1. Move all terms to the left-hand side:\n   -5 x - 1 = 0\n\n2. Simplify:\n   -5 x - 1 = 0\n\n   3. Solve for x:\n   x = -1/5"
        self.assertEqual(solution, expected_solution)
        
        # Test invalid equation
        with self.assertRaises(sympy.SympifyError):
            solve_equation('2x +')
        
if __name__ == '__main__':
    unittest.main()