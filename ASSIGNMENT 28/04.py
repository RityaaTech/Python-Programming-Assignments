def main():
    fobj_1 = open("Demo.txt","r")
    Data = fobj_1.read()
    fobj_1.close()

    fobj_2 = open("NewDemo.txt","w")
    fobj_2.write(Data)
    fobj_2.close()

    print("Content Copied Successfully.")

if __name__ == "__main__":
    main()