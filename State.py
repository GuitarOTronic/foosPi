from gpiozero import LED, MotionSensor
from gpiozero import PWMLED
from time import sleep
from signal import pause 



class Foos:
    def __init__(self):
        self.game = Game("Sean", "Lauren", "Murderface", "Mitch")

    def redGoal(self):
       self.game.goal("red")
       red.on()

    def resetGame(self, game):
        #TODO: turn these into Players
        self.game = Game( "Sean", "Lauren", "Murderface", "Mitch")


class Game(Foos):
    def __init__(self, player1, player2, player3, player4):
        self.score = { "red":0, "black": 0 }
        self.redTeam = {"redD": player1, "redO": player2 }
        self.blackTeam = {"blackD": player3, "blackO":player4}

    def get_teams(self):
        return self.redTeam, self.blackTeam

    def goal(self, team):
        self.score[team]=self.score[team] + 1
        if self.score[team] == 2:
            self.gameOver()
        print("Red: ", self.score.get("red"), " Black: ", self.score.get("black"))
    
    def gameOver(self):
        winner = self.getWinner(self)
        print("Your winner is ", winner, " !")
        super().resetGame(Foos)
        #self.resetScore(self)

    def getWinner(self, score):
        if self.score.get("red") > self.score.get("black"):
            return "Red"
        else:
            return "Black"

    #def resetScore(self, score):
     #self.score = { "red": 0, "black": 0}

    


red = LED(18)
redPIR = MotionSensor(4)

game = Foos()
   
while True:
    redPIR.when_motion = game.redGoal
    sleep(2)
    #red.off()
    redPIR.when_no_motion = red.off
   # pause()
