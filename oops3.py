# constructor in python oops

class whatsapp_Group:
    new_group = "Love coding group"

    def __init__(self ,name,group_member,group_name):
        self.name = name
        self.group = group_member
        self.group_name = group_name


    # def print_details(self):
    #     return f" This group leader is {self.name} and the group member is {self.group_member}" \
    #            f" and group name is {self.group_name}"


# Harry = whatsapp_Group("Prince",26,"high coding gruop")
Prince = whatsapp_Group("Prince",26,"high coding gruop")
# Harry.name = "Harry"
# Harry.group_member = 12
# Harry.group_name = "Best coding gruop"
#
# Prince.name = "Prince"
# Prince.group_member = 26
# Prince.group_name = "high coding gruop"

# print(Harry.print_details()
print(Prince.group_name)
