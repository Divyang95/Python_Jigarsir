#fibonacci searies
#0 1 1 2 3 5 8 13 21 34 89

n = int(input("Enter N :"))

a,b = 0,1
print(a, end=" ")

while(b<n):
    print(b,end=" ")
    a,b = b,a+b

print()
print("***Same fibonacci series****")
print()
c,d = 0,1
print(c,end=" ")
for i in range(n):
    print(d,end=" ")
    c,d = d,c+d
    if (d>n):
        break
    
    
