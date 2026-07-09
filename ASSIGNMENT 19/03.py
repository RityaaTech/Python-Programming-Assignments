from functools import reduce

def Check_Number(n):
    if (n>=70 and n<=90):
        return True
    else:
        return False

def Product(x,y):
    return x*y

def Increase(n):
    return n+10


def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70] 
    
    F_Data = list(filter(Check_Number,Data))
    print(f"LIST AFTER FILTER : {F_Data}")

    M_Data = list(map(Increase,F_Data))
    print(f"LIST AFTER MAP : {M_Data}")

    R_Data = reduce(Product,M_Data)
    print(f"LIST AFTER REDUCE : {R_Data}")

if __name__ == "__main__":
    main()
