# single inheritance in python

class Employee:
    no_of_leaves2 = 10
    def __init__(self,aname,asalary,arole,):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def print_details(self):
       return f" This group leader is {self.name} and the group member is {self.salary}" \
             f" and group name is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves2 = new_leaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls (params[0], params[1], params[2])
         return cls(*string.split("-"))

    @staticmethod
    def print_static(string):
        print (f"Prince is very {string}")

class programmer(Employee):
    no_of_holiday = 45
    def __init__(self,name ,salary,role,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = languages



    def programmer_details(self):
        return f"The programmer is name {self.name} salary is" \
               f" {self.salary} and role {self.role} the languages are {self.language}"


Prince = Employee("Prince",4550,"instructor")
Balraj = Employee("Balraj",500,"student")
Rohan = Employee.from_dash("Prince-4500-instructor")

shubham = programmer("shubham",7900,"Instructor",["Python cpp Php"])
karan = programmer("karan",67000,"student",["Php html css java"])

# print(karan.programmer_details())
print(programmer.no_of_holiday)
print(Employee.no_of_leaves2)