from functools import reduce


number = [1,2,3,4,5,6]

def addition(x,y):
    return x+y
    
new_data = reduce(addition,number)
print(new_data)
