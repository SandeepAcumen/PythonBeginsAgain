#1
'''
fruits ={"apple","banana","mango","orange"}

fruits.add("grape")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("mango")
print(fruits)

'''

#2
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.union(set2)
print(set3)
'''

#3
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
print(set3)
'''

#4
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.difference(set2)
print(set3)
'''

#5
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 =set1.symmetric_difference(set2)
print(set3)
'''
#6
'''
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]


sample_set.update(sample_list)
print(sample_set)

'''

#7
'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)
'''

#8
'''
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10,20,30})
print(set1)

'''

#9
'''
subset_set = {10, 20}
main_set = {10, 20, 30, 40}

is_subset =subset_set.issubset(main_set)
print(is_subset)

'''

#10
'''

set1 = {10, 20}
set2 = {10, 20, 30, 40}

is_superset = set2.issuperset(set1)
print(is_superset)
'''

#11
'''
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set3 = set1.intersection(set2)
print("Two sets have items in commom",set3)

'''

#12
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

'''

#13
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)

'''

#14
'''
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

set_list1= set(list1)
set_list2 = set(list2)

s3 =set_list1.intersection(set_list2)
print(s3)

'''
#15
'''
my_list = [10, 20, 30]

f = frozenset(my_list)
print({f})

'''

#16
'''
sentence = "dog is a simple animal dogs is selfless animal"
words = sentence.lower().split()
unique_words = set(words)
unique_word_count = len(unique_words)
print(f"Number of unique words: {unique_word_count}")
'''
######
'''
sentence = "dog is a simple animal dogs is selfless animal"

single_words = sentence.lower().split()

words_set =set(single_words)

length_words = len(words_set)
print(length_words)

'''
#17







































