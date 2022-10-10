# generator in python

"""""""""
iterable - __iter__() or__getitem__()
iterator - __next__()
iteration -
"""

def gen(n):
    for i in range(n):
        yield(i)

g = gen(7)
# print(g)

# print(type(g))

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

# this is iterable
# p = "prince"

p = "prince"
ite = iter(p)
print(ite.__next__())
print(ite.__next__())



# print(p[1])
# print(iter(p))
# for i in p:
#     print(i)



a = "prince"
for c in a:
      print (a)
# Here a is an iterable.



