import sys
import os
import time
import schedule
from datetime import datetime

def Count_Files(Folder):
    Border = "="*40

    if not os.path.exists(Folder):
        print("Directory Not Found")
        return

    count = 0

    for item in os.listdir(Folder):
        path = os.path.join(Folder,item)

        if os.path.isfile(path):
            count = count + 1
    
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    print(f"Log File gets created with File Name : {LogFileName}")                  
    fobj = open(LogFileName,"w")
    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Border+"\n\n")
    
    print("Files from the Directory : ")
    fobj.write(Border+"\n\n")
    for FolderName , SubFolder , FileName in os.walk(Folder):
        for fname in FileName:
            fobj.write(fname+"\n")

            
    fobj.write(Border+"\n")
    fobj.write(f"LogFile gets created at : {timestamp}")
    fobj.write(f"CREATION TIME : {datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}")
    fobj.write("\n"+Border+"\n")
           
    fobj.close()

def main():
    Border = "="*40
    print(Border)
    print(" Marvellous Automation Script ".center(50,"="))
    print(Border)

    
    schedule.every(1).minute.do(Count_Files,"PYTHON ASSIGNMENTS")

    while(True):
        schedule.run_pending()
        time.sleep(1)

    

if __name__ == "__main__":
    main()