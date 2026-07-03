print(" START OF THE PROGRAM ".center(50,"="),end = "\n\n")

n = int(input("ENTER THE NUMBER : "))

fact = 1
for i in range (1,n+1):
    fact = fact * i

print(f"FACTORIAL OF NUMBER {n} IS {fact}",end = "\n\n")

print(" END OF THE PROGRAM ".center(50,"="))


'''
OUTPUT : 
============== START OF THE PROGRAM ==============

ENTER THE NUMBER : 5
FACTORIAL OF NUMBER 5 IS 120

=============== END OF THE PROGRAM ===============
'''