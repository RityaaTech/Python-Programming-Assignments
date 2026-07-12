import multiprocessing
import os

def Factorial(n):
    print(f"INPUT NUMBER : {n}")
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    
    return factorial

def main():
    print(f"PID OF MAIN : {os.getpid()}")
    data = [10,15,20,25]
    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial,data)
    pobj.close()
    pobj.join()
    print(f"RESULT : {Result}")

if __name__ == "__main__":
    main()

