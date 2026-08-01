import os
import shutil
import time

src = input("Enter Source Directory: ")
dest = input("Enter Destination Directory: ")

while True:

    if not os.path.isdir(src):
        print("Invalid Source Directory")
        break

    if not os.path.isdir(dest):
        print("Invalid Destination Directory")
        break

    logfile = open("CopyLog.txt", "a")

    for file in os.listdir(src):

        if file.endswith(".txt"):
            sourcefile = os.path.join(src, file)
            destfile = os.path.join(dest, file)

            try:
                shutil.copy2(sourcefile, destfile)
                logfile.write(file + " copied successfully\n")
                print(file, "Copied")

            except Exception:
                logfile.write(file + " could not be copied\n")

    logfile.close()

    time.sleep(600)