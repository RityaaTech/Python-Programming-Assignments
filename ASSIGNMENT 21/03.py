import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter
    for i in range(1000):
        lock.acquire()
        counter = counter + 1
        lock.release()

def main():
    data = []
    for i in range(5):
        T = threading.Thread(target=Increment)
        data.append(T)
        T.start()

    for T in data:
        T.join()

    print(f"FINAL COUNTER VALUE : {counter}")

if __name__ == "__main__":
    main()
 