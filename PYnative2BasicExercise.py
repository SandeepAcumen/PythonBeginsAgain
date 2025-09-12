#1
'''
number1 = int(input("Enter First number: "))
number2 = int(input("Enter Second number: "))

number3 =print("the Sum is :",number1 * number2)
'''

#2
'''
str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'

print(str1,str2,str3,str4,sep="**")

'''
#3
'''
num =80
print('%o'% num)
'''

#4
'''
num = 445.695841
print(f"{num:.3f}")
print(f"{num:.1f}")
'''

#5
'''
l1=float(input("enter 1: "))
l2=float(input("enter 2: "))
l3=float(input("enter 3: "))
l4=float(input("enter 4: "))
l5=float(input("enter 5: "))

l6=[l1,l2,l3,l4,l5]
print(l6)
'''
#6

#7
'''
str1,str2,str3 = input("Enter three names: ").split()
print("Name 1: ",str1)
print("Name 2: ",str2)
print("Name 3: ",str3)
'''

#8
'''
totalMoney = 1000
quantity = 3
price = 450

print(f"I have {totalMoney} so i can buy {quantity} football for {price}.00 dollars")
'''

#9
'''
import os
size =os.stat("harry.txt").st_size
if size == 0:
    print("file is empty")
'''

#10
'''
with open("harry.txt" ,"r") as fp:
    lines= fp.readlines()
    print(lines,end =" ")
'''
#11
'''
numerator =int(input("enter numerator: "))
denominator =int(input("Enter denominator: "))
percenage = (numerator / denominator) *100

print(f"{percenage:.2f} %")
'''
#12
'''
while True:
    print("---Menu---")
    print("1.Say hello")
    print("2.Calculate Square")
    print("3.Exit")

    choice = input("Enter your choice(1-3) :")
    if choice =="1":
        print("Hello there welocme")
    
    elif choice =="2":
        num = float(input("Enter the number"))
        print("the suare of number is", num**2)

    elif choice =="3":
        print("exiting ==byee")
        break
    
    else:
        print("invalid choise")

'''

#13
'''
word = input("Enter a word: ")
number= input("Enter a number: ")
print(f"{word:>20}{number}")
'''

#14
'''
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score':<5}")
print("-"* 18)
for names,score in zip(names,scores):
    print(f"{names:<10} {score:<5}")

'''
#15
'''
number_str = input("Enter the number : ")
padded_no = number_str.zfill(5)
print(padded_no)
'''


