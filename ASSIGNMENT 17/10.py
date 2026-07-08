def Addition(n):
    total = 0

    while n > 0 :
        total = total + (n%10)
        n = n // 10

    return total
    
print(Addition(5187934))
