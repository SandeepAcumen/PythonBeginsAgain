#https://prepinsta.com/interview-preparation/technical-interview-questions/most-asked-coding-questions-in-placements/

#Coding Interview

#1. Write a code to reverse a number
'''
def reverse():
    num = 12345
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    print("Reversed Number:", rev)

reverse()

'''
#or
'''
no =12345
rev =int(str(no)[::-1])
print(rev)
    
'''

#2. Write the code to find the Fibonacci series upto the nth term.

#3. Write code of Greatest Common Divisor

num1 = int(input("Enter First Number:"))
num2 =int(input("Enter second Number:"))

def gcdF(num1,num2):
    if num1 >num2:
        small =num2
    else:
        small = num1

    for i in range(1,small +1):
        if (num1 % i == 0) and (num2 % i ==0):
            gcd = i

    print("GCD of two number:{}".format(gcd))

gcdF(num1,num2)
