from turtle import *;from random import *;x=200;setup(x*3,x*2);bgcolor('black');color('navy');pu();ht();tracer(False);goto(-x,x);begin_fill();goto(x,x);goto(x,-x);goto(-x,-x);goto(-x,x);y=(x/2);[goto(-x,y-(z*(x/4))) or [fd(x/4) or circle(20) for _ in range(7)] and bk(350) for z in range(6)];goto(-x,-x);end_fill();del x,y
#   ^^^ Ignore ^^^

class Connect4: # <=== The Main Class / Root
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        
        self.gameboard = [['black' for z in range(7)] for z in range(6)]

        self.map = [[' ' for z in range(7)] for z in range(6)]

        # Uses self.map to create a matrix corresponding to self.gameboard
        sx = -150
        sy = 100
        for row in range(6):
            
            for col in range(7):
                self.map[row][col] = (sx,sy)

                sx += 50
            sx = -150
            sy -= 50
            
        del sx, sy
        
# This is an update method
# Would've been called that if it wasn't already reserved
    def remap(self):
        for row in range(6):
            for col in range(7):
                goto(self.map[row][col])
                color(self.gameboard[row][col])
                
                begin_fill()
                circle(20)
                end_fill()


                                        ###########
                                        # LEVEL 1 #
                                        ###########

class Player(Connect4):
    def __init__(self,psc,ort):
        self.psc = psc # - Player's Color
        self.ort = ort # - Player One or Player Two?
        
    def makemove(self,game,cords):
        row = cords[0]
        col = cords[1]
        game.gameboard[row][col] = self.psc

        
                                        ###########
                                        # LEVEL 2 #
                                        ###########

# Difference between HumanP and Player is that HumanP has preset colors
class HumanP(Player):
    def __init__(self,psc=None,ort=None):
        super().__init__(psc,ort)
        
        self.psc = 'red'
        self.ort = '1st'
        self.ir = False # - Is Robot?
        
# Same as HumanP and Player except with the addition of a difficulty variable
class RobotP(Player):
    def __init__(self,psc=None,ort=None,dif=None):
        self.dif = dif # - Difficulty
        super().__init__(psc,ort)
        
        self.psc = 'yellow'
        self.ort = '2nd'
        self.ir = True # - Is Robot?
        
                                        ###########
                                        # LEVEL 3 #
                                        ###########

class Handicap(HumanP):
    def makemove(self,r1,c1,r2,c2):
        super().__init__(map,psc)
        
        map[r1][c1] = psc
        map[r2][c2] = psc

#class EasyR(RobotP):
#class MediR(RobotP):
#class HardR(RobotP):


#   vvv Set up things below vvv

p1=HumanP()
p2=RobotP()
game = Connect4(p1,p2)


baf = 'back' # back and forth
ON = True

while ON:
    if baf == 'back':
        if p1.isRobot():
            p1.makemove(game,(randint(0,7),randint(0,6)))
        else:
            p1.makemove(game,tuple(input('Cords: ')))
        baf = 'forth
    elif baf == 'forth':
        if p1.isRobot():
            p1.makemove(game,(randint(0,7),randint(0,6))
        else:
            p1.makemove(game,tuple(input('Cords: ')))
        baf = 'back'
    game.remap()



