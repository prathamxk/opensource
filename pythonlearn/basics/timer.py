from datetime import datetime
import time
import winsound
from winsound import Beep
import lockscreen

timercount = input("Enter how long you want timer in minutes from 1 to 59: ")
timercountsec = int(timercount) * 60
while timercountsec > 0:
    time.sleep(1)
    print(timercountsec)
    timercountsec-=1

frequency = 2000

duration = 1200

winsound.Beep(frequency, duration)
time.sleep(1)
winsound.Beep(1500 , duration)
time.sleep(1)
winsound.Beep(1800 , duration)

lockscreen.timeIsUp()

print("Alarm clock worked.")
