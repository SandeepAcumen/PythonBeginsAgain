class Employee:
    company ="Asus"

    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company
    
    def get_info(self):
        print(f"The name of the emp is {self.name}.Salary is {self.salary}")


e1 = Employee(3400,"John",5,"Tesla")  
print(e1.company) 
print(e1.get_info())     