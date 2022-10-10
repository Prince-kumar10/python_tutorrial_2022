# l = 40  #global
# def function1(n):
#     global l
#     # l = 100  # Local
#     y = y + 200  # Local
#     print(n, "I have printed ")
#     print(l,y)
# function1("This is me ")
# # print(l)



y = 20

def harry():
    x = 100
    def prince():
        global y
        y = 200
    print("Today calling harry",x)
    prince()
    print ("after calling prince ",x)
harry()
print(y)



