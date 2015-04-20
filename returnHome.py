
import RPi.GPIO as GPIO

def returnHome(motors):
	# need to just use serial GPIO location to move the motors
	# then back in main we can call pos.update(0,0,0) to update all that
	# bringing in the motors though we dont need to thread them, just individually move them X,Y,Z

	import configVars as Vars
	GPIO.setmode(GPIO.BCM)
	# GPIO.setup(motors[i].DIR, GPIO.OUT)
	# GPIO.setup(motors[i].STEP, GPIO.OUT)
	# GPIO.setup(Vars.stopper, GPIO.IN)
	# GPIO.setup(Vars.stopper, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)	
	GPIO.setup(Vars.stopper, GPIO.IN)
	switch = GPIO.input(Vars.stopper)				

	# just iterate through motors[] 0,1, for this #X and Y, Z will need custom work due to sensor!
	i = 0 #temp just running Y while x belt is tightened
	while i<2:
	
		GPIO.setup(motors[i].DIR, GPIO.OUT)
		GPIO.setup(motors[i].STEP, GPIO.OUT)

		while GPIO.input(13) == 1:
			print "switch equals  1"
			motors[i].simpleMove(1, 0) 	# moving 1mm at a time c-clockwise until we hit switch 
	
		while  GPIO.input(13) != 1:
			print "switch does not equals 1"
			motors[i].simpleMove(55, 1)	# gently moving off switch so it can be used for next motor
		i = i+1		
		print("zeroed out : ", motors[i].ID)
	GPIO.cleanup()
