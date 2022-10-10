# map function in python


# numbers = ["12","89","34","9","7"]
# numbers= list(map(int,numbers))

# for i in range(len(numbers)):
#      numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] +1
# print(numbers[2])



def sqe(a):
   return a+a

num = [2,3,4,5,6,7]
square = list(map(sqe,num))
print(square)


#
# oppo = [12,3 ,21,15,18,]
# add = list(map(lambda x:x*x,oppo))
# print(add)





# def square(x):
#    return x*x
#
# def cube(y):
#    return y*y*y
#
# func = [square,cube]
# for i in range(5):
#    oppo = list(map(lambda x:x(i),func))
#    print(oppo)
