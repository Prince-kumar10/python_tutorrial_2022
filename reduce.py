from functools import reduce

list12 = [1,2,3,4,]
# num = 0
# for i in list12:
#     num = num + i
# print(num)
num = reduce(lambda x,y:x+y,list12)
print(num)


