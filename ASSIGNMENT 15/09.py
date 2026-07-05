from functools import reduce

number = [1,2,3,4,5,6,7,8,9,10]

def Product(x,y):
    return x*y

new_data = reduce(Product,number)
print(new_data)
