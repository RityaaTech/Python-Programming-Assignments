import threading

def Maximum(Data):
    print(f"MAXIMUM ELEMENT : {max(Data)}")

def Minimum(Data):
    print(f"MINIMUM ELEMENT : {min(Data)}")

def main():
    data = [1,2,3,4,5,6,7,8,9,10]

    T1 = threading.Thread(target=Maximum,args=(data,))

    T2 = threading.Thread(target=Minimum,args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
