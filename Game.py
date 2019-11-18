class Game:
    def __init__(self, player1, player2, player3, player4):
        self.score = { "red":0, "black": 0 }
        self.redTeam = {"redD": player1, "redO": player2 }
        self.blackTeam = {"blackD": player3, "blackO":player4}

    def goal(self, team):
        self.score[team]=self.score[team] + 1
        if self.score[team] == 5:
            self.gameOver()
        print("Red: ", self.score.get("red"), " Black: ", self.score.get("black"))
    
    def gameOver(self):
        winner = self.getWinner(self)
        print("Your winner is ", winner, " !")
        self.resetScore(self)

    def getWinner(self, score):
        if self.score.get("red") > self.score.get("black"):
            return "Red"
        else:
            return "Black"

    def resetScore(self, score):
        self.score = { "red": 0, "black": 0}


