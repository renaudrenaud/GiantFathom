import time
import RPi.GPIO as GPIO

relay_ch = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_ch, GPIO.OUT)

while True:
    time.sleep(1)
    GPIO.output(relay_ch, GPIO.LOW)
    print("Magnet off")
    time.sleep(1)
    GPIO.output(relay_ch, GPIO.HIGH)
    print("Magnet on")
