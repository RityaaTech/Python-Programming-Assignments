print(" START OF THE PROGRAM ".center(50,"="),end = "\n\n")

n = int(input("ENTER THE NUMBER : "))

sum = 0
for i in range(1,n+1):
    sum = sum + i

print(f"SUM OF THE NUMBER {n} : {sum}",end = "\n\n")

print(" END OF THE PROGRAM ".center(50,"="))

'''
OUTPUT : 
============== START OF THE PROGRAM ==============

ENTER THE NUMBER : 5
SUM OF THE NUMBER 5 : 15

=============== END OF THE PROGRAM ===============
'''

