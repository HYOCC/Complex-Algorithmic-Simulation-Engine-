from random import randint
from resources.ballObj import ball


def roll():
    return randint(1,100)

def calculateRoll(ball:ball, action:str, accuracyStat:int):
    if action == 'hit':# Hit action
        currentRoll = roll()
        print(f'rolled {currentRoll}')
        if currentRoll <= accuracyStat - ball.getDifficulty():# Successful hit 
            print('Accurate hit')
            ball.increaseDifficulty(10)
            return True
        elif currentRoll <= accuracyStat + ((100 - accuracyStat) % 10):
            print('Almost accurate hit')
            ball.increaseDifficulty(8)
            return True
        elif currentRoll <= accuracyStat + 2 * ((100 - accuracyStat) % 10):
            print('half accurate hit')
            ball.increaseDifficulty(5)
            return True
        elif currentRoll <= accuracyStat + 3 * ((100 - accuracyStat) % 10):
            print('weak hit')
            ball.increaseDifficulty(1)
            return True
        else:# Complete miss
            print('missed')
            return False
    
    elif action == 'receive':
        currentRoll = roll()
        print(f'rolled {currentRoll}')
        if currentRoll <= accuracyStat - ball.getDifficulty():# Successful hit 
            print('Accurate receive')
            ball.decreaseDifficulty(10)
            return True
        elif currentRoll <= accuracyStat + ((100 - accuracyStat) % 10):
            print('Almost accurate hit')
            ball.decreaseDifficulty(8)
            return True
        elif currentRoll <= accuracyStat + 2 * ((100 - accuracyStat) % 10):
            print('half accurate hit')
            ball.decreaseDifficulty(5)
            return True
        elif currentRoll <= accuracyStat + 3 * ((100 - accuracyStat) % 10):
            print('weak hit')
            ball.decreaseDifficulty(1)
            return True
        else:# Complete miss
            print('missed')
            return False
            
                   
        
            

class player():
    def __init__(self, name, accuracy):
        self.name = name 
        self.accuracy = accuracy
    
    def hit(self, ball:ball):
        return calculateRoll(ball, 'hit', self.accuracy)
    
    def receive(self, ball:ball):
        return calculateRoll(ball, 'receive', self.accuracy)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()