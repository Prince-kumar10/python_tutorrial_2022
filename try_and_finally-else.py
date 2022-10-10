f1 = open("prince .txt")

try:
    f = open("prince")

except EOFError as e:
    print("print eof error aa gaya hai ",e)

except IOError as x:
    print("print io error aa gaya hai ",x)

except Exception as a:
    print(a)


else:
    print("This will run only if  except is not running ")

finally:
    print("run this anyway....")
    f1.close()

print("important stuff")