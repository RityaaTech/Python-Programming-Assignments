import multiprocessing
import time
import os

def Check_Even(n):
    S = 0 
    for i in range(2,n+1,2):
        S = S + i
    return S
    print(f"PROCESS ID : {os.getpid()}")
    print(f"INPUT NUMBER : {n}")
    print(f"THE SUM OF THE EVEN NUMBERS : {S}")


def main():
   
    data = [1000000,2000000,3000000,4000000]
    
    pobj = multiprocessing.Pool()

    Result = pobj.map(Check_Even,data)

    pobj.close()
    pobj.join()

    print(f"THE SUM OF THE EVEN NUMBERS : {Result}")


if __name__ == "__main__":
    main()