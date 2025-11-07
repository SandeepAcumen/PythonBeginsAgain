#Arrays
'''
1.Liner Data Structure
2.Contiguous memory location
3.Access elements randomly
4.Homogeneous elements only

'''

#Applications of Arrays
'''
1.Storing information -linear fasion
2.Suitable for application that require frequent searching

'''

#1-Dimensional Array
'''
1. 1D can be related to a row
2.Elements are stored one after another
3.Only one subscript ot index is used
'''

#2-Dimensional Array
'''
1. 2D can be related to a table or matrix
2. Elements are stored one after another i.e one 1D array inside other
3. Two subscripts or indices are used, one row and one column
4. Dimension depends upon the number of subscripts used

'''

#Array Implementation

#1.create 1D array and elements to it
'''
print("How many element to store inside the array: ",end="")
num = input()
arr=[]
print("\nEnter",num,"Element:",end ="")
num = int(num)
for i in range(num):
    element = input()
    arr.append(element)
print("\nThe array elements are")
for i in range(num):
    print(arr[i],end="")

'''

#2.create 2D elemenets
'''
row_no = int(input("Enter number of rows: "))
col_no = int(input("Enter number of columns: "))
total_arr = [[0 for col in range(col_no)] for row in range(row_no)]

for row in range(row_no):
    for col in range(col_no):
        total_arr[row][col] = row *col
print(total_arr)

'''

# Deleting the array
'''
arr= [10,20,30,40,50,60]
del arr[2]
print(arr)

arr1 = [10, 20, 40, 50, 60]
removed = arr1.pop(2)
print(arr1)
print("The removedarr is",removed)


arr2 = [10, 20, 50, 60]
arr2.remove(50)
print(arr2)

'''

#3. Insertion in the array
'''
arr = [10,20,30]
arr.append(40)
print(arr)

arr.insert(0,5)
print(arr)

arr.extend([50,60,70])
print(arr)

arr= arr + [80,90]
print(arr)

'''

#4.Search the arr
'''
arr = [10,20,30,40]
if 30 in arr:
    print("30 Present")
    print("The index of 30 is",arr.index(30))
else:
    print("30 is not present in Array")

'''

#5.Sort
'''
arr=[10,20,5,2,6,66]
arr.sort()
print(arr)

'''
















