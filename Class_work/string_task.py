s = input("Enter a string : ")
al=0
nm=0
up=0
lw=0
sp=0
sl=0

for i in s:
    if i.isalpha():
        al+=1
        if(i.isupper()):
            up+=1
        elif(i.islower()):
            lw+=1
    elif i.isnumeric():
        nm+=1
    elif i.isspace():
        sp+=1
    else:
        sl+=1

print("alphas are :",al);
print("upper are :",up);
print("lowers are :",lw);
print("numbers are :",nm);
