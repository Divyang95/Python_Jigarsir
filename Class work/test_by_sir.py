print("**** Test *** 65-81 and 97 to 113")

n1 = int(input("Enter rows you want : "))
chr_ = 65

for i in range(1,n1+1):
    for j in range(i):
        if (chr_% 2 == 0):
            print(chr(chr_+32),end="")
        else:
            print(chr(chr_),end="")
        chr_+=1
    print()



print("*** Prime Number ****")

n = int(input("Enter number for checkiing whether number is prime or not :"))

nosp = 0

for i in range(1,n+1):
    if(n%i==0):
        nosp+=1

if(nosp == 2):
    print("Given numver is prime")
else:
    print("Given number is not prime number")

