class Player:
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.x = []
        self.y = []
        self.win = None
    
    def choose(self, x, y):
        self.x.append(x)
        self.y.append(y)
    
    def result(self):
        if self.win == False:
            print("Player " + self.name + " loses!")
            print("Try your best next time!")
        elif self.win == True:
            print("Player " + self.name + " wins!")
            print("Congratulations!")
        else:
            return