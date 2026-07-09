import threading

def Even():
    print("FIRST 10 EVEN NUMBER : ",end = "\n")
    for i in range(2,21,2):
        print(f"{i}",end = "  ")
        

def Odd():
    print("FIRST 10 ODD NUMBERS",end = "\n")
    for i in range(1,20,2):
        print(f"{i}",end = "  ")

def main():
    
    T1 = threading.Thread(target=Even,name="Even")
    T2 = threading.Thread(target=Odd,name="Odd")

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()