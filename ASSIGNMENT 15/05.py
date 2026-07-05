from functools import reduce


number = [1,2,3,4,5,6,7,8,9,10]

def maximum(x,y):
    if (x>y):
        return x
    else:
        return y
    
Data = reduce(maximum,number)
print(Data)


