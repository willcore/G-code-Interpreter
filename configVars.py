__author__ = 'William'

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

from printHead import PrintHead

milimeterMode = True

dummySTEP = 20
dummyDIR = 21

xSTEP = 20
xDIR = 21

ySTEP = 12 
yDIR = 16

zSTEP = 19 
zDIR = 26

eSTEP =5 
eDIR = 6

xStopper = 13 
yStopper = 6


filamentDiameter = 0.0

feedrate = 0.0

temperature = 0.0

fanRate = 0.0


