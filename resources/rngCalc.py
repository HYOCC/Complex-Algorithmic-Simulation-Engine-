from random import randint
from resources.ballObj import ball

def spotRoll():
    return randint(1,3)

def roll():
    return randint(1,100)

# Serve algorithm
def calcRollServe(ball:ball, accuracy:int, spot:int):
    ball.stateUpdate('served')
    
    # Accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate serve!')
        ball.setRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.setRoute(spot)
            print('Accurate serve!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best hand placement...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.setRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad touch...')
        return False
        
# receive algorithm
def calcRollReceive(ball:ball, accuracy:int, spot:int):
    ball.stateUpdate('received')
    
    # Accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate receive!')
        ball.setRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.setRoute(spot)
            print('Accurate receive!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best recieve...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.setRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad recieve and the ball goes out...')
        return False
                