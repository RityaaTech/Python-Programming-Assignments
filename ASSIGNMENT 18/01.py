def Number():
    n = int(input("ENTER THE NUMBER OF ELEMENTS : "))
    list = []

    for i in range(n):
        number = int(input())
        list.append(number)
    
        total = sum(list)
    
    return total

print(Number())

   