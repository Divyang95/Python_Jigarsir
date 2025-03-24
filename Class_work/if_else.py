'''
1. Simple IF

if condition:
    statement

2. If/Else

if condition:
    statement
else:
    statement

3.Nested If

if condition:
    if condition:
        statement
    else:
        statement
else:
    statement

4.ledder if
if condition:
    statement
elif condition:
    statement
elif condition:
    statement
else:
    statement

single =(means Assign value)
double == (means checking the value) it is called relational operator

'''

a = int(input("Enter Value of A : "))
#print("A:",a);
#print(type(a))
if a>0:
    print(a,"is positive number")
else:
    print(a,"is negative numbetr")

if a%2 == 0:
    print(a,"is Even number")
else:
    print(a,"is Odd number")

