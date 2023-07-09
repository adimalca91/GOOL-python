
'''
Time Complexity is: O(exp)
'''
def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)

'''
Time Complexity is: O(2^n) - NOT GOOD! Use the iterative implementation instead, O(n).
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)