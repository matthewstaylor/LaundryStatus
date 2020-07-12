import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader=SimpleMFRC522()

try:
	text=input('New data:')
	print('Place tag to write.')
	reader.write(text)
	print("Wrote tag.")
finally:
	GPIO.cleanup()