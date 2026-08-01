import schedule
import time
import datetime

def Greet():
    print("Namaskar...")

def main():
    print(" AUTOMATION SCRIPT STARTED ".center(50,"="))

    schedule.every().day.at("9:00").do(Greet)

    while(True):
        schedule.run_pending()
        time.sleep(1)