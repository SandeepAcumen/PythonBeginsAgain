'''
class Employee:

    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name =name
        self.bond=bond
    
    def get_info(self):
        print(f"The name of the emp is {self.name}.Salary is {self.salary}")
    
e1 =Employee(3400,"candy",4)
e1.get_info()

'''

class book:

    def __init__(self,name):
        self.name = name

    def book_name(self):
        print(f"the name of the book is {self.name}")


b =book("Born to Run")
b.book_name()
