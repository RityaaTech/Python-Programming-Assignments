def Number(N):
    List = []
    for i in range(N):
        n = int(input("ENTER THE NUMBER : "))
        List.append(n)

    Search = int(input("ENTER THE NUMBER YOU WANT TO COUNT : "))
    Result = List.count(Search)

    return Result

print(Number(11))