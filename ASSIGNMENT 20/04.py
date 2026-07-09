import threading

def SMALL(text):
    C = sum(1 for i in text if i.islower())
    print(f"THREAD ID : {threading.get_ident()}")
    print(f"THREAD NAME : {threading.current_thread().name}")
    print(f"LOWERCASE LETTER : {C}")
    
def CAPITAL(text):
    C = sum(1 for i in text if i.isupper())
    print(f"THREAD ID : {threading.get_ident()}")
    print(f"THREAD NAME : {threading.current_thread().name}")
    print(f"UPPERCASE LETTER : {C}")

def DIGITS(text):
    C = sum(1 for i in text if i.isdigit())
    print(f"THREAD ID : {threading.get_ident()}")
    print(f"THREAD NAME : {threading.current_thread().name}")
    print(f"DIGITS : {C}")

def main():
    text = input("ENTER THE STRING : ")

    T1 = threading.Thread(target=SMALL,args=(text,),name = "SMALL")

    T2 = threading.Thread(target=CAPITAL,args=(text,),name = "CAPITAL")

    T3 = threading.Thread(target=DIGITS,args=(text,),name = "DIGITS")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()