import time 
seconds = input("Enter the timer duration")

def countDown_timer(seconds):
    mins = int(seconds/60)
    secs = int(seconds%60)

    timer = f'{mins}:{secs}'
    print(timer)
    seconds -= 1
    print("Time up!")

countDown_timer(int(seconds))
