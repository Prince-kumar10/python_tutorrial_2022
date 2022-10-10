# diamond shape in python

class A:
    def met(self):
        print("This  is a method from class A")
    pass
class B(A):
    def met(self):
        print("This  is a method from class B")

class C(A):
    def met(self):
        print("This  is a method from class C")
    pass
class D(C,B):
    pass

a = A()
b = B()
c = C()
d = D()

d.met()