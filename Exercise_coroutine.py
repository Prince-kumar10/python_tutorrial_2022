def search_name():
    import time
    list12 =[]
    time.sleep(2)
    print("Enter the coroutine what you want to add")
    for i in range(3):
      add = str(input())
      list12.append(add)

    while(True):
        text = (yield)
        if text in list12:
            print("you name is added ")
        else:
            print("your name is not added sorry!")


if __name__=='__main__':
    print("coroutines is starting")
    search = search_name()
    next(search)
    name2 = str(input("Enter the name"))
    search.send(name2)
    print(type(search))
    search.close()









