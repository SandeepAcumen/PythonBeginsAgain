#1

'''
my_tuple = (1,2,3,4,5)
print(my_tuple)

third =my_tuple[3]
print("the fourth element in tuple is : ",third)

length = len(my_tuple)
print(length)
'''

#2
'''
original_tuple = ('a', 'b')
three_times = original_tuple*3
print(three_times)
'''

#3
'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sliced = numbers[3:7]
print(sliced)

'''

#4
'''
tuple1 = (10, 20, 30, 40, 50)

print(tuple1[::-1])

'''

#5
'''
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])
print(tuple1[0])
print(tuple1[2])
'''

#6
'''
tuple1 =(50,)
print(tuple1)
'''

#7
'''
tuple1 = (10, 20, 30, 40)
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]

print(a)
print(b)
print(c)
print(d)
'''

#8
'''
tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1 ,tuple2 =tuple2 ,tuple1
print(tuple1,tuple2)
'''

#9
'''
tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 =tuple(i for i in tuple1 if i==44 or i==55)
print(tuple2)

'''

#10
'''
my_list = [10, 20, 30]
convert = tuple(my_list)
print(convert)
'''

#11
'''
def convert_tuple(my_list):
    convert = tuple(my_list)
    return convert
    

list=[10,20,30,5,6,9,55]
result = convert_tuple(list)
print(result)
'''

#12
'''
t1 = (1, 2, 3)
t2 = (1, 2, 4)

if t1 > t2:
    print(" Yes,t1 is greater than t2 ")
elif t1 < t2:
    print("t1 lesser than t2")
else:
    print("t1 = t2")

'''

#13
'''
my_tuple = (1, 2, 2, 3, 4, 4, 5)

uniq = set(my_tuple)
s =tuple(uniq)
print(s)
'''

#14
'''
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

high_achievers = [student for student in students if student[1] >= 90]
print(high_achievers)
'''

#15
'''
t = (1, 2, 3, 4)
squared_tuple_map = tuple(map(lambda x: x**2, t))
print(f"Squared tuple (map function): {squared_tuple_map}")

'''

#16
'''
tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0]=222
print(tuple1)
'''

#17

#18
'''
tuple1 = (50, 10, 60, 70, 50,50,5)
print(tuple1.count(50))
'''

#19
'''
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))

'''



































