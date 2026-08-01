import os
import time 
from datetime import datetime

def main():
    print(" AUTOMATION SCRIPT STARTED ".center(50,"="))
    File_Path = input("ENTER THE FILE PATH : ")

    while(True):
        log = open("FileSizeLog.txt","a")
        if (os.path.exists(File_Path)):
            size = os.path.getsize(File_Path)

            log.write(f"FILE PATH : {File_Path}\n")
            log.write(f"FILE SIZE : {size} BYTES\n")
            log.write(f"DATE AND TIME : {datetime.now()}\n")
            log.write(f" THANK YOU FOR USING AUTOMATION SCRIPT ".center(50,"="))

            print(" INFORMATIO STORED.. ".center(50,"="))

        else:
            print("FILE DOES NOT EXIST...")

        time.sleep(30)

if __name__ == "__main__":
    main()