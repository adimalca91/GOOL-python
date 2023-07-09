''' While loops '''
''' If the number of iterations in unknown a head you would rather use while loops '''

def while_factorial():

    num = int(input("Please Enter a Number: "))
    is_num = num
    factorial_num = 1


    while(is_num):
        factorial_num *= is_num
        is_num -= 1
    print(f"Factorial of {num} is {factorial_num}")


''' For loops '''
''' If the number of iterations is well known you would rather use for loop '''

def for_factorial():
    num = int(input("Please Enter a Number: "))
    factorial_num = 1
    for i in range(2, num+1):
        factorial_num *= i
    print(f"Factorial of {num} is {factorial_num}")


# for_factorial()

''' The range() function in Python '''

def rng_func():
    print(range(1,5))
    for i in range(1,10,2):
        print(i)

def rng_factorial():
    num = int(input("Please Enter a Number: "))
    factorial_num = 1
    for i in range(1, num+1):
        factorial_num *= i
    print(f"Factorial of {num} is {factorial_num}")

def display_inline():
    n = 4
    for i in range(n):
        print("*", end='') # If had not added the end attribute with empty string the default is new line

''' The operations of break and continue '''
''' These operations can change the flow of the loops '''

''' Nested Loops '''

def display_square(num):
    for i in range(num):
        for j in range(num):
            print('*', end='')
        print()

def seq_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    print(f"Sum of seq {n} is {sum}")

def seven_boom():
    num = int(input("Please Enter a Number: "))
    while(num % 7 != 0):
        num = int(input("Please Enter a Number: "))
    else:
        print("Boom")

def create_opp_numer(num):
    res = 0
    while(num):
        digit = num % 10
        num = num // 10
        res = res*10 + digit
    print(res)

''' Fibonacci Numbers '''

def fibonacci_numbers(num):
    n1 = 0
    n2 = 1
    for i in range(num-1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(n3)

    # a = 0
    # b = 1
    # if num < 0:
    #     print("Please enter a positive number")
    # elif num ==0:
    #     print(f"Fibonacci number {num} = {a}")
    # elif num == 1:
    #     print(f"Fibonacci number {num} = {b}")
    # else:
    #     for i in range(num-1):
    #         a, b = b, a+b
    #     print(f"Fibonacci number {num} = {b}")


def is_primary(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

'''
Note: A composite number must have a factor less than or equal to the square root of
that number. Otherwise, the number is prime.
Therefore, to optimize this code to be O(sqrt(n)) instead of O(n) we can run
in the range until sqrt(n) - like this: range(2, int(n**0.5))
'''

