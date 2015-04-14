
import RPi.GPIO as GPIO

def returnHome(motors):
	# need to just use serial GPIO location to move the motors
	# then back in main we can call pos.update(0,0,0) to update all that
	# bringing in the motors though we dont need to thread them, just individually move them X,Y,Z

	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(motor[i].DIR, GPIO.OUT)
	GPIO.setup(motor[i].STEP, GPIO.OUT)
	GPIO.setup(Vars.stopper, GPIO.IN)
	
	switch = GPIO.input(Vars.stopper)				

	# just iterate through motors[] 0,1,2 for this
	i = 0
	while i<3:
	
		GPIO.setup(motor[i].DIR, GPIO.OUT)
		GPIO.setup(motor[i].STEP, GPIO.OUT)

		while switch != 1:
			motors[i].simpleMove(1, 0) 	# moving 1mm at a time c-clockwise until we hit switch 
		while switch:
			motors[i].simpleMove(1, 1)	# gently moving off switch so it can be used for next motor
		i = i+1		
	
