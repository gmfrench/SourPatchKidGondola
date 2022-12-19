import RPi.GPIO as GPIO
import StepperClass
import math
from threading import Thread
from time import sleep, time
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

### clear things up from previous runs  
GPIO.cleanup()
###

factory = PiGPIOFactory()

servo = Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
arm = Servo(24, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo.value = None
arm.value = None

step = StepperClass.Stepper()

# 1. rowing motion of the boat
## stepper - slow, continuous revolution
def rowingMotion(numRevs = 1, CW = True):
    while True:
        step.revolveFull(numRevs, CW)
        sleep(0.1)

# 2. rocking motion of the boat
## servo - steady oscillation with an arc of about 30 degrees
def rockingMotion():

    while True:
        #rotate right
        for i in range(0, 20):
                servo.value = math.sin(math.radians(i))
                sleep(0.04)
        #rotate left
        for i in reversed(range(0, 20)):
                servo.value = math.sin(math.radians(i))
                sleep(0.04)

# 3. motion of the arm
## servo - steady oscillation with an arc of about 30 degrees
def armMotion():    
    while True:
        while True:
            for i in range(0, 20):
                arm.value = math.sin(math.radians(i))
                sleep(0.06)


# 4. combine motion
## servo & stepper - simplifies the motion for demonstration purposes
def combo():
    while True:
        for i in range(0, 20):
                servo.value = math.sin(math.radians(i))
                sleep(0.04)
        sleep(0.2)
        step.revolveFull(1,True)
        sleep(0.2)
        for i in reversed(range(0, 20)):
                servo.value = math.sin(math.radians(i))
                sleep(0.04)
        step.revolveFull(2,True)
        sleep(0.2)
        servo.value = None
        arm.value = None
        
# we want 3. and 4. to occur simulatneously, so we need to
# start them as separate threads
t1 = Thread(target=armMotion)
threads = [t1] #allow for more threads to be added later
t2 = Thread(target=combo)
threads += [t2]

for tloop in threads:
    tloop.daemon = True
    tloop.start()

for tloop in threads:
    tloop.join()