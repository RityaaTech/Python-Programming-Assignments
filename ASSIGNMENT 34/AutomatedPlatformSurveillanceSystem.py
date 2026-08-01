import psutil        #install psutil
import sys
import os
import time 
import schedule

# Process Scanning Report
def ProcessScan():
    List_Process = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"]) #Convetr into Dictionary
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        List_Process.append(info)

    return List_Process

        
def Platform_Survellience(FolderName):
    Border = "="*50             #Design
    Ret = False

    Ret = os.path.exists(FolderName)

    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if (Ret == False):
            print("Unable to Proceed as Directory Name is existing but its not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory For logfile gets created successfully")

    #Timestamp Creation
    Timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    #Folder Store
    File_Name = os.path.join(FolderName,"Marvellous_%s.log" %{Timestamp})
    
    fobj = open(File_Name,"w")

    print(f"Logfile gets successfully created with name {File_Name}")

    fobj.write(Border+"\n")
    fobj.write("=== MARVELLOUS PLATFORM SURVELLIENCE SYSTEM ===\n")
    fobj.write(f"Log File gets created at : {Timestamp+"\n"}")
    fobj.write(Border+"\n\n")

    fobj.write("======== SYSTEM REPORT ==========\n")

    # CPU INFORAMTION
    fobj.write("Number of active CPU cores : %s %%\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM INFORMATION
    Memory = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" %Memory.percent)
    fobj.write("Total RAM Available : %s\n" %Memory.total)
    fobj.write(Border+"\n")

    # Network Usage
    Netobj = psutil.net_io_counters()  
    fobj.write("Network Usage Report\n")
    fobj.write("SENT : %.2f MB\n" %(Netobj.bytes_sent / (1024 * 1024)))
    fobj.write("RECEIVE : %.2f MB\n" %(Netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # ProcessLog
    Data = ProcessScan()
    for info in Data:
        fobj.write("PID : %s\n" % info.get("pid"))        
        fobj.write("Name : %s\n" % info.get("name"))
        fobj.write("User Name : %s\n" % info.get("username"))
        fobj.write("Status : %s\n" % info.get("status"))
        fobj.write("CPU Usage : %.2f\n" % info.get("cpu_percent"))
        fobj.write("RAM Usage : %.2f\n" % info.get("memory_percent"))

        fobj.write(Border+"\n")

            
    fobj.write("\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("======== END OF LOG FILE =========") 
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "="*50             #Design
    print(Border)
    print(" MARVELLOUS PLATFORM SURVELLIENCE SYSTEM ".center(50,"="))
    print(Border)

    # --h and --u handling
    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h" or sys.argv[1] =="--H"):
            print("This Automation script is used to perform")
            print("1 : It fetch the information of running process")
            print("2 : It fetch information about the primary storage as RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessor.")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file.")
            print("7 : It sends the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] =="--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of Folder for log file creation ")
        else:
            print("Unable to proceed as there is no matching arguement")
            print("Please use --h or --u flag for getting more details")

    # Actual Project Code
    elif (len(sys.argv) == 3):
        #print(f"CPU Usage : {psutil.cpu_percent()}")
        print("Scheduler Started Successfully")
        print("Press Ctrl + C to abort the Automation Script")
        schedule.every(int(sys.argv[1])).minutes.do(Platform_Survellience, sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    # Error Handling
    else:
        print("Invalid Number of Arguements")
        print("Unable to proceed as arguements are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print(" THANK YOU FOR USING OUR AUTOMATION SYSTEM ".center(50,"="))
    print(Border)

if __name__ == "__main__":
    main()