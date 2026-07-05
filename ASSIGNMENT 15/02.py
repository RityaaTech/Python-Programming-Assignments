number = [1,2,3,4,5,6,7,8,9,10]

def check_even(x):
    if (x%2==0):
        return True
    else:
        return False
    
data = list(filter(check_even,number))
print(data)
