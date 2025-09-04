#Dunder Method means double underscore " _ _"

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    #dunder Method
    def __str__(self):
        return f"the name {self.name} salary is {self.salary}"
    
    def __len__(self):
        return len(self.name)
        

a = Employee("Harry", 2345)

print(a.name , a.salary)

print(str(a))
print("The length of the name is",len(a))

