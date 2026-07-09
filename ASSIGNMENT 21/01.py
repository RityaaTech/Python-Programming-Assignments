import threading

def Is_Prime(n):
    if (n<2):
        return False
    for i in range(2,int(n**0.5) + 1):
        if (n%i == 0):
            return False
    return True

def Prime(n):
    print("PRIME NUMBERS : ")
    for i in n:
        if Is_Prime(i):
            print(i,end = " ")

def Non_Prime(n):
    print("PRIME NUMBERS : ")
    for i in n:
        if not Is_Prime(i):
            print(i,end = " ")

def main():
    data = [1,2,3,4,5,6,7,8,9,10]

    T1 = threading.Thread(target=Prime,args=(data,))

    T2 = threading.Thread(target=Non_Prime,args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
