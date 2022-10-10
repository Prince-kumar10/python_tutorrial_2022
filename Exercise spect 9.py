# import inspect
#
# class A(object):
#     pass
#
# print(inspect.isclass(A))

# import inspect
# import numpy
#
# print(inspect.ismodule(numpy))


import inspect

f = inspect.currentframe()
i =  inspect.getframeinfo(f)

print(f.f_lineno)
# print(f.f_locals)
print(i.filename)
print(i.function)


