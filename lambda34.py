# Lambada function or Anonymous function
def add(a,b):
    return a+b

minus = lambda a,b: a-b

# def minus(a,b):
#     return a-b
# print(minus(8,9))

# def a_fist(a):
#    return a[1]
a = [[8,7],[99,89],[6,2]]
a.sort(key= lambda o:o[1])
print(a)
