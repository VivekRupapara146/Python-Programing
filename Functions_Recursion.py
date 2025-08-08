'''
    syntax:
define:     def func1():
                //body_code
call:       func1()
parameters and return values

risk of infinite calling

'''

def greet(name):
    gr = "Hello "+ name
    return gr

name = input("Enter your name: ")

a = greet(name)
print(a)

'''
RECURSION
 A function calling itself
factorial, sum of n, etc.
'''
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


x = int(input("Enter a number to find factorial: "))

fact = fact(x)

print(f"Factorial of {x} is {fact}")