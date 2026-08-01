import schedule
import time
import shutil
import os
from datetime import datetime

source = input("Enter source file path: ")
destination = input("Enter destination folder path: ")

def backup():
    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    new_name = name + "_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ext
    dest_file = os.path.join(destination, new_name)

    shutil.copy(source, dest_file)

    with open("backup_log.txt", "a") as file:
        file.write("Backup completed successfully at " +
                   datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    print("Backup Completed Successfully")

schedule.every().hour.do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)