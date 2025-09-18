#1
'''
my_list = [10, 20, 30, 40, 50]
print(my_list[2])
length =len(my_list)
print(length)

if length==0:
    print("IS Empty")
else:
    print("Is not emplty")

'''

#2
'''
my_list = [10, 20, 30, 40, 50]
my_list[1]=200
print(my_list)

my_list.append(600)
print(my_list)

my_list.insert(2, 300)
print(my_list)

my_list.remove(600)
print(my_list)

del my_list[0]

'''

#3
'''
my_list = [10, 20, 30, 40, 50]
l = len(my_list)
s = sum(my_list)
print(s/l)

'''

#4
'''
list1 = [100, 200, 300, 400, 500]

print(list1[::-1])
'''

#5
'''
numbers = [1, 2, 3, 4, 5, 6, 7]
square_no =[]
for n in numbers:
    square = n**2
    square_no.append(square)
print(square_no)

'''
#7
'''

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis','Football']

count =0
for i in sports:
    if i =='Football':
        count +=1
print(count)
'''

#8
'''
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)
'''

'''
numbers = [5, 2, 8, 1, 9]
sort =sorted(numbers)
print(sort)
'''

#9

'''
original_list =[10,20,30]

copied_list =original_list

copied_list.append(40)
copied_list.insert(2,1000)
print(copied_list)
'''

#10
'''
list_a = [1,2,3]
list_b = [3,4]

list_c= list_a+list_b
#print(set(list_c)) // repieted once will be priented
print(list_c)
'''

#11
'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = list(filter(None,list1))
print(result)
'''

#12
'''
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

print(set(list_with_duplicates))

'''

#13
'''
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)

print(list1)

''' 


#14
'''
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6,456.256]

only_numbers = [x for x in my_list if isinstance(x,int)]

print(only_numbers)

'''
#15
'''
nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

element=nested_list[1][1]
print(element)

'''

#16
'''

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]

flat_list = [item for sublist in list_of_lists for item in sublist]

print(flat_list)

'''

#17
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i+j for i,j in zip(list1,list2)]
print(list3)
'''

#18
'''
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [i+j for i in list1 for j in list2]

print(list3)
'''

#19
'''
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i,j in zip(list1,list2[::-1]):
    print(i,j)

'''

#21
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

'''

#22









