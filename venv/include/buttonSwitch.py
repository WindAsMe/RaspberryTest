# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-24 下午3:02
# File     :buttonSwitch.py
# Location:/Home/PycharmProjects/..
import RPi.GPIO as GPIO
import time

# Pin Definition
ledPin = 7
butPin = 12

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Running")

GPIO.output(ledPin, True)
try:
    while True:
        if GPIO.input(butPin):
            # button is released
            GPIO.output(ledPin, False)
        else:
            # button is pressed
            GPIO.output(ledPin, True)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Terminal!")
