n = int(input("ENTER THE NUMBER : "))
sum = 0
while (n>0):
    digit = n % 10
    sum = sum + digit 
    n = n//10
print(f"SUM OF THE DIGITS : {sum}")

'''
ENTER THE NUMBER : 123
SUM OF THE DIGITS : 6
'''