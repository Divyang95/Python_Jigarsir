#UDF Library
def maxOfTwo(a,b):
    if a>b:
        print(a,"is max")
    else:
        print(b,"is max")

def maxOfThree(a,b,c):
    if(a>b):
        if(a>c):
            print(a,"is max")
        else:
            print(c, "is max")
    elif b>c:
        print(b,"is max")
    else:
        print(c,"is max")

def oddeven(a):
    if a%2 == 0:
        print(a,"is even")
    else:
        print(a,"is odd")

def fibonacci(n):
    a,b = 0,1
    print(a,end = " ")
    while b<n:
        print(b,end = " ")
        a,b = b,a+b
    print()
    
def prime(n):
    numberOfDivisbles = 0
    for i in range(1,n+1):
        if(n%i == 0):
            numberOfDivisibles += 1
    if(numberOfDivisibles == 2):
        print(n,"is prime Number")
    else:
        print(n,"is not prime")
            
    
