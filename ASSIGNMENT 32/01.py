import os 
import time 
from datetime import datetime

def main():
    while(True):
        now = datetime.now()

        File_Name = now.strftime("File_%d_%m_%Y_%H_%M_%S.txt")

        fobj = open(File_Name,"w")
        fobj.write(f"File Name : {File_Name}")
        fobj.write(f"Creation Date : {now.strftime("%d-%m-%Y")}")
        fobj.write(f"Creation Time : {now.strftime("%H:%M:%S")}")

        print(f"{File_Name} created successfully.")

        time.sleep(60)

if __name__ == "__main__":
    main()