n = int(input("ENTER THE NUMBER : "))
print("FACTORS ARE : ")
for i in range (1,n+1):
    if (n%i == 0):
        print(i,end = " ")

'''
ENTER THE NUMBER : 12
FACTORS ARE : 
1 2 3 4 6 12 

'''

