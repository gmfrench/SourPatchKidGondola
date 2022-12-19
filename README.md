# SourPatchKidGondola
Code for PHYS351 final project
Author:        G. French
Collaborators: A. McNally, A. Ringberg
Last edited:  12/19/2022

PINOUT
 - servo (turning)
        PWM pin 23
 - servo (arm)
        PWM pin 24
 - stepper (motor controller)
        PWM pins 17, 18, 27, 22

CODE
 The body of the code is contained within the file 'main.py' which calls external files that contain functions of their own. The code, once started, runs continuously using independent functions for rowing and rocking motions (see 'main.py' for their definitions).
