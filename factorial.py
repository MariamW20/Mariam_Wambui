def factorial_recursive(n):
    
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
 # Main solution
number = 5

result_recursive = factorial_recursive(number)
print(f"Factorial of {number}: {result_recursive}")