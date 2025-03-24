#decorator is function that takes another function as argument returns a new function with enhanced functionality
def decorator(f):
    def sample():
        print("This is before function")
        f()
        print("This is after function")
    return sample

@decorator
def star():
    print("*"*50)
    
#it means star = decorator(star), it means inside star = sample stored when decorator applied inside star wrapper or sample is stored
#when we call star means we are calling sample() and whatever we want to before calling f() which is original function star
#decorator argument should pass above star
    

star()

#generator : is a special type of function that returns an iterator object instead of using return to send back single value generator function use yield to produce a series of results over time
#This allows the function to generate values and pasuse its execution after each yield maintaining its state b/w iteration
#iterator means list tuple dictionary means which have multiple data is called iterator on which we can run loop is called iterotor object (OBJECT)

def even(num):
    cnt = 1
    while cnt<=num:
        if(cnt%2==0):
            yield cnt
        cnt+=1
        

ctr = even(10)
print(ctr)
for n in ctr:
    print(n)
    

