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





