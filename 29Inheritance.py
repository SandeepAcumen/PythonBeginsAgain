'''
class Animal:

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Generic animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof Woof")

d=Dog("Bruno")
d.speak()
'''
#Super
'''
class Animal:

    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Generic animal sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof Woof")

d=Dog("Bruno")
d.speak()

'''

#single inheritance
'''
class laptop:
    def brand(self):
        print("this is lenovo laptop")

class gaminglaptop(laptop):
    def gbrand(self):
        print("This laptop has a high-end graphics card.")


g1 =gaminglaptop()
g1.brand()
g1.gbrand()
'''

#multilevel inheritrance
'''
class laptop:
    def brand(self):
        print("this is MAcbook")

class gaming(laptop):
    def gamingbrand(self):
        print("for gaming i use legion")

class editing(gaming):
    def editing(self):
        print("for editing i use MacBook")

brand = editing()
brand.brand()
brand.editing()
      '''  

# multiple inheritance












