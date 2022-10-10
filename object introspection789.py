class Employee():
    def __init__(self,fname ,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname} {self.lname} @princethakur.com"

    def explain(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        # if self.fname == None or self.lname == None:
            return  f"{self.fname} {self.lname} @princethakur.com"

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skillf","f")

# print(skillf.explain())
# print(skillf.email)

# print(type(skillf))
print(type("this is a string "))

print(id("this is me "))
print(id("you are very hardsome"))

o = "this is me "
# print(dir(o))
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))