n = 18

print(" number of guesses only 9 times ")

guesses_of_number = 1
while(guesses_of_number <=9):
    print(guesses_of_number )
    guesses_of_number = guesses_of_number + 1
    n1 = int(input(" guess the number\n "))
    if n1 < 18:
        print(" you guesses the big number\n")
    elif n1 > 18:
        print("you guesses the small number\n")
    elif n1 == 18:
        print(guesses_of_number,"guesses he took to finish")
        print("you are winner")
        break
    if(guesses_of_number==10):
      print("Gmae over")


















