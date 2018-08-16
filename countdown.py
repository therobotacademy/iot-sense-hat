#!/usr/bin/python
# https://codeclubprojects.org/en-GB/sense-hat/countdown-timer/
from sense_hat import SenseHat
sense = SenseHat()

import time

red= [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]

# Cuenta atras con caracteres
#for i in range (5,0,-1):
#    sense.show_letter(str(i),blue)
#    time.sleep(1)

# Cuenta atras con puntos de la matriz (7 segundos + 3 de parpadeo)
s =7

# Creamos una lista de 64 puntos negros
timer= []
for i in range(64):
    timer.append(black)
# Ahora se van a#adiendo 1 punto por cada segundo
for i in range(0,s):
    time.sleep(1)
    timer[i] = red
    sense.set_pixels(timer)

# Al completar la cuenta ponemos la matriz en azul
# Y parpadeando negro-azul- ...
for i in range(64):
    timer[i] = blue

# Y parpadeamos 3 veces (3 segundos)
for i in range(3):
    sense.clear()
    time.sleep(0.5)
    sense.set_pixels(timer)
    time.sleep(0.5)

# Acabamos dejando la matriz apagada
sense.clear()
