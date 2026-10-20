# Write a program to find the roots of a quadratic equation  

import cmath

def find_roots(a, b, c):
    if a == 0:
        if b != 0:
            return f"This is a linear equation. The root is: {-c / b}"
        else:
            return "Invalid equation (no solution)."

    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return f"Two distinct real roots:\nRoot 1 = {root1:.2f}\nRoot 2 = {root2:.2f}"
    
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One repeated real root:\nRoot = {root:.2f}"
    
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return f"Two complex roots:\nRoot 1 = {root1:.2f}\nRoot 2 = {root2:.2f}"


print("Quadratic Equation Solver (ax² + bx + c = 0)")
try:
    coeff_a = float(input("Enter coefficient a: "))
    coeff_b = float(input("Enter coefficient b: "))
    coeff_c = float(input("Enter coefficient c: "))
    
    result = find_roots(coeff_a, coeff_b, coeff_c)
    print("\n--- Results ---")
    print(result)

except ValueError:
    print("Please enter valid numerical values.")
