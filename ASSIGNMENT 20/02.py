import threading

def Even_Factor(n):
    sum = 0
    for i in range(1,n+1):
        if (n%i == 0 and i%2==0):
            print(i)
            sum = sum + i
    print(f"SUM OF THE EVEN FACTORS : {sum}")

def Odd_Factor(n):
    sum = 0
    for i in range(1,n+1):
        if (n%i==0 and i%2!=0):
            print(i)
            sum = sum + i
    print(f"SUM OF THE ODD FACTORS : {sum}")

def main():
    n = int(input("ENTER THE NUMBER : "))

    T1 = threading.Thread(target=Even_Factor,args=(n,))
    T2 = threading.Thread(target=Odd_Factor,args=(n,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
    