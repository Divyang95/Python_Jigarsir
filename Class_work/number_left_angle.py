'''
print("****right angle 1 222 333 4444 pattern ****")
'''
n = int(input("Enter a number of rows : "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()


print("***** Left angle triangle ***")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


print("******* Right angle triangle and pyramid ****")
for i in range(10):
    print(" "*(9-i),end="")
    for j in range(1,i):
        print(j,end = " ")
    print()

print("Reverse pyramid")
for i in range(10):
    print(" "*(i), end="")
    for j in range(1,10-i):
        print(j, end=" ")
    print()

'''
print("**** Alphabet ****")
abcd = ["A","B","C","D","E","F","G","H","I","J","K"]
for i in range(abcd.len()):
    print(" "*(9-i), end="")
    for j in range(1,i):
        print(j, end=" ")
    print()
'''

for i in range(97,105):
    print(" "*(105-i),end ="")
    for j in range(97,i):
        print(chr(j), end=" ")
    print()
