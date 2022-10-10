import time

initial = time.time()
print(initial)

k = 0
while(k<45):
    time.sleep(2)
    print("This is prince bhai")
    k+=1
print("while loop ran in",time.time() - initial,"seconds")
#
# initial2 = time.time()
# for i in range(45):
#     print("This is not prince bhai")
#     print(i)
# print("for loop ran in",time.time() - initial2,"seconds")

# localtime = time. asctime(time.localtime(time.time()))
# print(localtime)