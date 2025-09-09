#1
'''
number1 =40
number2 =30

number3 = number1*number2

while(number3 >1000):
    print(number1+number2)
    break
else:
    print(number3)

'''

#2
'''
previous_num = 0
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num = i
'''

#5
'''
x =[12,34,56,878,44,122]
first=x[0]
last =x[-1]

while(first==last):
    print(True)
    
else:
    print(False)

'''

#6
'''
list=[10,20,30,46,55,125,123,2356,568485]
for l in list:
    if l% 5==0:
        print(l)

'''

#7
'''
    
str_x ="Emma is good developer. Emma is a writer"

c =str_x.count("Emma")
print(f"Emma appeared {c} Times")

   ''' 

#8
'''
for num in range(6):
    for i in range(num):
        print(num, end =" ")

    print("\n")
'''

#9    
'''

no = input("Enter a number: ")

if no == no[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")

'''
#10
'''
def merge(list1,list2):
    result_list =[]

    for num in list1:
        if num %2 ==0:
            result_list.append(num)

    for num in list2:
        if num%2 ==1:
            result_list.append(num)

    return result_list

list1=[10,20,30,35,25]
list2=[40,45,60,75,90]

print("result list:" , merge(list1,list2))

'''

#11
'''
number  = 1234
while number> 0:
    digit = number %10
    number = number // 10
    print(digit,end  =" ")
'''
#12
'''
income = 45000
tax_payable = 0
print("Given income", income)
if income <= 10000:
    tax_payable = 0
elif income <= 20000:   
    x = income - 10000  
    tax_payable = x * 10 / 100
else:  
    tax_payable = 0    
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

    
'''

#13
'''
for i in range(1,11):
    for j in range(1,11):
        print(i*j ,end =" ")
    print(" ")

'''

#14
'''
for i in range(6,0,-1):
    for j in range(0,i-1):
        print("*" , end =' ')

    print(" ")
'''

#15
'''
base = int(input("Enter the base: "))
exponent =int(input("NEter the exponent: "))


answer =  base  ** exponent

print(answer)
'''


#16
'''
number = int(input("Enter the number : "))
original = number
reverse = 0

while number > 0:
    result = number % 10
    reverse = reverse * 10 + result
    number = number // 10
    print(result, end=" ")

print() 

if reverse == original:
    print("It is a palindrome")
else:
    print("Not a palindrome")

'''

#17

year =int(input("Enter the year"))

if year %4==0:
    print("leap year")
else:
    print("Not a leap year")



