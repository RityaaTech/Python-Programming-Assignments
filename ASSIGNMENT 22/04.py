import multiprocessing
import time


def Power_Calculations(N):
    sum = 0
    for i in range(1,N+1):
        sum = sum + i*i*i*i*i
    return sum


def main():
    Data = [1000000,2000000,3000000,4000000]
    start_time = time.perf_counter()
    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Power_Calculations,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"RESULT : {Result}")
    print(f"EXECUTION TIME : {end_time-start_time} SECONDS")



if __name__ == "__main__":
    main()






