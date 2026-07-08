from MarvellousNum import Check_Prime

def List_Number(N):
    list = []
    for i in range(N):
        number = int(input("ENTER THE NUMBER : "))
        list.append(number)

    total = 0
    for i in list:
        if Check_Prime(i):
            total = total + i
        return total 
    
    Result = List_Number(N)
    return Result

print(List_Number(11))

