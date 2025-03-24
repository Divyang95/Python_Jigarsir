import random

file = open("odd_even_data.txt","w")
for i in range(10):
    if(i == 9):
        file.write(str(random.randint(1,100)))
    else:
        file.write(str(random.randint(1,100))+",")

print("10 random number written inside odd_even_data.txt file")
file.close()

file = open("odd_even_data.txt","r")
odd = open("odd_elements.txt","w+")
even = open("even_elements.txt","w+")
prime = open("prime_elements.txt","w+")

str_file = file.read()
list_each_data = str_file.split(",")[:-1]



for item in list_each_data:
    divisible_count = 0
    for i in range(1,int(item)+1):
        if(int(item)%i == 0):
            divisible_count+=1
    if(divisible_count == 2):
        prime.write(item+",")
            

for item in list_each_data:
    if(int(item)%2 == 0):
        even.write(item+",")
    else:
        odd.write(item+",")
print("** written in main file **")
file.seek(0)
print(file.read())
print("** print in prime file**")
prime.seek(0)
print(prime.read())
print("** print in odd file **")
odd.seek(0)
print(odd.read())
print("** print in even file **")
even.seek(0)
print(even.read())

file.close()
odd.close()
even.close()
prime.close()

    

