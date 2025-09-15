#1
'''
def about(name,age):
    print("The name is :",name)
    print("age is :",age)

about("sandeep",45)
'''

#2
'''
def func1(*args):     # *args lets you pass any number of arguments
    print("Printing values")
    for val in args:
        print(val)

func1(20, 40, 60)
print()          # just for a blank line between the two outputs
func1(80, 100)
'''

#3
'''
def calculation(a,b):
    sum=a+b
    sub=a-b
    print(sum,sub)

calculation(50,10)

'''

#4
'''
def showEmployee(name,salary=9000):
    print(f"Name: {name} salary: {salary}")

showEmployee("Ben",120000)
showEmployee("Jessa",10000)
showEmployee("sandeep")

'''
#5
'''
def other_fun(a,b):
    square = a**2

    def addition(a,b):
        return a+b
    
    add=addition(a,b)
    return add + 5

result =other_fun(5,10)
print(result)
'''

#6

'''
def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
    
res =addition(10)
print(res)

'''
#7
'''
def students(name,age):
    print(name,age)

students("sandeep",22)
new_student = students
new_student("ada",33)

'''

#8
#single line 
#print(list(range(4,30,2)))
'''
#single line print(list(range(4,30,2)))

def even():
    start =4
    end=31
    for i in range(start,end):
        if i%2==0:
            print(i)

even()

'''
#9
'''
x = [4, 6, 8, 24, 12, 2]
print(max(x))
print(min(x))

'''

#10
'''

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type} named {pet_name}.")

describe_pet('Dog','Harry')
describe_pet('hamster','Lucy')

describe_pet(animal_type="cat",pet_name='Whiskers')
describe_pet(animal_type="BOBcat",pet_name='tom')
'''

#11
'''
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
print_info(name="samdeep",age=22,school="vvs")
print_info(salry=45678,college="chaitra PU college")

'''
#12
'''
g_var =20
def modifed_global():
    global g_var
    g_var=30
    print("inside ",g_var)

modifed_global()
print("outside",g_var)

'''

#13

#14
'''
square =lambda x:x**2

number = 5
squared_number = square(number)
print(f"The square of{number} is {squared_number}")
'''

#15
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = list(filter(lambda x:x%2==0,numbers))
print(even_number)

'''
#16
'''
number =[1,2,3,4,5,6,7]
double_number = list(map(lambda x:x*2 ,number))
print(double_number)

'''
#17
'''
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
sorted_data = sorted(data, key=lambda item: item[1])
print(f"The sorted list of tuples based on the second element is: {sorted_data}")
'''

