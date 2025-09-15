# to find the squares of 1 to 10
'''
number = [1,2,3,4,5,6,7,8,9,20]

def square(x):
    return x * x

new = list(map(square,number))
print(new)
'''
#filter
'''
def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a =[1,3,5,43,4356,7657,23,2,2,3,5,67,7]

new =list(filter(is_greater_than_9,a))
print(new)

'''

#Reduce
from functools import reduce
a = [1,2,3,4,5,6,7]

def sum(a,b):
    return a+b

c = reduce(sum,a)
print(c)


