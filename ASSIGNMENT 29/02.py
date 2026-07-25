def main():
    fobj = input("ENTER THE FILE : ")
    File = open(f"{fobj}","r")
    Data = File.read()
    print(Data)
    
if __name__ == "__main__":
    main()