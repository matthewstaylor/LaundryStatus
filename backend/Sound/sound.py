import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from datetime import datetime
import requests

sound=27

GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)

reader=SimpleMFRC522()

def postLaundryData(laundryDone):
    now = datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    url = 'http://ec2-52-14-234-1.us-east-2.compute.amazonaws.com/laundry'
    if laundryDone:
        laundryStatus = "Laundry done!"
        laundryColor = "green"
    else:
        laundryStatus = "Laundry in progress!"
        laundryColor = "red"
    myobj = {
        'laundry_status': laundryStatus,
        'time_posted': now,
        'color': laundryColor
    }
    x = requests.post(url, json=myobj)
    print(x.text)


def callback(sound):
    now = datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    if GPIO.input(sound):
        print("Sound Detected! Assuming laundry is running! " + now)
        postLaundryData(False)
        time.sleep(10)
    else:
        print("Checking...")
        time.sleep(3)


GPIO.add_event_detect(sound, GPIO.FALLING, callback=callback)  # let us know when the pin goes HIGH or LOW

try:
    waitingList = []
    while True:
        if GPIO.input(sound)==0:
            print('sound')
            postLaundryData(False)
            waitingList.clear()
        else:
            print('waiting')
            waitingList.append(0)
            if len(waitingList) > 10:
                postLaundryData(True)
                waitingList.clear()
            time.sleep(5)
except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()  # resets all GPIO ports used by this program
finally:
    GPIO.cleanup()
