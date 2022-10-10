class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "instance var in class A"
        self.special = "special"

class B(A):
  classvar2 = "I am a in class B"

  def __init__(self):
      # super().__init__()
      self.var1 = "I am inside class B's constructor"
      self.classvar1 = "instance var in class B"
      super().__init__()
      print(super().classvar1)

a = A()
b = B()

# print(b.classvar1)
print(b.special,b.var1,b.classvar1)