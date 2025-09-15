a = (45,65,95,75,35,11)
for i in a:
    print(i +1)


print("the insdex of 1 is ", a[2])

# a[3] =66 well get error cause it does not allow changes

b=(5,)
print(b)

tu =(3,2,56)
a,b,c =tu
print(a)
print(b)
print(c)

t =(12,36,96,85,12,12,36)
print("The Number of times 12 is replied is",t.count(12))

#Why Tuples
#1Faster than List
#2safe for unintended Modification
#3 USed as dictionary keys(sience they are hashable)


