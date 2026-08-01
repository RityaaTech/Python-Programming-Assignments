import schedule
import time 
from datetime import datetime

def main():

    fobj = open("Marvellous.txt","a")
    fobj.write(f"Task Executed at {datetime.now().strftime("%d - %m - %Y  %I : %M:%S %p")},")
    print("Data Written Successfully")

    schedule.every(1).minutes.do(main)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


