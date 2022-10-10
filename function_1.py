# function in python

"""""""""
Functions And Docstrings

 “Functions in Python can be defined as lines of codes 
 that are built to create a specific task and
can be used again and again in a program when called.”
There are two types of functions in the Python language:

Built-in functions
User-defined functions
We have used a lot of built-in functions in our code till now, 
these functions include print(), or sum(), etc.
So, we have a good idea about how to call a function.
Built-in functions are already present in our python program, and we 
just have to call them whenever we need them to execute.

"""""



# a = 9
# b = 7
# num = sum((a,b)) #built in  function
# print(num)

def function1(a,b):
    print("Hello you are in funcion ",a+b)

def function2(a,b):
    """This is a function which will calculate of average of two number
      This function doesnt work for three number """
    average = (a+b)/2
    # print(average)


    return average
v =(function2(9,9))
# print(function1(9,9))
# print(v)

print(function2.__doc__)