from Queue import Queue
import RotaryEncoder
from time import sleep
from sys import exit

A_PIN  = 17 #wiring=0 A pin on rotary
B_PIN  = 27 #wiring=2 B pin on rotary 
SW_PIN = 22 #wiring=3 press pin on rotary


RotQueue = Queue()                                                              # define global que for events
encoder = RotaryEncoder.RotaryEncoderWorker(A_PIN, B_PIN, SW_PIN, RotQueue)     # create a new rotary switch

import atexit
@atexit.register
def close_gpio():                                                               # close the gpio port at extit time
    encoder.Exit()

def process():
    
    while not(RotQueue.empty()):
        m=RotQueue.get_nowait()
        if m == RotaryEncoder.EventLeft:
            print "Detected one turn to the left"
            pass # add action for turning one to the left
        elif m == RotaryEncoder.EventRight:
            print "Detected one turn to the right"
            pass # add action for turning one to the left
        elif m == RotaryEncoder.EventDown:
            print "Detected press down"
            pass # add action for turning one to the left
        elif m == RotaryEncoder.EventUp:
            print "Detected release up"
            pass # add action for turning one to the left
            #exit()                   # uncomment to exit by "pressing the knob"
        RotQueue.task_done()
                    
if __name__ == "__main__":
    try:
        while(True):
            print "waiting 5s"
            sleep (5)  # here you can process on RPI whatever you want and operate the rotary knob it won't be missed
            process()  # and check what has happened with rotary
    except KeyboardInterrupt:
        print "broken by keyboard"             

        
    