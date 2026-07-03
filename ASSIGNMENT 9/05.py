print(" START OF THE PROGRAM ".center(50,"="),end = "\n\n")

def Check(x):
    if (x % 3 == 0 and x % 5 == 0):
        print(f"{x} IS DIVISIBLE BY 3 AND 5")
    else:
        print(f"{x} IS NOT DIVISIBLE BY 3 AND 5")

Check(15)

print(" END OF THE PROGRAM ".center(50,"="))

'''
OUTPUT :
============== START OF THE PROGRAM ==============

15 IS DIVISIBLE BY 3 AND 5
=============== END OF THE PROGRAM ===============

'''