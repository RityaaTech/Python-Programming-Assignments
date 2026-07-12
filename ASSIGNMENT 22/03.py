import multiprocessing
import math

def Count_Prime(N):
    count = 0
    
    for N in range(2,int(N+1)):
        prime = True 
        for i in range(2,int(math.sqrt(N) + 1)):
            if (N%i == 0):
                prime = False
                break
        
        if prime:
            count = count + 1

        return count
    
def main():
    Data = [10000,20000,30000,40000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(Count_Prime,Data)
    
    pobj.close()
    pobj.join()

    print(f"RESULT : {Result}")


if __name__ == "__main__":
    main()
