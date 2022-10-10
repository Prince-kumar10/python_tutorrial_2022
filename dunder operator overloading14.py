class Employee:
    no_of_leaves2 = 10
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role


    def print_details(self):
       return f" The name is {self.name} salary is  {self.salary}" \
             f" and role is {self.role}"
    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves2=new_leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}','{self.salary}','{self.role}')"
        # return f" The name is {self.name} salary is  {self.salary}" \
        #        f" and role is {self.role}"
         # return self.print_details()

    def __str__(self):
        return f" The name is {self.name} salary is  {self.salary}" \
               f" and role is {self.role}"




emp1 = Employee("Prince",78,"student")
emp2 = Employee("Balraj",2,"cleaner")

# print(emp1 / emp2)
# print(repr(emp1))
# print(emp1)
print((emp1))