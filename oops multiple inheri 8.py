# multiple inheritance in python

class Employee:
    ver = 10
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

class Player:
    ver = 14
    def __init__(self,name,circket):
        self.name = name
        self.game = circket

    def player_details(self):
        return f"The player information is name {self.name}" \
               f" and favorite game is  {self.game }"

class cool_programmer(Player,Employee):
    # ver = 23
    no_of_language = "c++"

    def setlanguage(self):
        print(self.no_of_language)



Prince = Employee("Prince",4550,"instructor")
Balraj = Employee("Balraj",500,"student")
Rohan = Employee.from_dash("Prince-4500-instructor")

Kaushal = Player("Kaushal","circket")
Vishal = cool_programmer("vishal","hockey")


# Vishal.setlanguage()
# cool = Kaushal.player_details()
# print(cool)
print(Vishal.ver)