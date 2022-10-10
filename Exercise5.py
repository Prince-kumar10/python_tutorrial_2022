
def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


print("Health management system")
print("1 Do you want to see\n2 if you want to write ")
write = int(input())
if write > 2:
    print("This is incorrect number Error")

print("Choice Any One Charator")
print("1 harry\n2 rohan\n3 hammad")
n1 = int(input())
if n1 > 3:
    print("This is incorrect number Error")
print()
print("what do you want ")
print("1 exercise\n2 food")
n2 = int(input())
if write == 2:
    print("type here")
n4 = str(input())

if write == 2:
    if n2 == 1 and n1 == 1:
        f = open("harry.exercise", "a")
        f.write(n4)
        print("1successfully add")

if write == 1:
    if n2 == 1 and n1 == 1:
        f = open("harry.exercise", "r")
        content = (f.read())
        print(content)
        for line in f:
            print(line)

if write == 2:
    if n2 == 2 and n1 == 1:
        f = open("harry.food", "a")
        f.write(n4)
        print("2successfully add")

if write == 1:
    if n2 == 2 and n1 == 1:
        f = open("harry.food", 'r')
        content = (f.read())
        print(content)
        for line in f:
            print(line)

if write == 2:
    if n1 == 2 and n2 == 1:
        f = open("rohan.exercise", "a")
        f.write(n4)
        print("3successfully add")

if write == 1:
    if n1 == 2 and n2 == 1:
        f = open("rohan.exercise", 'r')
        content = (f.read())
        print(content)
        for line in f:
            print(line)

if write == 2:
    if n1 == 2 and n2 == 2:
        f = open("rohan.food", "a")
        f.write(n4)
        print("4successfully add")

if write == 1:
    if n1 == 2 and n2 == 2:
        f = open("rohan.food", 'r')
        content = (f.read())
        print(content)
        for line in f:
            print(line)

if write == 2:
    if n1 == 3 and n2 == 1:
        f = open("hammad.exercise", "a")
        f.write(n4)
        print("5successfully add")

if write == 1:
    if n1 == 3 and n2 == 1:
        f = open("hammad.exercise")
        content = (f.read())
        print(content)
        for line in f:
            print(line)

if write == 2:
    if n1 == 3 and n2 == 2:
        f = open("hammad.food", "a")
        f.write(n4)
        print("6successfully add")

if write == 1:
    if n1 == 3 and n2 == 2:
        f = open("hammad.food")
        content = (f.read())
        print(content)
        for line in f:
          print(line)