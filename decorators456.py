# DECORATORS IN PYTHON

# def function():
#     print("This is me prince ")
# func2 = function()
# print(func2)


# def function2(x):
#     if x == 0:
#         return print
#     if x == 1:
#         return sum
# a = function2(1)
# print(a)

def suare(fun1):
        def cube():
           print("Movie club")
           fun1()
           print("chnnal subscribe")
        return cube

@suare
def oppo():
    print("this is me prince")


# oppo = suare(oppo)
oppo()

