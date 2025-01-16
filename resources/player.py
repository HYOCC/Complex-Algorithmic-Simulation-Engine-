from random import randint
from resources.ballObj import ball

roll = randint(1, 100)

class player():
    def __init__(self, name, accuracy):
        self.name = name 
        self.accuracy = accuracy
    
    def hit(self, ball:ball):
        # Accuracy around 50 or higher
        if self.accuracy - ball.attributes['difficulty'] > 50:
            currentRoll = roll + (self.accuracy // 10) 
            if currentRoll > 30:# Hit goes where user wanted
                print('successful hit')
                ball.increaseDifficulty(5)
                return 'successs'
            else:# not the best hit A
                print('hit off')
                if currentRoll < 20:# Hit is a comlete miss
                    print('complete miss')
                else:
                    print('half decent hit')
                    ball.increaseDifficulty(2)# updates ball difficulty

        # accuracy stat is around 30
        elif self.accuracy - ball.attributes['difficulty'] > 30:
            currentRoll = roll + (self.accuracy // 10)
            if currentRoll > 60:# Hit goes where user wanted
                print('successful hit')
                ball.increaseDifficulty(5)
                return 'successs'
            else:# not the best hit A
                print('hit off')

                if currentRoll < 30:# Hit is a comlete miss
                    print('complete miss')
                else:
                    print('half decent hit')
                    ball.increaseDifficulty(2)
    
    def receive(self, ball:ball):
        if self.accuracy - ball.attributes['difficulty'] > 50:
            currentRoll = roll + self.accuracy // 10 - ball.state['diffculty']
            if currentRoll > 30:# Hit goes where user wanted
                print('successful receive')
                ball.attributes['difficulty'] = 0
                return 'successs'
            else:# not the best hit 
                print('receieve off')
                
                if currentRoll < 20:# Hit is a comlete miss
                    print('complete miss')
                    ball.increaseDifficulty(2)
                else:
                    print('half decent receieve')
                    ball.decreaseDifficulty(2)
                    
        # accuracy stat is around 30
        elif self.accuracy - ball.attributes['difficulty'] > 30:
            currentRoll = roll + self.accuracy // 10
            if currentRoll > 60:
                print('successful receive')
                ball.attributes['difficulty'] = 0
                return 'successs'
            else:# not the best hit A
                print('receive off')
                
                if currentRoll < 30:# Hit is a comlete miss
                    print('complete miss')
                    ball.increaseDifficulty(2)
                else:
                    print('half decent receive')
                    ball.decreaseDifficulty(2)
        else:
            print('lost the point')
    
    def __str__(self):
        return self.name
