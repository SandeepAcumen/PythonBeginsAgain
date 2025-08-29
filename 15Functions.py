'''
a =4
b= 65
c=5
avg = (a+b+c)/3
print(avg)

a1 =44
b1= 655
c1=532
avg1 = (a1+b1+c1)/3
print(avg1)
'''
#without return type
def average(a,b,c):
    d=(a+b+c)/3
    print("The average is :" , d)
average(3,4,7)

def sum(x,y):
    z=x+y
    print("The Sum is :" ,z)
sum(654665,4654)


#with return type
def average(a,b,c):
    d=(a+b+c)/3
    return d
o1 = average(3,4,7)
print(o1)


def mul(q,w,e):
    r=q*w*e
    return r
m1=mul(12,34,56)
print(m1)
