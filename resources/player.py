from random import randint
from ballObj import ball

roll = randint(1, 100)




class player():
    def __init__(self, name, accuracy):
        self.name = name 
        self.accuracy = accuracy
    
    def hit(self, ball:ball):
        if self.accuracy - ball.attributes['difficulty'] > 50:
            currentRoll = roll + self.accuracy // 10 
            if currentRoll > 30:# Hit goes where user wanted
                print('successful hit')
                return 'successs'
            else:# not the best hit A
                print('hit off')
                
                if currentRoll < 20:# Hit is a comlete miss
                    print('complete miss')
                else:
                    print('half decent hit')
    
    def receive(self, ball:ball):
        if self.accuracy - ball.attributes['difficulty'] > 50:
            currentRoll = roll + self.accuracy // 10 
            if currentRoll > 30:# Hit goes where user wanted
                print('successful receive')
                return 'successs'
            else:# not the best hit 
                print('receieve off')
                
                if currentRoll < 20:# Hit is a comlete miss
                    print('complete miss')
                else:
                    print('half decent receieve')
    
    def __str__(self):
        return self.name
