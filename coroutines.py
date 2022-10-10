def searcher():
    import time
    # some 4 seconds time consuming task
    book = "This is book write prince is very hardworking   "
    time.sleep(4)

    while(True):
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book ")

search = searcher()
next(search)
input("press any key ")

search.send("prince")
input("press any key ")
search.send("prince is ")
input("press any key ")
search.send(" nice coder")
input("press any key ")
search.send("i am like harry video")
search.close()


