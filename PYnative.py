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
a= [32,5,56,10,360,984,74,48990]
for n in a:
    if n % 5 ==0:
        print(n)

'''

#7
'''
string ="Emma is good developer,Emma is a writter"

num=string.count("Emma")
print("Emma is replied for ", num)

'''

#8
'''
for num in range(6):
    for i in range(num):
        print(num,end="")
    print("")
'''

#9
#print palindrom 
'''
word = input("Enter the word : ")
if word == word[::-1]:
    print(f"{word} is a Palindrom")
else:
    print(f"{word} is not a Plaindrom")
'''
#for number
'''
num = int(input("Enter the number :"))
if str(num) == str(num)[::-1]:
    print(f"{num} is a palindrom")
else:
    print(f"{num} is not a Palindrom")
'''

#10
'''
list1=[10,20,25,30,35]
list2=[40,45,60,75,90]

def odd():
    for n in list1:
        if n % 2==1:
            print(n)

def even():
    for n in list2:
        if n % 2==0:
            print(n)
'''

'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def odd():
    result = []
    for n in list1:
        if n % 2 == 1:
            result.append(n)
    return result

def even():
    result = []
    for n in list2:
        if n % 2 == 0:
            result.append(n)
    return result

# Combine results from both functions
final_list = odd() + even()
print(final_list)

'''
#11
'''
number = 3245
while number >0:
    digit = number %10
    number =number //10
    print(digit,end = "")

'''

#12



 
    


    


