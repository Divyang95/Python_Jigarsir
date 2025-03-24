'''

*
**
***
****
*****
******

'''

n = int(input("Enter No of rows : "))

for i in range(1,n+1,1):
    for j in range(0,i,1):
        print("*",end="")
    print()

print("************** Right Angle Triangle ********")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

print("*****Single line left angle triangle as per sir *******")
for i in range(1,n+1):
    print("*"*i)

print("*****Single line right angle triangle as per sir *******")
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)
