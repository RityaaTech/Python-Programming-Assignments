number = [1,2,3,4,5,6,7,8,9,10]

def Count_Even(x):
    if (x%2==0):
        return x
    else:
        return False
    
data = len(list(filter(Count_Even,number)))
print(data)
