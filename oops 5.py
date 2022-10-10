# @classmethod in class python and print str

class Employee:
    no_of_leaves2 = 10
    def __init__(self,aname,asalary,arole,):
        self.name = aname
        self.salary = asalary
        self.role = arole


    # def print_details(self):
    #    return f" This group leader is {self.name} and the group member is {self.salary}" \
    #          f" and group name is {self.role}"
    #
    # @classmethod
    # def change_leaves(cls, new_leaves):
    #      cls.no_of_leaves2 = new_leaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls (params[0], params[1], params[2])
         return cls(*string.split("-"))


Prince = Employee("Prince",4550,"instructor")
Balraj = Employee("Balraj",500,"student")
Rohan = Employee.from_dash("Prince-4500-instructor")

# Prince.change_leaves(12)

print(Rohan.name)