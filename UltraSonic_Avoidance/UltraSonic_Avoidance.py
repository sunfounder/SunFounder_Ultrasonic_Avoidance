#!/usr/bin/env python
'''
**********************************************************************
* Filename    : UltraSonic_Avoidance.py
* Description : A module for SunFounder UltraSonic Avoidance
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-26    New release
**********************************************************************
'''
import time
import RPi.GPIO as GPIO

class UltraSonic_Avoidance(object):
	def __init__(self, channel):
		self.channel = channel
		GPIO.setmode(GPIO.BCM)

	def get_distance(self):
		pulse_end = 0
		pulse_start = 0
		GPIO.setup(self.channel,GPIO.OUT)
		GPIO.output(self.channel, False)
		time.sleep(0.01)
		GPIO.output(self.channel, True)
		time.sleep(0.00001)
		GPIO.output(self.channel, False)
		GPIO.setup(self.channel,GPIO.IN)
		while GPIO.input(self.channel)==0:
			pulse_start = time.time()
		while GPIO.input(self.channel)==1:
			pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 100 * 343.0 /2
		distance = int(distance)
		
		return distance

if __name__ == '__main__':
	UA = UltraSonic_Avoidance(17)
	while True:
		print 'distance', UA.get_distance()
		#print 'distance', read_distance()
		time.sleep(0.5)