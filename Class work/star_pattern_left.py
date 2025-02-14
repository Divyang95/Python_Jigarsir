'''
*
**
***
****
*****

    *
   **
  ***
 ****
*****
'''

n = int(input("Enter N : "))

for i in range(1,n+1):
    print("*"*i)

print("Star pattern left angle")

for i in range(1,n+1):
    print(" "*(n-i), "*"*i)

        
for i in range(1,n+1):
    print(" "*(n-i), " *"*i)

for i in range(n,0,-1):
    print(" "*(n-i), " *"*i)
    
