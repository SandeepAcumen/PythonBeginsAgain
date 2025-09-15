#1 using For
'''
for i in range(1,11):
    print(i)

i=1
while i<=10:
    print(i)
    i = i+1
'''

#2
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end =" ")
    print( )

for i in range(1,6):
    print(str(i) * i)
'''

#3
'''
sum=0
num= int(input("Enter number : "))

for i in range(1,num+1,1):
    sum =sum+i
print("Sum is :", sum)
    
'''

#4
'''
num=int((input("Enter the number : ")))
for i in range(1,11):
    j=num*i
    print(j)

'''

#5
'''
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i >500:
        break

    if i >150:
        continue
    if i %5 ==0:
        print(i)
'''

#6
'''
count =0
number =54654564

while number!=0:
    number =number // 10
    count =count+1

print(count)

'''
#7

'''
k=5
for i in range(0,6):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print()

'''
#8
'''
list1 = [10, 20, 30, 40, 50]

new_list = reversed(list1)
for i in new_list:
    print(i)

'''

#9
'''
for i in range(-10,0):
    print(i)
'''

#10
'''
for i in range(5):
    print(i)
print("Done!")

'''
#11

# for i in range(1,21):
#     if i>1:
#         for j in range(2,i):
#             if (i%j) ==0:
#                 break
#         else:
#             print(i,end=" ")
'''
start =20
end=50
for num in range(start,end+1):
    if start>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print(num)
'''

#12
'''
num1=0
num2=1
print("The Febonbacci series is : ")

for i in range(10):
    print(num1, end =" ")
    res =num1+num2
    num1 =num2
    num2=res

'''

#13
'''
factorial =1

for i in range(1,6):
    factorial=factorial*i
print(factorial)

'''

#14
'''
num= 123456
rev=0
while num != 0:
    digit = num %10
    rev =rev * 10 +digit
    num =num //10
print(rev)
'''
#else
'''
no=123456
rev=int(str(no)[::-1])
print(rev)

# if no ==rev:
#     print("is plaindrom")
# else:
#     print("not a palindrom")
'''

#15
'''
#for oddd index to print
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i)
    
#for even index to print
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[::2]:
    print(i)
'''

#16
'''
for i in range(1,6):
    print(f"Current Number is : {i}  and the cube is {i}",i**3)

'''

#17
'''
terms = 5
num = 2
sum_seq = 0
for i in range(0, terms):
    print(num, end="+")
    sum_seq += num
    num = num * 10 + 2
print("\nSum of above series is:", sum_seq)
'''

#18
'''
for i in range(0,6):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for i in range(6,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")

    print()

'''

#19
'''
for i in range(1,11):
    print(i,"multipliaction of is : ")
    for j in range(1,11):
        print(i*j,end =" ")

    print()
'''

#20


