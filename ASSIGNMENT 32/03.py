import os 
import time
from datetime import datetime

def main():
    File_Path = input("ENTER THE FILE PATH : ")

    while(True):
        try:
            if not os.path.exists(File_Path):
                print("File does not exist")
            elif os.path.getsize(File_Path) == 0:
                print("File is Empty.")
            else:
                fobj = open(File_Path,"r")
                print("\nFILE CONTENT : ")
                print(fobj.read())
                fobj.close()

        except PermissionError:
            print("Permission Denied")

        except OSError:
            print("File cannot be opened.")

        time.sleep(60) 

if __name__ == "__main__":
    main()