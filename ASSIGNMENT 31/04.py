import sys
import os
import time
import schedule
from datetime import datetime

def Directory_Scanner(Directory_Path = "Marvellous"):
    Border = "="*40
    
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
    for FolderName , SubFolder , FileName in os.walk(Directory_Path):
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

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used travel Directory")
            print("For better usage please check --u flag")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("PLease Execute script as ")
            print("python Filename.py DirectoryName")
            print("Directory Name should be absolute path.")
        else:
            #Directory_Scanner(sys.argv[1])
            schedule.every(10).minute.do(Directory_Scanner,sys.argv[1])

            while(True):
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of Arguements")
        print("PLease use --h or --u for more information..")

    print(Border)
    print(" Thank You for using Marvellous Automation Script ".center(50,"="))
    print(Border)

if __name__ == "__main__":
    main()