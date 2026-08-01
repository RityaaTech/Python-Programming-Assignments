import schedule
import time 
import datetime

def Lunch():
    print("Lunch Time!")

def Wrap_Up():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(Lunch)

    schedule.every().day.at("18:00").do(Wrap_Up)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()