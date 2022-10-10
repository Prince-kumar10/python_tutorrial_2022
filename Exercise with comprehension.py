print("what do you want to put in the comprehension")
comp = str(input())
print("what kind of comprehension do you want to make ")
print("press 1 for list comprehension ")
print("press 2 for set comprehension ")
print("press 3 for dictionary comprehension ")
comp2 = int(input())

if comp2 == 1:
    list2 = [i for i in comp]
    print(list2)
    print(type(list2))


if comp2 == 2:
    set3 = {item for item in [comp]}
    print(set3)
    print(type(set3))

if comp2 == 3:
    dict23 = {item: f"this is dict object {comp}"for item in range(1)}
    print(dict23)
    print(type(dict23))






