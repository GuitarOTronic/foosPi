from gpiozero import LED, MotionSensor
from gpiozero import PWMLED
from time import sleep
from signal import pause 

import Game

class Foos

game = Game.Game( "Sean", "Lauren", "Murderface", "Mitch")
game.goal("red")
red = LED(18)
pir = MotionSensor(4)
score = 0

def count():
   game.goal("red")
   red.on()
   
while True:
    pir.when_motion = count
    sleep(2)
    pir.when_no_motion = red.off


   # pause()
