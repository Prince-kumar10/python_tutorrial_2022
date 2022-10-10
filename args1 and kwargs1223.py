# def function_name_point(a,b,c,d):
#     print(a,b,c,d,)
#
# function_name_point("datta","rohan","hassan","kaushal")


def function(normal,*args,**kwargs):
    print(type(args))
    # print(args[5])
    print(normal)
    for item in args:
        print(item)

    print("\nNow i would like to introduce some of our heroes\n")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

last1 = ["balraj", "vishal", "sammer"
        ,"sKillf","hammad","shivam","harry"]

normal = "I am a normal argument and the student are"
kwargs = {"prince":"fitness instructor","harry":
         "monitor","The programmer":"coodinator"}

function(normal,*last1,**kwargs)