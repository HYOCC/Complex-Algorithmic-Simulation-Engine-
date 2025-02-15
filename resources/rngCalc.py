from random import randint
from resources.ballObj import ball

def spotRoll():
    return randint(1,3)

def roll():
    return randint(1,100)

########## Test

def testCalcRollServ(ball:ball, accuracy:int, strength:int, spot:dict):# spot: {'gSpot':int, 'sSpot':int}
    ball.stateUpdate('served')
    
    # Strength = velocity added to the ball
    ball.increaseVelocity(strength)

    # Accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate serve!')
        ball.testSetRoute(spot) 
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.testSetRoute(spot)
            print('Accurate serve!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best hand placement...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.testSetRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad touch...')
        return False


def testCalcRollReceive(ball:ball, accuracy:int, ballControl:int , spot:dict):# spot: {'gSpot':int, 'sSpot':int} 
    ball.stateUpdate('received')
    
    # calculating the contro of the ball for receive
    def calcControl():
        # ball control check which depends on velocity of the ball
        if ballControl >= ball.getVelocity():
            print('Took complete control over the ball!')
            ball.resetVelocity()
            ball.testSetRoute(spot)
            return True
        else:
            controlRoll = roll()
            if controlRoll > ball.getVelocity() - ballControl:
                print('Took complete control over the ball!')
                ball.resetVelocity()
                ball.testSetRoute(spot)
                return True
            elif controlRoll > ball.getVelocity() - (ballControl + ballControl // 10):# ex control = 40 ballV = 50.... 50 - (40 + 40/10)... has to roll more than 2
                print('Not the best control but its a up!!')
                ball.decreaseVelocity(ballControl)
                ball.testSetRoute(spot)
                return True
            else:# couldnt control the spike otherwise 
                print('oof, the spike overtook him')
                return False

    # Accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        return calcControl()
    else:# accracy stat is below 50
        accuracyRoll = roll()
        if accuracyRoll <= (accuracy * 2) + (accuracy // 5):# ex.40 == 80 + 8 = 88 chances of making it
            return calcControl()
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best recieve...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                print('but the ball goes where he wants it!')
                return calcControl()
            
        # the ball just goes out
        print('Oooh a bad recieve and the ball goes out...')
        return False

    
def testCalcRollSet(ball:ball, accuracy:int, spot:dict):# spot: {'gSpot':int, 'sSpot':int}
    ball.stateUpdate('setted')
    
    # accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate set!')
        ball.testSetRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.testSetRoute(spot)
            print('Accurate set!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best set...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.testSetRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad set and the ball goes out...')
        return False

def testCalcRollSpike(ball:ball, accuracy:int, spot:dict):# spot: {'gSpot':int, 'sSpot':int}
    ball.stateUpdate('spike')
    # accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate spike!')
        ball.testSetRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.testSetRoute(spot)
            print('Accurate spike!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best spike...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.testSetRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad spike and the ball goes out...')
        return False

##########


# Serve algorithm
def calcRollServe(ball:ball, accuracy:int, strength:int, spot:int):
    ball.stateUpdate('served')
    
    # Strength = velocity added to the ball
    ball.increaseVelocity(strength)
    
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
def calcRollReceive(ball:ball, accuracy:int, ballControl:int , spot:int):
    ball.stateUpdate('received')
    
    # calculating the contro of the ball for receive
    def calcControl():
        # ball control check which depends on velocity of the ball
        if ballControl >= ball.getVelocity():
            print('Took complete control over the ball!')
            ball.resetVelocity()
            ball.setRoute(spot)
            return True
        else:
            controlRoll = roll()
            if controlRoll > ball.getVelocity() - ballControl:
                print('Took complete control over the ball!')
                ball.resetVelocity()
                ball.setRoute(spot)
                return True
            elif controlRoll > ball.getVelocity() - (ballControl + ballControl // 10):# ex control = 40 ballV = 50.... 50 - (40 + 40/10)... has to roll more than 2
                print('Not the best control but its a up!!')
                ball.decreaseVelocity(ballControl)
                ball.setRoute(spot)
                return True
            else:# couldnt control the spike otherwise 
                print('oof, the spike overtook him')
                return False

    # Accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        return calcControl()
    else:# accracy stat is below 50
        accuracyRoll = roll()
        if accuracyRoll <= (accuracy * 2) + (accuracy // 5):# ex.40 == 80 + 8 = 88 chances of making it
            return calcControl()
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best recieve...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                print('but the ball goes where he wants it!')
                return calcControl()
            
        # the ball just goes out
        print('Oooh a bad recieve and the ball goes out...')
        return False

# setting algorithm
def calcRollSet(ball:ball, accuracy:int, spot:int):
    ball.stateUpdate('setted')
    
    # accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate set!')
        ball.setRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.setRoute(spot)
            print('Accurate set!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best set...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.setRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad set and the ball goes out...')
        return False

# spiking algorithm
def calcRollSpike(ball:ball, accuracy:int, strength:int, spot:int):
    ball.stateUpdate('spiked')
    
    # Strength to ball
    ball.increaseVelocity(strength)
    
    # accuracy check
    if accuracy >= 50:# accuracy state of 50 or over is guaranteed to go where it goes
        print('Accurate spike!')
        ball.setRoute(spot)
        return True
    else:
        accuracyRoll = roll()
        if accuracyRoll <= accuracy * 2:# if accuracy stat is lower, it has a accuracy stat * 2 chance of making it accurate
            ball.setRoute(spot)
            print('Accurate spike!')
            return True 
        elif accuracyRoll <= accuracy * 3:# if roll is between accuracy stat * 2 and accuracy stat * 3, its a off serve that might be off
            accuracyRoll = roll()
            print('not the best spike...')
            if accuracyRoll <= 50:# 50/50 if the ball goes in and where he wants it
                ball.setRoute(spot)
                print('but the ball goes where he wants it!')
                return True
            
        # the ball just goes out
        print('Oooh a bad spike and the ball goes out...')
        return False
    