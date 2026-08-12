from datetime import datetime
import time
from playsound import playsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")
print("Alarm set for:", alarm_time)

while True:
    current = datetime.now().strftime("%H:%M:%S")
    print(current, end="\r")

    if current == alarm_time:
        print("\nWake Up!")
        playsound("alarm.mp3")   # Make sure alarm.mp3 is in the same folder
        break

    time.sleep(1)

input("Press Enter to exit...")