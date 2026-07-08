#print(dir(str))

def Check_Digits(n):
    count = 0

    while(n>0):
        count = count + 1
        n = n//10
    
    return count

print(Check_Digits(5187934))
