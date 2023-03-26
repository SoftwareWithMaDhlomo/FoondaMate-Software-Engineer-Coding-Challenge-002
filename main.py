import sympy

#Algorithm to simplify input dtring to correct sympy format 

def format_equation(equation):
  
    #Split Equation Entered by the spaces
    splitInputString = equation.split(" ")
    
    #uncomment the line below if you wanna see what it looks like 
    #print(splitInputString)

    #Use this to get a by dropping the attached x 
    a = splitInputString[0].split("x")[0]
    
    #Use to get the sign of equation +/-
    sign = splitInputString[1]
    
    #use to get the b in the equation
    b = splitInputString[2]
    
    #use to get c of equatuion and ppass as number
    c = int(splitInputString[4])
    
    #Check of c moving to the left will be + or minus 
    if c > 0:
        c = str("-"+str(c))
    elif c < 0:
        c= "+"+ str(abs(int(c)))
    
    # return the fixed equation
    return str(a + '**x' + sign + b + c)   

 
def solve_equation(equation):
    x = sympy.Symbol('x')
    lhs, rhs = sympy.Eq(sympy.simplify(equation)).as_expr_with_vars(x)
    solution_steps = []
    
    # Move all terms to the left-hand side
    expression = lhs - rhs
    solution_steps.append(f"1. Move all terms to the left-hand side:\n   {sympy.latex(expression)} = 0")
    
    # Simplify
    expression = sympy.simplify(expression)
    solution_steps.append(f"2. Simplify:\n   {sympy.latex(expression)} = 0")
    
    # Solve for x
    x_solution = sympy.solve(expression, x)
    
    # Construct solution string
    solution = f"Solution:\n\n   {sympy.latex(lhs)} = {sympy.latex(rhs)}\n"
    for step in solution_steps:
        solution += f"\n{step}"
    solution += f"\n\n   3. Solve for x:\n   x = {sympy.latex(x_solution)}"
    return solution

if __name__ == '__main__':
    while True:
        equation = input("Enter a linear equation in the format 'ax + b = c' (or 'q' to quit): ")
        if equation == 'q':
            break
        try:
            # solution = solve_equation(equation)
            # print(solution)
            
            print(sympy.solve(format_equation(equation), sympy.Symbol('x')))
            
        except (sympy.SympifyError, ValueError) as e:
            print(f"Invalid equation: {str(e)}")
