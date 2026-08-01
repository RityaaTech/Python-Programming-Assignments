import schedule
from datetime import datetime
import time

def main():
    Now = datetime.now()
    print(f"CURRENT DATE AND TIME : {Now.strftime("%d - %m - %Y %I : %M : %S %p")}")
    schedule.every(1).minute.do(main)

    while (True) : 
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

