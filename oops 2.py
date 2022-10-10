class Employee:
    no_of_leaves2 = 10
    pass

Prince = Employee()
Balraj = Employee()



Prince.name = "Prince"
Prince.salary = 4550
Prince.role = "instructor"
print(Prince.__dict__)

Balraj.name = "Balraj"
Balraj.salary = 3500
Balraj.role = "Student"
Balraj.no_of_leaves = 80
print(Balraj.__dict__)

Employee.no_of_leaves2=12
print(Employee.__dict__)

# print(Prince.no_of_leaves2)

# Eployee.no_of_leaves = 100
# print(Eployee.no_of_leaves)


