import threading

def Even_List(data):
    even = [i for i in data if i%2==0]
    print(f"EVEN ELEMENTS : {even}")
    print(f"SUM : {sum(even)}")

def Odd_List(data):
    odd = [i for i in data if (i%2!=0)]
    print(f"ODD ELEMENTS : {odd}")
    print(f"SUM : {sum(odd)}")

def main():
    data = [1,2,3,4,5,6,7,8,9,10]
    new_data = list(map(int,data))

    T1 = threading.Thread(target=Even_List,args=(new_data,))
    T2 = threading.Thread(target=Odd_List,args=(new_data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()