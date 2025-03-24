print("Start Code")

try:
    a = int(input("Enter A :"))
    b = int(input("Enter B :"))
    c = a/b
    print("Division : ",c)
    l = ["java","javascript","nodejs","AI"]
    index = int(input("Enter index number : "))
    print(l[index])
except ZeroDivisionError as e :
    print("Except Caught : ",e)
except ValueError as e :
    print("Exception Caught : ",e)
except IndexError as e:
    print("Exception caught : ",e)
print("End code")
    
