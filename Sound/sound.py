import RPi.GPIO as GPIO
import time

channel=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def function(channel):
    if GPIO.input(channel):
        print ("Washer/Dryer running")
    else:
        print("Checking if laundry done...")
        for i in range(0,5):

        time.sleep(15)
        if (GPIO.input(channel)):
                print("Not done.")
        else:
                print("Laundry done!")

GPIO.add_event_detect(channel, GPIO.RISING, callback=function)

while True:
    time.sleep(5)