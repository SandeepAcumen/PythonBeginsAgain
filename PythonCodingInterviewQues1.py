#https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md 
# Beginner Level

#1. What is Python??
#2. How is Python Interpreted?
#3. What are Pythons key features??
#4. What is PEP 8?
#5. How do you manage memory in Python?
#6. What are Pythons data type?
#7. What is the difference between Tuple and List?

#8.How do you handle exeptions in Python
'''
class Python:
    def handel_exp():
        print("Before Expection")
        try:
            a =20
            b=10
            c=a/b
            print(c)

        except:
            print("Error occured")

Python.handel_exp()

'''

#9. Converting an Interger into Decimal
'''
import decimal
class Python:
    def Int_Dec():
        number = 10
        print(decimal.Decimal(number))
        print(type(decimal.Decimal(number)))

Python.Int_Dec()
   '''     


#10. Converting a String of Integers into Decimals
'''
import decimal
class Python:
    def string_int():
        string="123456"
        print(decimal.Decimal(string))
        print(type(decimal.Decimal(string)))

Python.string_int()
'''

#11. Reversing a String using an Extended Slicing Technique
'''
class Python:
    def slicing():
        string='Hello'
        print(string[::-1])

Python.slicing()
'''

#12. Counting Vowels in a Given Word
'''
class Python:
    def Count_vowels():
        vowel = ['a', 'e', 'i', 'o', 'u']
        word = "programming"
        count =0
        for i in vowel:
            if i in word:
                count +=1
        print("The number of vowels are",count)

Python.Count_vowels()
'''

#13. Counting Consonants in a Given Word
'''
class Python:
    def counting_consonants():
        vowel = ['a', 'e', 'i', 'o', 'u']
        word = "programming"
        count =0
        for i in vowel:
            if i in word:
                count += 1

        print(count)

Python.counting_consonants()
        
'''

#14. Counting the Number of Occurrences of a Character in a String
'''
class Python:
    def count_char():
        string ="Python is a Programming Language"
        count =0
        charater =['p','P']
        for i in string:
            if i in charater:
                count +=1
        print(count)

Python.count_char()

'''
#15. Writing Fibonacci Series

#16. Finding the Maximum Number in a List
'''
class Python:
    def max_no():
        list1 =[122,3,6,9,6,5,8,3]
        max_no = list1[0]
        for i in list1:
            if max_no < i:
                max_no =i

        print(max_no)

Python.max_no()

'''

#17. Finding the Minimum Number in a List
'''
class Python:
    def min_no():
        list1 =[122,3,6,9,6,5,8,3]
        min_no = list1[0]
        for i in list1:
            if min_no > i:
                min_no =i

        print(min_no)

Python.min_no()

'''

#18. Finding the Middle Element in a List
'''
class Python:
    def middle_no():
        list1 =[122,3,6,9,60,5,8]
        mid= int(len(list1) / 2)
        print(list1[mid])

Python.middle_no()
        
'''

#19. Converting a List into a String
'''
class Python:
    def list_string():
        list1 =[122,3,6,9,60,5,8]
        string=''.join(map(str,list1))
        print(string)

Python.list_string()

'''
#20. Adding Two List Elements Together
'''
import numpy as np
class Python:
    def addlist():
        list1 = [1,2,3,5]
        list2 = [4,6,9,8]
        result = np.add(list1,list2)
        print(result)

Python.addlist()

'''
#21.Comparing Two Strings for Anagrams
'''
class Python:
    def anagram():
        string1 = 'Race'
        string2 = 'Care'

        string1 = list(string1.upper())
        string2 = list(string2.upper())
        string1.sort()
        string2.sort()

        if string1 == string2:
            print("True")
        else:
            print("False")

Python.anagram()

'''

#22. Checking for Palindrome Using Extended Slicing Technique
'''
class Python:
    def palindrom():
        str1 ='Malayalam'.lower()
        str2 = 'malayalam'.lower()
        if str1 == str2[::-1]:
            print("Given string is the palindrome")
        else:
            print("Not a Palindrome")

Python.palindrom()

'''
#23.Counting the White Spaces in a String
'''
class Python:
    def white_space():
        str1 ="Hello Wo rd s"
        result =str1.count(" ")
        print(result)

Python.white_space()
'''

#24. Counting Digits, Letters, and Spaces in a String
'''
class Python:
    def total_count():
        str1 ="Sandeep* hdsfk6455kjgd fh   784hg98 $^$$*^"
        total_digit = 0
        total_letter = 0
        total_spaces = 0
        for i in str1:
            if i.isdigit():
                total_digit +=1
                
            elif i.isalpha():
                total_letter +=1
                
            elif i.isspace():
                total_spaces +=1
                

        print("Total digits present are",total_digit)
        print("Total letters present are",total_letter)
        print("Total spaces present are",total_spaces)
            

Python.total_count()
'''
#25. Counting Special Characters in a String
'''
import re
spChar = "!@#$%^&*()"

count = re.sub('[\w]+', '', spChar)
print(len(count))
'''

#26. Removing All Whitespace in a String ***********
'''
import re
class Python:
    def remove_spaces():
        string="S and e e p "
        spaces = re.compile(r'\s+')
        result = re.sub(spaces,'',string)
        print(result)

Python.remove_spaces()
'''
#or
'''
class Python:
    def remove_spaces():
        string="S and e e p "
        removed= string.replace(" ","")
        print(removed)

Python.remove_spaces()

'''
#27.  Building a Pyramid in Python *********

#28. Randomizing the Items of a List in Python
'''
from random import shuffle
list1 = ['Python','is','Easy']
shuffle(list1)
print(list1)

'''

#29. Find the Largest Element in a List
'''
class Python:
    def large_list():
        list1 = [12,23,56,9,9,654,56]
        print(max(list1))

Python.large_list()

'''
#30. Remove Duplicates from a List
'''
class Python:
    def remove_duplicate(list1):
        return list(set(list1))
    
print(Python.remove_duplicate([12,36,2,5,6,9,2]))

'''
#31. Factorial of a Number ***********
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage:
print(factorial(5))

'''
#32. Merge Two Sorted Lists
'''
class Python:
    def merge_sort(list1,list2):
        return sorted(list1+list2)
        

print(Python.merge_sort([1,2,3],[4,5,6]))

'''
#33. Find the First Non-Repeating Character
'''
def first_non_repeating_character(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None

# Example usage:
print(first_non_repeating_character("swiss"))

'''
###################  Advanced Level ############

#34. What are Python metaclasses?
   # Classes is a instance of class

#35. Explain the difference between is and ==
   # is: Checks if two references point to the same object.
   # ==:  Checks if the values of two objects are equal.

#36. How does Python's memory management work?
   #Python uses reference counting and garbage collection. 
   # Objects with a reference count of zero are automatically 
   # cleaned up by the garbage collector.

#37. What is the purpose of Python's with statement?

#38. What are Python's @staticmethod and @classmethod?
   #@staticmethod: Defines a method that does not operate 
   # on an instance or class; no access to self or cls.
   #@classmethod: Defines a method that operates on the 
   # class itself; it receives the class as an implicit 
   # first argument (cls).

#39.  How do you implement a singleton pattern in Python?
   #A singleton pattern ensures that only one instance of a 
   # class is created throughout the entire program.
   #No matter how many times you create an object — you 
   # always get the same instance.

#40. Explain Pythons garbage collection mechanism?
   #Python uses a garbage collection mechanism based on 
   # reference counting and a cyclic garbage collector to 
   # detect and collect cycles

#41. What are Pythons's Magic methods?
   #Magic methods are special methods with double underscores
   #at the beginning and end.They enable the customization of 
   #behavior for standard operation.
   #1. __init__ : Constrctor
   #2. __str__ : String representation
   #3. Addition operator

#42. How do you handle multi-threading in Python?
   #code example
'''
import threading
import time

def print_number():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letter():
    for c in "ABCDEFGH":
        print(c)
        time.sleep(1)

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)
t1.start()
t2.start()

'''

#43. What are Python's coroutine functions?
'''
import asyncio

async def say_hello():
    await asyncio.sleep(3)
    print("Hello")

asyncio.run(say_hello())
 
'''

#44. Explain the Pythons's global Interpreter Lock(GIL)

#45. What are metaclasses in Python???
  
'''
A metaclass in Python is a class of a class that defines 
how a class behaves.Classes themselves are instances of metaclasses.
You can customize class creation by defining a metaclass, such as modifying 
class properties, adding methods, or implementing design patterns.

'''

#46. Can you explain the difference between deepcopy and copy in Python?

'''
copy.copy() creates a shallow copy of an object. It copies the object's 
structure but not the elements themselves, meaning it only copies references
 for mutable objects.

copy.deepcopy() creates a deep copy of the object, including recursively 
copying all objects contained within the original object. Changes made to 
the deep-copied object do not affect the original object.


'''

#47. Describe Python’s __slots__ and its benefits.

#48. What is the difference between is and == in Python?

#49. Find the Longest Consecutive Sequence in an Unsorted List?

#=========== Most Frequently Asked Python Questions by Big Tech Companies======

#1. Longest Substring Without Repeating Characters
'''
class Python:
    def longest_substring(s):
        start =0
        max_length = 0
        seen = {}

        for i,char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1

            seen[char] = i
            max_length = max(max_length, i -start +1)

        return max_length
    

print(Python.longest_substring("abcabcbb"))
print(Python.longest_substring("pwwkew"))

'''












































