class Employee:
    comapany ="HP"

    def __init__(self,name ,salary):
        self.name= name
        self.salary =salary
    
    #inStance Method
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a,b):
        return a +b
    
    @classmethod
    def print_company(cls):
        print(cls.comapany)

    @classmethod
    def change_copanyname(cls,new_comapany):
        cls.company =new_comapany

e1 = Employee("Sandeep",123)
e2 = Employee("Acumen",265898)

print(Employee.comapany)

e1.print_info()
e2.print_info()

print(f"The sum of two is",e2.sum(12003,12453))
print(e1.sum(12003,12453))

e1.print_company()
e1.change_copanyname("Velocity")
e1.print_company()







#print((e1.name,e1.salary))