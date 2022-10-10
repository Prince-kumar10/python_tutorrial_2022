# public  private  in python

# public
# protected
# private



class Employee:
    ver = 10
    no_of_leaves2 = 10
    _protected = 23
    __private = 98

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


Prince = Employee("Prince",4550,"instructor")


# print(Employee._protected)
# print(Employee._Employee__private)