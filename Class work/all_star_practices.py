print("*** Practice of all 20 patterns first start with star pattern all with nested for loop and sir method single line ***")
print("Start with Left angle triangle with and remember as print function moves cursor to new line automatically to stay in line use end='' ")
print("and to move in new line use print() because print() function moves cursor in new line automatically")
print()
n = int(input("Enter Number of Rows you want:"))

print("***left angle triangle using for loop****")

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

print()
print("***left angle triangle using sir method***")
for i in range(n+1):
    print("*"*i)

print("***Right angle triangle using for loop ****")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

print("***Right angle triangle using sir method****")
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)

print("*** Pyramid ***")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(" *",end="")
    print()

print("*** Reverse Pyramid ***")
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range((n+1)-i):
        print(" *",end="")
    print()


print("*** 1 12 123 *** pattern bydefault i and j starts with 0")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("*** 1 11  1234 ** left angle triangle")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()
    
print("***Right angle triangle 1 22 33")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(i,end="")
    print()

print("*** Pyramid with 1 22 33 ***")
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

print("*** reverse pyramid 1 12 123 ***")
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,(n+2)-i):
        print(k,end=" ")
    print()

print("**** right angle triangle using abcd 65-81 and big 97 to 113")
for i in range(65,76):
    for j in range(76-i):
        print(" ",end="")
    for k in range(65,i+1):
        print(chr(i),end=" ")
    print()
    

    




        
    

            
    
        

