class Employee():
    def __init__(self,fname ,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname} {self.lname} @princethakur.com"

    def explain(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return  f"{self.fname} {self.lname} @princethakur.com"

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    @email.setter
    def email(self,string):
        print("setting now...")
        name = string.split("@")[0]
        self.lname = name.split(".")[0]
        self.fname = name.split(".")[1]



vishal_kumar = Employee("vishal","kumar")

vishal_kumar.fname = "raj"

# print(vishal_kumar.email)

vishal_kumar.email = "that.this @princethakur.com"

print(vishal_kumar.fname)

print(vishal_kumar.email)


