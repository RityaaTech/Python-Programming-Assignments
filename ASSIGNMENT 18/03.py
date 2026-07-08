def Minimum(N):
    List = []
    for i in range(N):
        n = int(input("ENTER THE NUMBER : "))
        List.append(n)
        Result = min(List)

    return (f"MINIMUM NUMBER : {Result}")

print(Minimum(4))
