import os 
import time 
import schedule
from datetime import datetime

def Scan_Directory(Folder):
    if not os.path.exists(Folder):
        print("Directory Not found.")
        return 

    files = 0
    folders = 0

    for item in os.listdir(Folder):
        path = os.path.join(Folder,item)

        if (os.path.isfile(path)):
            files = files + 1
        elif (os.path.isdir(path)):
            folders = folders + 1

    print(f"\nDirectory Scanned : {Folder}")
    print(f"Total Files : {files}")
    print(f"Total Subdirectories : {folders}")
    print(f"Scan Time : {datetime.now().strftime("%d-%m-%Y  %I : %M : %S %p ")}")

def main():
    schedule.every(1).minutes.do(Scan_Directory,31)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()