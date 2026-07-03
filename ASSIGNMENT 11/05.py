n = int(input("ENTER THE NUMBER :  "))
original = n 
reverse = 0 

while(n>0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if (original == reverse):
    print("PALINDROME")
else:
    print("NOT PALINDROME")

'''
ENTER THE NUMBER :  121
PALINDROME
'''
