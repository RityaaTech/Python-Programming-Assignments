n = int(input("ENTER THE NUMBER : "))
count = 0
while(n>1):
    count = count + 1
    n = n // 10

print(f"COUNT OF THE DIGITS = {count}")

'''
ENTER THE NUMBER : 7521
COUNT OF THE DIGITS = 4
'''
