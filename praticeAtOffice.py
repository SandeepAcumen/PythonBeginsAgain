# def add(name,age):
#     print(f"I am {name} and i am {age} years old")

# add("sandeep",22)

'''
def calculator(a,b):
    add = a+b
    sub = a-b
    return add,sub

result =calculator(45,10)
print(result)
'''
'''
def show_employee(name,salary=9000):
    print(f"Name: {name}, salary: {salary}")

show_employee("Sandeep",4568)
show_employee("shfedsf")

'''
'''
def addition(num):
    if num:
        return num +addition(num-1)
    else:
        return 0
    
res = addition(15)
print(res)
'''
'''
print(list(range(3,31,2)))

'''
'''

x = [4, 6, 8, 24, 12, 2]

print(min(x))

'''

'''
global_var =10

def change_global():
    global global_var
    global_var =40
    print(" changed gloabal",global_var)

change_global()
print(global_var)

'''
'''

x = [4, 6, 8, 24, 12, 2]
x.sort()
print(x)
'''

'''
x = [4, 6, 8, 24, 12, 2]
x.sort(reverse=True)
print(x)

'''
'''
class Python:

    def expectionHanding():
        print("Before Execption Handong")

        try:
            a=10
            b=0
            c=a/b
        except:
            print("error in the code")

Python.expectionHanding()
'''

'''
import decimal
i =10
print(decimal.Decimal(i))
print(type(decimal.Decimal(i)))
'''

'''
import decimal

string ='123456789'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

'''

#data type of python :
# string 
# int 
# float 
# map 
# tuple 
# boolean
# set
# dict
# range

'''
string="Hello i am sandeep"
print(string[::-1])

'''
#
'''

vowel = ['a', 'e', 'i', 'o', 'u']
string= 'Acumen is a Software company'
cunt=0
for i in string:
    if i in vowel:
        cunt =cunt+1
print(cunt)

'''
#
'''
vowel = ['a', 'e', 'i', 'o', 'u']
string= 'Acumen is a Software company'
count =0
for i in string:
    if i not in vowel:
        count +=1
  
print(count)

'''
#
'''
charater ='p,P'
string= 'Python is pap'
count =0
for i in string:
    if i in charater:
        count +=1
print("The number of occurance of p is ",count)

'''
#
'''
numberList = [15, 85, 35, 89, 125]
print(max(numberList))

'''
#
'''
numberList = [15, 85, 35, 89, 125]
print(min(numberList))

'''
#
'''
numberList = [15, 85, 35, 89, 125]

mid = int(len(numberList) /2)

print(numberList[mid])

'''
#
'''
list1 = ['S','W','R','G','P']

string = ''.join(list1)
print(string)
print(type(string))

'''
#
'''
numberList = [15, 85, 35, 89, 125]
max_no =numberList[0]

for i in numberList:
    if max_no < i:
        max_no = i

print(max_no)

'''
#

'''
import numpy as np
lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 

result = np.add(lst1,lst2)
print(result)

'''

#
'''
str1 ="asa".lower()
str2 ="asa".lower()

if str1 ==str2[::-1]:
    print("True")
else:
    print("False")

'''
#
'''
string = "P r ogramm in g "
print(string.count(' '))

'''

#

















































