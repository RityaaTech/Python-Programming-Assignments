from functools import reduce

def Check_Prime(n):
    if (n<1 == 0):
        return False
    
    for i in range(2,n):
        if (n%i==0):
            return False

    return True

def Multiplication(n):
    return n*2

def Maximum(n):
    return max(n)


def main():
    Data = [2,70,11,10,17,23,31,77]
    F_Data = list(filter(Check_Prime,Data))
    print(f"LIST AFTER FILTER : {F_Data}")

    M_Data = list(map(Multiplication,F_Data))
    print(f"LIST AFTER MAP : {M_Data}")

    R_Data = reduce(Maximum,M_Data)
    print(f"LIST AFTER REDUCE : {R_Data}")

if __name__ == "__main__":
    main()