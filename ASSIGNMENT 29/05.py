def main():
    File = input("ENTER THE FILE NAME : ")
    Word = input("ENTER THE WORD : ")

    fobj = open(File,"r")
    Data = fobj.read()
    fobj.close()

    count = Data.count(Word)

    print(f"Frequency of {Word} is {count}")

if __name__ == "__main__":
    main()