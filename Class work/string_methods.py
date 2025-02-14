s=input("Enter a string : ")
total_alpha = 0
total_numeric = 0
total_space = 0

for i in range(len(s)):
    if(s[i].isalpha()):
        total_alpha+=1

print(total_alpha)
