import multiprocessing
import os
import time


def Factorial(N):
    print(f"PID OF FACTORIAL : {os.getpid()}")
    fact = 1
    for i in range(1,N+1):
        fact = fact * i
    return fact

def main():
    print(f"PID OF THE MAIN : {os.getpid()}")
    data = [10,15,20,25]
    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial,data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"RESULT : {Result}")
    print(f"TIME REQUIRED : {end_time - start_time:.4f} SECONDS")


if __name__ == "__main__":
    main()


