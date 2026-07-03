n = int(input("ENTER THE NUMBER : "))

reverse = 0
while(n>0):
    digit = n % 10
    reverse = reverse * 10 + digit 
    n = n // 10

print(f"REVERSE : {reverse}")

'''
ENTER THE NUMBER : 123
REVERSE : 321
'''