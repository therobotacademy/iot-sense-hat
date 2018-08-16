#!/usr/bin/python
import time
from sense_hat import SenseHat
sense = SenseHat()
X = [255, 0, 0] # Red
o = [0, 0, 150] # Blue

question_mark = [
o, o, o, X, X, o, o, o,
o, o, X, o, o, X, o, o,
o, o, o, o, o, X, o, o,
o, o, o, o, X, o, o, o,
o, o, o, X, o, o, o, o,
o, o, o, X, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, X, o, o, o, o
]
sense.set_pixels(question_mark)
time.sleep(2)
sense.clear()
