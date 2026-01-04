#1A
'''
str1 = "James"
print("Original string is :" ,str1)
res = str1[0]
l = len(str1)

m= int(l/2)
#print the midindex
res = res + str1[m]

res =res + str1[l-1]

print("The new string is : ",res)
'''

#1B
'''
def get_middle_three_char(str1):
    print("Print the original string: ",str1)

    middle = int(len(str1)/2)
    print(middle)
    res = str1[middle -1 : middle + 2]
    print("Middle three chars are :",res)

get_middle_three_char("sandeep")
get_middle_three_char("JaSonAy")

'''
#2

'''
def append_middle(s1,s2):
    middle = int(len(s1) /2)

    x = s1[:middle:]

    x = x+s2
    x= x+s1[middle:]

    print("After append new string in midlle:  ",x)

append_middle("Ault","kelly")
'''
#3
'''
def mix_string(s1,s2):
    first_char = s1[0]+ s2[0]

    middle_char = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]

    last_char =s1[len(s1) -1] + s2[len(s2)-1]

    res =first_char+middle_char+last_char
    print(res)

mix_string("America","Japan")
'''

#4
'''
str1= "PUghsgdGG"

print("Original strinf is ",str1)

lower =[]
upper =[]

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str = ''.join(lower+upper)
print("result", sorted_str)

'''

#5
'''
def find_char_no_sybbole(sample_str):
    char_count =0
    digit_count =0
    symbole_count =0
    for char in sample_str:
        if char.isalpha():
            char_count +=1
        
        elif char.isdigit():
            digit_count +=1
        
        else:
            symbole_count += 1

    print("char+count is:",char_count,"Digit count:",digit_count,"Sysmbole count:",symbole_count)


sample_str = "P@yn2at&#i5ve"
find_char_no_sybbole(sample_str)
'''

#6
'''
s1 = "Abc"
s2 ="XyzdsgD"

s1_length = len(s1)
s2_length = len(s2)

length = s1_length if s1_length >s2_length else s2_length
result =""

s2=s2[::-1]

for i in range(length):
    if i <s1_length:
        result = result + s1[i]
    if i < s2_length:
        result=result +s2[i]

print(result)

'''

#7
'''
def string_in_list(s1,s2):
    flag =True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag

s =string_in_list("sa","sandeep")
print(s)

'''

#8
'''
str1 = "Welcome to USA. usa awesome,usa isn't it?"
count =str1.lower().count("usa")
print(count)
'''

#9
'''
str1 = "PYnat54ive29@#8496"
count_digit =0
total=0
for char in str1:
    if char.isdigit():
        total += int(char)
        count_digit +=1

avg =total/count_digit
print(avg)

'''

#10
'''
str1 ="Apple"
char_dirt =dict()

for char in str1:
    count =str1.count(char)
    char_dirt[char] = count

print(char_dirt)

'''
#11
'''
str1 = "PYnative"

str1=str1[::-1]
print(str1)
'''
'''
str1 = "PYnative"
str1 = ''.join(reversed(str1))
print(str1)
str1 =''.join(reversed(str1))
'''

#12
'''
str1 = "Emma is a data scientist who knows Python. Emma works at google."

s= str1.rfind("knows")
print(s)
'''
#13
'''
str1 = "Emma-is-a-data-scientist"
sub_string=str1.split("-")
for i in sub_string:
    print(i)
'''

#14

'''
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list=[]
for i in str_list:
    if i:
        res_list.append(i)

print(res_list)

'''
#15
'''
import string
str1 = "/*Jon is @developer & musician"

new_str =str1.translate(str.maketrans('','', string.punctuation))
print(new_str)
'''

#16
'''
str1 = 'I am 25 years and 10 months old'
result ="".join([item for item in str1 if item.isdigit()])
print(result)
'''

#17

#18

