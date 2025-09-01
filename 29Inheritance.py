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

