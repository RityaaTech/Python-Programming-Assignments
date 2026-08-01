import schedule
import time

def Display_Message(Message):
    print(f"Message : {Message}")

def main():

    schedule.every(5).seconds.do(Display_Message,"Ganapati Bappa Moraya")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()