from gpiozero import LED, MotionSensor
from time import sleep
from signal import pause
import sys

red = LED(19)
#redPIR= MotionSensor(4)

class Game():
    def __init__(self, player1, player2, player3, player4, sio):
        self.score = { "red":0, "black": 0 }
        self.isOn = False
        self.sio = sio
        #self.red = LED(18)
        #self.redPir = MotionSensor(4)
        self.redTeam = {"redD": player1, "redO": player2 }
        self.blackTeam = {"blackD": player3, "blackO":player4}

    def get_teams(self):
        return self.redTeam, self.blackTeam

    def redgoal(self, x):
        self.score = {"red":self.score.get("red") + 1, "black": self.score.get("black")}
        # self.score = {"red" : self.score["red"] + 1, "black" : self.score["red"]}
        print("we have made it this far")
        red.on()
        sleep(2)
        red.off()
        if self.score.get("red") == 100:
            self.gameOver()
            return
        print("Red: ", self.score.get("red"), " Black: ", self.score.get("black"))
        #TODO: this is where the errors coming from \/
        return
        
        
    def gameOver(self):
        winner = self.getWinner(self)
        print("Red: ", self.score.get("red"), " Black: ", self.score.get("black"))
        print("Your winner is ", winner, " !")
        self.isOn = False
        
        playAgain = input("Play again? y/n")
        if playAgain == "y":
            self.resetScore(self)
            self.swapPositions(self)
        else:
            sys.exit()
        
    def resetScore(self, score):
        self.score =  { "red":0, "black": 0 }
        
    def getWinner(self, score):
        if self.score.get("red") > self.score.get("black"):
            return "Red"
        else:
            return "Black"
        return "Tie"
    
    def swapPositions(self, redTeam):
        playerA = self.redTeam.get("redD")
        playerB = self.redTeam.get("redO")
        print("Teams are ", self.redTeam)
        self.redTeam = {"redD":playerB, "redO": playerA}
        print("Teams are ", self.redTeam)
