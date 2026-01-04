#1 WAP to fing comman letters in given String
'''
string1 = "NAINAE"
string2 = "REENE"

s1 =set(string1)
s2 = set(string2)

comman = s1 & s2
print(comman)
'''
#to print total number of occurances
'''
from collections import Counter
string1 = "NAINAE"
string2 = "REENE"

s1 = Counter(string1)
s2 =Counter(string2)

total = s1 & s2
print(total)

'''
#2 to count the frequency of words appearing in a string

'''
import re
from collections import Counter
string1 = "Sheena loves eating apple and mango.Her sister also loves eating apple and mango"

clean_string = re.sub(r'[^\w\s]','',string1)

words = clean_string.lower().split()

word_count = Counter(words)

print(word_count)

'''
'''
#3 Convertion of two list into dictonanry 

list1 = ["naina","kimi","Sheema"]
list2 = [12345,2356,9652]

new_dict = dict(zip(list1,list2))
print(new_dict)

dict.items("naina" ,12345)
'''

#4 find missing numbers in array
        
'''
arr =[1,2,6,8,11]
missing =[]

for i in range(1,12):
    if i not in arr:
        missing.append(i)

print(missing)

'''

#5 bubble sort
'''
list1 =[5, 3, 8, 4, 2]

n = len(list1)

for i in range(n):
    for j in range(n-1):
        if list1[j] >list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list1)
'''
#square the numbers in the list

'''
list1 = [1,2,3,4,5]
square =[]

for i in list1:
    j= i*i
    square.append(j)

print(square)
    
'''
































