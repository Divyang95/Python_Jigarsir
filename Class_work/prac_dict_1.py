d1 = {
    "user":{"name":"Divyang","age":25},
    "location":"Ahmedabad",
    "skills":{"python":"Intermediate"}
    }
d2 = {
    "user":{"age":26,"city":"Mumbai"},
    "location":"Surat",
    "skills":{"Javascript":"Beginner"}
    }

d3 = {}
d3 = d1.copy()
print(d3)

d3.update(d2)
print(d3)
