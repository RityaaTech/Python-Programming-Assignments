import os
import time

folder = input("Enter Directory Path: ")

while True:

    logfile = open("DeleteLog.txt", "a")

    for path, dirs, files in os.walk(folder):

        for file in files:

            filename = os.path.join(path, file)

            try:
                if os.path.getsize(filename) == 0:
                    os.remove(filename)
                    logfile.write(filename + "\n")
                    print(filename, "Deleted")

            except PermissionError:
                print("Permission Denied:", filename)

    logfile.close()

    time.sleep(3600)