import os 

def main():
    File = input("ENTER THE FILE : ")
    if (os.path.exists(File)):
        print(f"{File} : File Exists")
    else:
        print(f"{File} : Not Exists")

if __name__ == "__main__":
    main()