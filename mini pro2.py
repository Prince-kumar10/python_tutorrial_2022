import time
class library():
    def __init__(self,list23,name):
        self.list_book = list23
        self.name = name
        self.dictionary12 = {}

    def display(self):
        print(f"This is name of {self.name}")
        for i in self.list_book:
            print(i)


    def lend_book(self,asked1,asked2 ):
        if asked2 not in self.dictionary12.keys():
            self.dictionary12.update({asked1:asked2})
            print("some time wait for pressing")
            time.sleep(1)
            print(self.dictionary12)
            print("please take your book\n")

    def add_book(self,asked3):
        self.list_book.append(asked3)
        print("your book add to the list")

    def return_book(self):



if __name__=='__main__':
    prince_library = library(["english", "math", "hindi", f"gorw and rich"], "Prince Library")
    while(True):
        print("what do you want to do in the librery ")
        print("press 1 for display library books  ")
        print("press 2 for lend library books  ")
        print("press 3 for add library books ")
        print("press 4 for return the library book")
        a = int(input())

        if a == 1:
            prince_library.display()

            loop12 =(input("if you press s for stop and continue for press c "))
            if loop12 == "s":
                break
            if loop12 == "c":
                continue

        elif a == 2:
            asked1 = input("Enter the book ")
            asked2 = input("Enter the name ")
            prince_library.lend_book(asked1,asked2)
            loop12 = (input("if you press s for stop and continue for press c "))
            if loop12 == "s":
                break

            if loop12 == "c":
                continue


        elif a == 3:
            print("Name the book watch you want to add")
            asked3 = str(input())
            prince_library.add_book(asked3)





























