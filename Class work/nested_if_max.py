a = int(input("Enter value of A :"))
b = int(input("Enter value of B :"))
c = int(input("Enter value of C:"))

if a>b:
    if b>c:
        print(b,"is Max")
    else:
        print(c,"is Max")
elif b>c:
    print(b,"is Max")
else:
    print(c,"is Max")
