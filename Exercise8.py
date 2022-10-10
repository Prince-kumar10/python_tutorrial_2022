class Electronic_device():
     mobile_version = 90123
     def print_versoin(self):
         return f" This is my new phone" \
                f" version {self.mobile_version} "

class Pocket_gadget(Electronic_device):
    new_gadget = "loptop"

    def print_gadget(self):
        return  " This is my new gadget" \
               f" is {self.new_gadget} "

class Phone(Pocket_gadget):
    new_phone = "iphone 13"

    def phone_updated(self):
        return f"This is new phone updated {self.new_phone}"

Prince = Electronic_device()
harry = Pocket_gadget()
balraj = Phone()

print(Prince.print_versoin())
print(harry.print_gadget())
print(balraj.phone_updated())

print(Phone.mobile_version)
print(Phone.new_gadget)