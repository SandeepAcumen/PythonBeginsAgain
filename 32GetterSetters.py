#no full codeee
'''
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
    @property
    def fist_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l= self.name.split(" ")
        new_name =f"{first} {l[1]}"
        self.name =new_name


e =Employee("Sandeep Kumar",125665)

print(e.first_name)
e.first_name ="John"
print(e.name)

#print(e.name,e.salary)
        
'''

class Employee:
    def __init__(self, firstname, salary):
        self._firstname = firstname     # note the underscore for a "private" variable
        self._salary = salary

    # Getter for firstname
    @property
    def firstname(self):
        return self._firstname

    # Setter for firstname
    @firstname.setter
    def firstname(self, new_name):
        # you can put validation logic here if needed
        if len(new_name) < 2:
            raise ValueError("Firstname must be at least 2 characters long")
        self._firstname = new_name


# Usage
e = Employee("Sandeep", 125665)

# fetch firstname using the getter
print("First name:", e.firstname)

# update firstname using the setter
e.firstname = "Kumar"
print("Updated first name:", e.firstname)
