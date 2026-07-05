number = [3,15,30,27,9,12]

def Divisible(x):
    if (x%3 == 0 and x%5 == 0):
        return True
    else:
        return False
    
data = list(filter(Divisible,number))
print(data)
