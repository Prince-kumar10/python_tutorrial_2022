# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input




class library:
    def __init__(self,Books_Available):
        self.Books_Available = Books_Available


    def show_books(self):
           return self.Books_Available

    # def return_book(self):



if __name__=='__main__':
    while(True):
        print("what do you want to do in the librery ")
        print("press 1 for display library books  ")
        print("press 2 for lend library books  ")
        print("press 3 for add library books ")
        print("press 4 for return the library book")
        a = int(input())

        prince = library("History\nSociology\nEnglish\nPunjabi\nPhysical\nHindi\ne.v.s\ncomputer\n")
        if a == 1:
            print(prince.show_books())

            w1 = (input("if you are continue press c if your stop then press s \n"))
            if w1 == "s":
                break
            if w1 == "c":
                continue

        if a == 2:
         print("Enter the name ")
         P1 = str(input())
         print("Enter the book name ")
         P2 = (input())

         P3 = {"Rajkumar": "English", "Kaushal": "History",
              "vishal": "physical"}


         if P2 == "english":
             print("People Have Taken This Books\n")
             print(P3)
         if P2 == "history":
             print(P3)
         if P2 == "physical":
             print(P3)


         elif P2 == "evs":
             P4 = {P1: P2}
             print(P4)
             print("We Are Saving Your Name Now You Can Take Your Book\n")

         elif P2 == "computer":
              P4 = {P1: P2}
              print(P4)
              print("We Are Saving Your Name Now You Can Take Your Book\n")


         elif P2 == "sociology":
            P4 = {P1: P2}
            print(P4)
            print("We Are Saving Your Name Now You Can Take Your Book\n")

         elif P2 == "punjabi":
            P4 = {P1: P2}
            print(P4)
            print("We Are Saving Your Name Now You Can Take Your Book\n")

         elif P2 == "hindi":
            P4 = {P1: P2}
            print(P4)
            print("We Are Saving Your Name Now You Can Take Your Book\n")



         w1 = (input("if you are continue press c if you stop then press s \n"))
         if w1 == "s":
             break
         if w1 == "c":
             continue

        if a == 3:
            print("Name the book which you want to add!")
            P5 = str(input())
            prince = library(f"History\nSociology\nEnglish\nPunjabi\nPhysical\nHindi\ne.v.s\ncomputer\n{P5}\n")
            print(prince.show_books())

            w1 = (input("if you are continue press c if you stop then press s \n"))
            if w1 == "s":
                break
            if w1 == "c":
                continue


































