import multiprocessing
import os

def Odd_Count(n):
    count = (n+1)//2
    print(f"INPUT NUMBER : {n}")
    print(f"ODD NUMBER COUNT : {count}")
    print(f"PROCESS ID : {os.getpid()}")


def main():
    data = [1000000,2000000,3000000,4000000]
    pobj = multiprocessing.Pool()

    Result = pobj.map(Odd_Count,data)
    pobj.close()
    pobj.join()
    print(f"COUNT OF THE ODD NUMBERS : {Result}")

if __name__ == "__main__":
    main()

