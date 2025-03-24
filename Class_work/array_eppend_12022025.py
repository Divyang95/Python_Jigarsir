l = []

print("any value between 2000 to 3200 which is divisible by 5 byut not divisible by 7")
print()

for i in range(2000,3201):
    if i%5==0 and i%3 ==0:
        l.append(i)

print(l)
