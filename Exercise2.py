# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

while(True):
  n1 = int(input("Enter the frist number "))
  n2 = int(input("Enter the second number "))
  n3 = input('so what you want? ' + '+,-,/,%,* ')
  if n1 == 45 and n2 == 3 and n3 == '*':
    print(555)

  elif n1 == 56 and n2 == 9 and n3 == '+':
    print(77)
    break

  elif n1 == 56 and n2 == 6 and n3 == '/':
    print(4)
    break

  elif n3 == '+':
    pr1 = n1 + n2
    print(pr1)
    break

  elif n3 == '-':
    pr2 = n1 - n2
    print(pr2)
    break

  elif n3 == '*':
    pr3 = n1 * n2
    print(pr3)

  elif n3 == '/':
    pr4 = n1 / n2
    print(pr4)
    break

  elif n3 == '%':
    pr5 = n1 % n2
    print(pr5)
    break

  else:
    print("Error! Please check your input")
    continue
