import threading

def Display():
    for i in range(1,50,1):
     print(i)

def Reverse_Display():
    for i in range(50,0,-1):
       print(i)

def main():
   T1 = threading.Thread(target=Display)

   T2 = threading.Thread(target=Reverse_Display)

   T1.start()
   T1.join()

   T2.start()
   T2.join()


if __name__ == "__main__":
   main()