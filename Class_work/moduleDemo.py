import UDF

while True:
    print("*"*30)
    print("1. Max of Two")
    print("2. Max of Three")
    print("3. Odd Even")
    print("4. Fibonacci Series")
    print("5. Prime Number")
    print("6. Exit")
    print("*"*30)

    choice = int(input("Enter your Choice: "))
    print("*"*30)
    if choice == 1:
        n1 = int(input("Enter Number : "))
        n2 = int(input("Enter Number : "))
        UDF.maxOfTwo(n1,n2)
        print("*"*30)

    elif choice == 2:
        n1 = int(input("Enter Number : "))
        n2 = int(input("Enter Number : "))
        n3 = int(input("Enter Number : "))
        UDF.maxOfThree(n1,n2,n3)
        print("*"*30)

    elif choice == 3:
        n2 = int(input("Enter Number : "))
        UDF.oddeven(n2)
        print("*"*30)
        
    elif choice ==4:
        n1 = int(input("Enter Number: "))
        UDF.fibonacci(n1)
        print("*"*30)
    elif choice == 5:
        n1 = int(input("Enter a Number : "))
        UDF.prime(n1)
        print("*"*30)
    elif choice == 6:
        print("Thank You for using our services")
        break
    
        
