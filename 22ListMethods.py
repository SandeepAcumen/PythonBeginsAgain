'''
marks =[21,26,45,64,75,26]

marks.append(40)
print(marks)

marks.pop()
print(marks)


n=marks.pop(2)
print("The number poped is ", n)


marks.reverse()
print(marks)

marks.sort()
print(marks)

mix =[4654,5514.36,True,"hgdshf"]
mix.reverse()
print(mix)


#Table of 5 in list

a=5
table = []
for i in range(1,11):
    table.append(5*i)

print(table)
 '''
 #or

table = [5*i for i in range(1,11)]
print(table)

six =[6*i for i in range(1,20)]
print(six)

