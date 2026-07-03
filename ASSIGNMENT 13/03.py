n = int(input("ENTER THE NUMBER : "))
sum = 0
for i in range (1,n):
    if (n%i == 0):
        sum = sum + i

if (sum == n):
    print(f"{n} IS PERFECT NUMBER")
else:
    print(f"{n} IS NOT PERFECT NUMBER")

'''
ENTER THE NUMBER : 6
6 IS PERFECT NUMBER
'''