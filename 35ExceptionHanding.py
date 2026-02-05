'''
while True:
    try:
        a = int(input("Enter the number 1 :"))
        b  = int(input("Enter the number 2 :"))

        print((f"the sum is { a + b}"))
    except:
        print("Data entried is wrong")
'''
'''
while True:
    try:
        a = int(input("Enter the number 1 :"))
        b  = int(input("Enter the number 2 :"))

        print((f"the sum is { a / b}"))

        
    except ValueError:
        print("Please dont perform bad typecases")

    except ZeroDivisionError:
        print("Hey dont divide by 0")

    except Exception as e:
        print("Unknown error occurred!!" , e)

'''

'''
a = int(input("Enter the number 1 :"))
b  = int(input("Enter the number 2 :"))

if b==0:
    raise ValueError("Please dont divide by 0")

print((f"the sum is { a / b}"))

'''

'''
a = int(input("Enter the number 1 :"))
b  = int(input("Enter the number 2 :"))

try:
    c= a/b
    print(c)

except Exception as e:
    print(e)

finally:
    print("This is always executed")

'''


