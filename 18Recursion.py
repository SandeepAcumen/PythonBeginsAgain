#recursion is a function calling itself to solve a problem
'''
to solve Fubanacci seriees 0 1 1 2 3 5 8 13

fib(0)  = 0
fib(1) = 1
fib(2) =fib(0) +fib(1)
fib(3) = fib(1) + fib(2)
fib(n) = fib(n-2) + fib(n-1)

'''

def fib(n):
    if(n==0 or n==1):
        return n

    return fib(n-2) + fib(n-1)
print(fib(5))
#print(fib(50))   # wont work because For fib(50), it makes over 20 billion recursive calls 😵

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 51
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
