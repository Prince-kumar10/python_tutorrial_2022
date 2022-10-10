# TRY EXCEPT IN PYTHON

""""
Handling In Python
Before discussing exceptional handling
, let us discuss, what an exception is 
actually.

“Exception can be said as an error, that
causes a program to crash. Unlike syntax
error, it is syntactically correct and
occurs mostly due to our negligence
"""""


print("Enter the frist number ")
n1 = (input())
print ("Enter the second number ")
n2 = (input())

try:
    print("The sum of these number is ",
          int(n1) + int(n2))
except Exception as e:
    print(e)

print("This line is very important")
