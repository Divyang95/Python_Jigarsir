#Function with no argument and no return value

def printLine():
    print("*"*45)

printLine()
print("Welcome to user Defined Function")
printLine()

#Function with argument but no  return value
def add(a,b):
    print("Addition : ",a+b)
    
printLine()
add(10,20)
printLine()

#Function with argument & return value
def sub(a,b):
    return a-b

printLine()
print(sub(10,20))
printLine()
