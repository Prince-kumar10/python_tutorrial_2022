# comprehension in python

# list comprehension
# ls = [ ]
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

ls = [i for i in range(100) if i%3 == 0 ]
# print(type(ls))
# print(ls)



# dictionary comprehension
# dict1 = {i:f"item{i}" for i in range(1,100) if i%2 == 0}
# print(dict1)

dict1 = {i: f"item{i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)


# set comprehension
dresses = {dress for dress in ["dress1" ,"dress2","dress1" ,"dress2","dress1" ,"dress2"] }
# print(dresses)



# generator comprehension
even = (i for i in range(100) if i%3 == 0)
print(type(even))
# print(even.__next__())
# print(even.__next__())
for i in even:
  print(i)