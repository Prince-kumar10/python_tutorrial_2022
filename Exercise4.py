print("How to print * line ")
num1 = int(input())
print("0 or 1")
num2 = int (input())
num3 = bool(num2)
if num3 == True:
    for e in range(1,num1,+1):
        for w in range(1,num1 +1):
         print("*",end="")
        print()
if num3 == False:
  for i in range(num1,0,-1):
        for o in range(1,i+1):
            print("*", end="")
        print()








#
# print("How match * printed  ")
# n1 = int(input())
# print("0 or 1")
# n2 = int(input())
# n3 = bool(n2)
# if n3 == True:
#     for i in range(1,n1+1):
#         for o in range(1, i+1):
#             print("*", end="")
#         print()
# if n3 == False:
#     for i in range(n1,0,-1):
#         for o in range(1,i+1):
#             print("*", end="")
#         print()
#
