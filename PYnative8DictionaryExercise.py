#1
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

my_dict['profession'] ='Doctor'

print(my_dict)

my_dict['age']=40

'''

#2
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

del my_dict['profession']

print(my_dict)
for key,value in my_dict.items():
    print(f"{key} : {value}")

'''

#3
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d = dict(zip(keys,values))
print(d)

'''

#4
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

my_dict.clear()
print(my_dict)

'''

#5
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1,**dict2}
print(dict3)
'''
############
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 =dict1.copy()
dict3.update(dict2)
print(dict3)
'''

#6
'''
string ='Jessa'
freq ={}

for c in string:
    freq[c] =freq.get(c,0+1)
print(f"{freq}")

'''
#7
'''
data = {'person': {'name': 'Alice', 'age': 30}}

ageee = data['person']['age']
print(ageee)
'''

#8
'''
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

c =sampleDict["class"]["student"]["marks"]["history"]
print(c)
'''

#9
'''
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

nested_student_dict["class"]["student"]["name"]="Jessa"
print(nested_student_dict)
'''

#10
'''
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees,defaults)
print(result)

'''

#11

'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys =["name"]["salary"]
newDict = {k : sample_dict[k] for k in keys}
print(newDict)

'''
#12
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name" ,"salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)

'''
#13
'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("200 is present in dict")

if "a" in sample_dict.keys():
    print("c is present")
else:
    print("Not Presnt")

'''

#14
'''
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict["location"] =sample_dict.pop("city")
print(sample_dict)
'''

#15
'''
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict.values()))

'''

#16
'''
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3'] ['salary']=8500
print(sample_dict)

'''

#17

'''
def invert_dictionary(input_dict):
  inverted_dict = {}
  # iterates through each key-value pair in the input_dict
  for key, value in input_dict.items():
    inverted_dict[value] = key
  return inverted_dict

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

print(f"Original dictionary 1: {original_dict1}")
print(f"Inverted dictionary 1: {invert_dictionary(original_dict1)}")
'''
  
#18
'''
from collections import OrderedDict
my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

s =sorted(my_dict.values())
print(s)
'''

#19
'''
from collections import OrderedDict

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print(f"Original dictionary: {my_dict}")

# Method 1: Create an OrderedDict sorted by values
print("\nSorted by values (as OrderedDict):")
sorted_by_value_ordered_dict = OrderedDict(my_dict)
print(sorted_by_value_ordered_dict)

# Method 2: Convert to a list of (key, value) tuples, sorted by value
print("\nSorted by values (as list of tuples):")
print(my_dict)

'''

#20
'''
def all_values_unique(d):
    # if values converted to a set keep the same length, all are unique
    return len(d.values()) == len(set(d.values()))

# Examples:
dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {}                                   # Empty dictionary (no values)

print(all_values_unique(dict1))  # True
print(all_values_unique(dict2))  # False
print(all_values_unique(dict3))  # True

'''



























