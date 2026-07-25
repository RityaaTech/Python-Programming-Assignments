def main():
    File = input("ENTER THE FILE NAME : ")
    Word = input("ENTER THE WORD YOU WANT TO SEARCH : ")

    fobj = open(f"{File}","r")
    Data = fobj.read()

    if Word in Data:
        print(f"{Word} found in File")
    else:
        print(f"{Word} not found in File.")

    fobj.close()

if __name__ == "__main__":
    main()