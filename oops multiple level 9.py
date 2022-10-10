class Dad:
    basketball = 1
    pass
class son(Dad):
    dance = 1
    def isdence(self):
        return f" Yes I dence {self.dance} no of time "

class Grandson(son):
    dance = 6
    def isdence(self):
        return f"Yes I dence awesomely {self.dance} no of time "

vishal = Dad()
Amit = son()
Prince = Grandson()

# print(Prince.isdence())
print(Prince.basketball)

# electronic device
# pocket gadget
# phone