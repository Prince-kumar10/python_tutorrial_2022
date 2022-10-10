# classmethod in python decorator


class Employee:
    no_of_leaves2 = 10
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role


    def print_details(self):
       return f" This group leader is {self.name} and the group member is {self.salary}" \
             f" and group name is {self.role}"
    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves2=new_leaves


Prince = Employee("Prince",4550,"instructor")
# Balraj = Employee()

Prince.change_leaves(12)


# Prince.name = "Prince"
# Prince.salary = 4550
# Prince.role = "instructor"

#
# Balraj.name = "Balraj"
# Balraj.salary = 3500
# Balraj.role = "Student"
# Balraj.no_of_leaves = 12

print(Prince.print_details())
# print(Prince.no_of_leaves2)
print(Employee.no_of_leaves2)
print(Prince.name)
print(Prince.salary)
print(Prince.role)

