#!/usr/bin/evn python
import RPi.GPIO as GPIO
import time
pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

for _ in xrange(10):
	print 'led on'
	GPIO.output(pin,True)
	time.sleep(0.5)

	print 'led off'
	GPIO.output(pin,False)
	time.sleep(0.5)

GPIO.cleanup()
print 'clean up'
print 'bye'
