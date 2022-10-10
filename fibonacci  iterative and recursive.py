def fiboIter(n):
    prevNum = 0
    currentNum = 1
    for i in range(1, n):
        prevprevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prevprevNum
    return currentNum



def fiboRecur(n):
    if n==0:
        return 0
    elif (n==1):
        return 1
    else:
       return fiboRecur(n-1) + fiboRecur(n-2)



if __name__=='__main__':
    num = int(input("Enter the fibonacci number "))
    print(f" using recursion value of fib ({num}) is {fiboRecur(num)}")
    print(f" using recursion value of fib ({num}) is {fiboIter(num)}")


