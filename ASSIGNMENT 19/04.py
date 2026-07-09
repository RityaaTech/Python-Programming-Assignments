from functools import reduce

def Check_Odd_Even(n):
    if (n%2==0):
        return True
    else:
        return False
    
def Square(x):
    return x*x

def Addition(x,y):
    return x+y

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]

    F_Data = list(filter(Check_Odd_Even,Data))
    print(f"DATA AFTER FILTER : {F_Data}")

    M_Data = list(map(Square,F_Data))
    print(f"DATA AFTER MAP :{M_Data}")

    R_Data = reduce(Addition,M_Data)
    print(f"DATA AFTER REDUCE : {R_Data}")


if __name__ == "__main__":
    main()