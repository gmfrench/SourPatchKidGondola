### StepperClass.py ###
import RPi.GPIO as GPIO
from time import sleep
from time import time

# assigning the GPIO pins
out1 = 17
out2 = 18
out3 = 27
out4 = 22

# important values to running the stepper
step_sleep = 0.005
step_count = 200
        
class Stepper:
    def __init__(self): 
        # setting up
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( out1, GPIO.OUT ) #A1
        GPIO.setup( out2, GPIO.OUT ) #A2
        GPIO.setup( out3, GPIO.OUT ) #B1
        GPIO.setup( out4, GPIO.OUT ) #B2
 
        # initializing
        GPIO.output( out1, GPIO.LOW )
        GPIO.output( out2, GPIO.LOW )
        GPIO.output( out3, GPIO.LOW )
        GPIO.output( out4, GPIO.LOW )

    # Reset all the pins
    def cleanup(self):
        GPIO.output( out1, GPIO.LOW )
        GPIO.output( out2, GPIO.LOW )
        GPIO.output( out3, GPIO.LOW )
        GPIO.output( out4, GPIO.LOW )
        GPIO.cleanup()
    
    # completes a given number of full-step CW (CCW) revs
    def revolveFull(self, numberOfRevs, CW = True):
        if CW:
            step_list = range(int(numberOfRevs*step_count))
        else:
            step_list = reversed(range(int(numberOfRevs*step_count)))

        for i in step_list:
            if i%4==0:
                GPIO.output( out4, GPIO.HIGH )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.HIGH )
            elif i%4==1:
                GPIO.output( out4, GPIO.HIGH )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.HIGH )
                GPIO.output( out1, GPIO.LOW )
            elif i%4==2:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.HIGH )
                GPIO.output( out2, GPIO.HIGH )
                GPIO.output( out1, GPIO.LOW )
            elif i%4==3:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.HIGH )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.HIGH )

            sleep(step_sleep)

    # completes a given number of half-step CW (CCW) revs
    def revolveHalf(self, numberOfRevs, CW = True):
        if CW:
            step_list = range(int(numberOfRevs*step_count*2))
        else:
            step_list = reversed(range(int(numberOfRevs*step_count*2)))
            
        for i in step_list:
            if i%8==0:
                GPIO.output( out4, GPIO.HIGH )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.HIGH )
            elif i%8==1:
                GPIO.output( out4, GPIO.HIGH )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.LOW )
            elif i%8==2:
                GPIO.output( out4, GPIO.HIGH )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.HIGH )
                GPIO.output( out1, GPIO.LOW )
            elif i%8==3:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.HIGH )
                GPIO.output( out1, GPIO.LOW )
            elif i%8==4:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.HIGH )
                GPIO.output( out2, GPIO.HIGH )
                GPIO.output( out1, GPIO.LOW )
            elif i%8==5:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.HIGH )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.LOW )
            elif i%8==6:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.HIGH )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.HIGH )
            elif i%8==7:
                GPIO.output( out4, GPIO.LOW )
                GPIO.output( out3, GPIO.LOW )
                GPIO.output( out2, GPIO.LOW )
                GPIO.output( out1, GPIO.HIGH )

            sleep(step_sleep/2)
