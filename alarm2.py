from datetime import datetime
import time
import winsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\nWake Up!")
        winsound.Beep(1000, 5000)  # Frequency = 1000 Hz, Duration = 5 sec
        break

    time.sleep(1)
    
"""
    first install playsound:

pip install playsound==1.2.2

Then:

from datetime import datetime
import time
from playsound import playsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current = datetime.now().strftime("%H:%M:%S")

    if current == alarm_time:
        print("Wake Up!")
        playsound("alarm.mp3")   # Put alarm.mp3 in the same folder
        break

    time.sleep(1)
How It Works

Suppose the current time is:

07:29:58
07:29:59
07:30:00

When both strings match:

if current == alarm_time:

the alarm is triggered.
"""
