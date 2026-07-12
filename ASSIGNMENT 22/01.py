import multiprocessing

def SumSquare(N):
    sum = 0
    for i in range(1,N+1):
        sum = sum + i*i
    return sum

def main():
    data = [1000000,2000000,3000000,4000000]
    Result = []
    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,data)

    pobj.close()
    pobj.join()

    print(f"RESULT : {Result}")


if __name__ == "__main__":
    main()







