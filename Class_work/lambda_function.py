cube1 = lambda x:x**3
print(cube1(5))

ans = lambda a,b:a if a>b else b
print(ans(10,20))

odd_even = lambda a:"is even" if a%2 == 0 else "is odd"

print(odd_even(20))

max_of_three = lambda x,y,z : f"{x} is max" if(x>y and x>z) else (f"{y} is max" if y>z and y>x else f"{z} is max") 
print(max_of_three(10,20,30))
