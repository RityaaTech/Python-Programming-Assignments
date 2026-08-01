import schedule
import time

def Display_Message(Message):
    print(f"Message : {Message}")


def main():
    seconds = int(input("ENTER THE TIME INTERVAL IN SECONDS : "))
    
    if (seconds <= 0):
            print("Interval must be greater than zero..")
            exit()

    schedule.every(seconds).seconds.do(Display_Message,"Jay Ganesh ...")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()




