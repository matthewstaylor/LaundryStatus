import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader=SimpleMFRC522()
GPIO.setup(11, GPIO.OUT, initial=0)

try:
	id, text=reader.read()
	if (id == 4328719364):
		print("Successfully read your phone.")
		GPIO.output(11,1) # green LED
		time.sleep(3) #Leave LED on 3 seconds
	print(id)
	print(text)
finally:
	GPIO.cleanup()