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

	def get_distance(self, Ranges=500):
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

		if pulse_start != 0 and pulse_end != 0:
			pulse_duration = pulse_end - pulse_start
			distance = pulse_duration * 100 * 343.0 /2
			distance = int(distance)
			
			if distance <= Ranges:
				#print 'start = %s'%pulse_start,
				#print 'end = %s'%pulse_end

				return distance

if __name__ == '__main__':
	UA = UltraSonic_Avoidance(17)
	while True:
		distance = UA.get_distance()
		if distance >= 0:
			print 'distance', distance, 'cm'
			time.sleep(0.2)
		elif distance == None:
			print False