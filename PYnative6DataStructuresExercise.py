#1
'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
result =[]

for i in l1:
    if i%2 ==1:
        result.append(i)

for i in l2:
    if i%2 ==0:
        result.append(i)

print(result)

'''
#2
'''
list1 = [54, 44, 27, 79, 91, 41]

removed =list1.pop(4)

list1.insert(2,removed)

list1.append(removed)

print(list1)
'''

#3
'''
sample_list =[11, 45, 8, 23, 14, 12, 78, 45, 89]

print("Original list" ,sample_list)

chunk_size = len(sample_list)//3

chunk1= sample_list[0:chunk_size]
chunk2 =sample_list[chunk_size:chunk_size*2]
chunk3 =sample_list[chunk_size*2:]

print(chunk1)
print(chunk1[::-1])
print(chunk2[::-1])
print(chunk3[::-1])

'''

#4
'''
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict =dict()
for i in sample_list:
    if i in count_dict:
        count_dict[i] +=1
    else:
        count_dict[i] =1

print(count_dict)
'''

#5
'''
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list,second_list)
result_set =set(result)
print(result_set)
'''

#6
'''
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection =first_set.intersection(second_set)
print(intersection)

for i in intersection:
    first_set.remove(i)

print(first_set)
'''
#7
'''
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
'''
#8
'''
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]

print(roll_number)
'''

#9
'''
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

speed_list = list()

for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)

print(speed_list)
'''

#10
'''
sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
print("Original list is :",sample_list)

sample_list= list(set(sample_list))
print(sample_list)

t =tuple(sample_list)
print("tuple", t)

print("Minimum number is ",min(t))
print("Maximum number is : ",max(t))

'''

