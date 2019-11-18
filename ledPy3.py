
from gpiozero import LED, MotionSensor
from gpiozero import PWMLED
from time import sleep
from signal import pause 

red = LED(18)
pir = MotionSensor(4)
score = 0
def count():
    red.on()
    score = score + 1
    return print("counting: ", score)
while True:
    pir.when_motion = red.on
    pir.when_motion = count
    sleep(2)
    red.off()
    if pir.when_motion:
        print("active fucker")
#if pir.when_motion:

#score = score + 1
    pir.when_no_motion = red.off


    pause()
