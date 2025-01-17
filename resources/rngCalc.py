from random import randint
from resources.ballObj import ball

def spotRoll():
    return randint(1,3)

def roll():
    return randint(1,100)

# Serve algorithm
def calcRollServe(ball:ball, accuracy:int, spot:int):
    # Accuracy checkk
    if accuracy >= 50:
        print('Accurate serve!')
        ball.setRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:
            ball.setRoute(spot)
            print('Accurate serve!')
            return True 
        elif accuracyRoll <= accuracy * 3:# Chance the ball wont go where it goes
            accuracyRoll = roll()
            print('not the best hand placement...')
            if accuracyRoll <= 50: # Good r0ll 
                ball.setRoute(spot)
                print('but the ball goes where he wants it!')
                return True

        print('Oooh a bad touch...')
        return False
        

    
                