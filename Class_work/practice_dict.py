d1={"a":5,"b":6,"c":7}
d2={"a":10,"c":20,"d":30}
d3={}

d3 = d1.copy()
print(d3)
d3.update(d2)
print(d3)

for key3 in d3:
    for key1 in d1:
        if(key3 == key1):
            d3[key3] = [d3[key3],d1[key1]]

print(d3)
