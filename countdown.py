#!/usr/bin/python
# https://codeclubprojects.org/en-GB/sense-hat/countdown-timer/
from sense_hat import SenseHat
sense = SenseHat()

for i in range (1,6):
    sense.show_letter(str(i))
    sleep(1)
