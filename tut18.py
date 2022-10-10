
# Sanke water Gun in python
# The snake drinks the water ,the gun shoots the sanke,and gun has no effect  on water

import random


start_number = 9
first = ["s" ,"w" ,"g"]
computer_number = 0
human_point = 0

print("SANKE WATER GUN GAME" )
print()
print("Choice the one character")

for i in range(start_number):
    input1 = str(input("1 press S SNAKE 2 press W WATER 3 press G GUN:"))
    choice = random.choice(first)
    print(choice)
    if input1 == choice:
        print(" you both are equal\n")

    elif input1 == 's' and choice == 'g':
        print("The match winner is computer\n")
        computer_number = computer_number+1
        print(f"you guess {input1} and computer guess is {choice}\n")
        print("computer win 1 point\n")
        print(f"computer point is {computer_number} and human point is{human_point}\n")

    elif input1 == 'g' and choice == 's':
        print("The match win is human\n")
        human_point = human_point +1
        print(f"you guess {input1} and comupter guess is {choice}\n")
        print("human win 1 point\n")
        print(f"computer point is {computer_number} and human point is {human_point}\n")

    elif input1 == 's' and choice == 'w':
        print("The match win is human\n")
        human_point = human_point + 1
        print(f"you guess {input1} and computer guess is {choice}\n")
        print("human win 1 point\n")
        print(f"computer point is {computer_number} and human point is {human_point}\n")

    elif input1 == 'w' and choice == 's':
        print("The match win is computer\n")
        computer_number = computer_number + 1
        print(f"you guess {input1} and comupter guess is {choice}\n")
        print("comupter win 1 point\n")
        print(f"comupter point is {computer_number} and human point is {human_point}\n")

    elif input1 == 'g' and choice == 'w':
        print("The match win is comuter\n")
        comupter_number = computer_number + 1
        print(f"you guess {input1} and computer guess is {choice}\n")
        print("computer win 1 point\n")
        print(f"computer point is {computer_number} and human point is {human_point}\n")

    elif input1 == 'w' and choice == 'g':
        print("The match win is human\n")
        human_point = human_point + 1
        print(f"you guess {input1} and computer guess is {choice}\n")
        print("Human win 1 point\n")
        print(f"computer point is {computer_number} and human point is {human_point}\n")
    else:
        print("This is Not a Correct Character Please Try Again\n")

start_number = start_number + 1
print(f"{start_number} is left")
print("Game Over")

if computer_number == human_point:
    print("Game is Tie")

elif computer_number > human_point:
    print("The match winner is computer")

else:
    print("The match winner is human")

    print(f"computer point is {computer_number} and human point is {human_point}\n")



