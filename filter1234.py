# oppo = [1,2,3,4,5,6,7,8]
#
# def square(x):
#     return x>5
#
# cube = list(filter(square,oppo))
# print(cube)


numbers12 = [2,34,8,67,78,4,]
def high_marks(x):
    if  x > 2:
        return True

def low_marks(y):
    if y < 78:
         return False
#
func = [high_marks,low_marks]
oppo = list(filter(high_marks,numbers12))
print(oppo)