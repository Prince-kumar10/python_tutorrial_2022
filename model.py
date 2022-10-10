
class Library:
    def __init__(self,list1,name):
        self.book_list1 = list1
        self.name = name
        self.lenddict = {}

    def display_books(self):
        print(f"we have following books in library: {self.name}")
        for item in self.book_list1:
            print(item)

    def lend_book(self,book,name):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:name})
            print("we have update our data you can take book now")
            print(self.lenddict)
        else:
            print("sorry book is not available")

    def add_book(self,book):
        self.book_list1.append(book)
        print("book has been added to list")

    def return_book(self,book):
        self.lenddict.pop(book)
        print("this book has been return")


if __name__ == '__main__':
    jatin = Library(["space atlas","zero to one","rich dad poor dad","hyper focus","space time"],"jatinlibrary")
    while(True):
        print("press 1. for display books")
        print("press 2. for lend book")
        print("press 3. for add book")
        print("press 4. for return book")
        ur_choice = input()
        if ur_choice not in ['1', '2', '3', '4']:
            print("please cooperate with library manager")
        else:
            ur_choice = int(ur_choice)

        if ur_choice == 1:
            jatin.display_books()
        elif ur_choice == 2:
            print("enter book you want to lend")
            book = input()
            print("enter your name")
            name = input()
            jatin.lend_book(book, name)
        elif ur_choice == 3:
            print("enter book you want to add in library")
            book = input()
            jatin.add_book(book)
        elif ur_choice == 4:
            print("book you want to return")
            book = input()
            jatin.return_book(book)
        else:
            print("please enter suitable input")


        print("press q to quit and c to continue")
        lastchoice = input()
        if lastchoice=="q":
            exit()
        elif lastchoice=="c":
            continue
        else :
            print("not valid choice, But thanks for coming")
            exit()


# dict1 = {"apple":"eat","rad":"rad colour is very beautiful"}
# prince = {"prince":"eat apple always"}
#
#
# dict1.update(prince)
# print(dict1)
#
#
#
# key1 = {"one":"one is bad number ","two":"two is nice number "}
#
# print(key1.keys())

# while(True):
#     dict12 = {            }
#     gg = (input("enter the first name "))
#     g12 = (input("enter the second name "))
#
#     dict12.update({gg:g12})
#     print(dict12)


    #
    # def lend_book(self,book,name):
    #     if book not in self.lenddict.keys():
    #         self.lenddict.update({book:name})
    #         print("we have update our data you can take book now")
    #         print(self.lenddict)
