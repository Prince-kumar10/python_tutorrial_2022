class genera():
     def __init__(self,name,number):
         self.name = name
         self.number = number

     def displayNum(self):
          return f"This is {self.name}  number {self.number}  "

     def gen(self,n):
         for i in range(n):
              yield(i)

     def fibIter(self,n):
          self.fibona1 = 0
          self.fibona2 = 1
          for i in range(1, n):
               numberNew = self.fibona1
               self.fibona1 = self.fibona2
               self.fibona2 = self.fibona1 + numberNew
          return self.fibona2



if __name__ =='__main__':
     prince = genera("fiboncci sequence",[1,1,2,3,5,8,13,21,34,55])
     print(prince.displayNum())
     fib = int(input("Enter the fibonacci sequence number "))
     gene = prince.gen(fib)
     print(prince.fibIter(fib))


     # prince.gen(12)




     # print(f)
     # print(f.__next__())
     # print(f.__next__())
     # for i in f:
     #      print(i)