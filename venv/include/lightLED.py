# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-24 上午11:22
# File     :lightLED.py
# Location:/Home/PycharmProjects/..
import RPi.GPIO as GPIO
import time

# Pin Definitions
ledPin = 7

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

print("Program running...")

ledStatus = True
GPIO.output(ledPin, ledStatus)

try:
    while True:
        time.sleep(1)
        ledStatus = not ledStatus
        GPIO.output(ledPin, ledStatus)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Terminal.")
