import threading

def SUM(data):
    sum = 0
    for i in data :
        sum = sum + i
    return sum

def PRODUCT(data):
    product = 1
    for i in data:
        product = product * i
    return product

def main():
    data = [1,2,3,4,5,6,7,8,9,10]
    T1 = threading.Thread(target=SUM,args=(data,))

    T2 = threading.Thread(target=PRODUCT,args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    

if __name__ == "__main__":
    main()
