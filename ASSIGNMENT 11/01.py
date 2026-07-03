n = int(input("ENTER THE NUMBER : "))

if (n > 1):
    for i in range(2,n):
        if (n % i == 0):
            print(f"{n} IS NOT PRIME NUMBER.")
            break
        else:
            print(f"{n} IS PRIME NUMBER.")
    else:
        print("NOT PRIME NUMBER.")

'''
ENTER THE NUMBER : 11
11 IS PRIME NUMBER.
'''