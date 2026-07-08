def Maximum(N):
    list = []
    for i in range(N):
        n = int(input("ENTER THE NUMBER : "))
        list.append(n)

        Result = max(list)
    
    return (f"MAXIMUM NUMBER : {Result}")

print(Maximum(7))


       