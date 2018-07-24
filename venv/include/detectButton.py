# !/usr/bin/python3
# -- coding: UTF-8 --
# Author   :WindAsMe
# Date     :18-7-24 下午12:49
# File     :detectButton.py
# Location:/Home/PycharmProjects/..
import Rpi.GPIO as GPIO
import time

# Pin Definition
butPin = 12

# Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_IP)

print("Running...")

try:
    while True:
        if GPIO.input(butPin):
            print("Released!")
        else:
            print("Pressed!")
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Terminal!")