import resources.ballObj as ballClass
import resources.player as playerClass
import resources.court as courtClass

# Team 1
hitter1 = playerClass.player('Oscar', 0, 0, 0, 0)
setter1 = playerClass.player('NickR', 40, 40, 40, 40)
libero1 = playerClass.player('KyleS', 50, 20, 60, 70)
right1 = playerClass.player('ooopy', 40, 60, 30, 30)
outside1 = playerClass.player('joppy', 40,60, 30, 30)
middle1 = playerClass.player('p2snis', 40,60, 30, 30)


# team 2 
hitter2 = playerClass.player('Johnn', 50, 45, 30, 50)
setter2 = playerClass.player('Lonnn', 50, 30, 50, 40)
libero2 = playerClass.player('Jason', 45 , 20, 55, 60)
outside2 = playerClass.player('Poppy', 40,60, 30, 30)
right2 = playerClass.player('Mommy', 40,60, 30, 30)
midde2 = playerClass.player('BIGPLYER', 40,60, 30, 30)

# ball class
ball = ballClass.ball()

# court class and printing for visualization
team1 = {hitter1: 'OH', setter1: 'S', libero1: 'L', right1:'RH', outside1: 'OH', middle1: 'M'}
court1 = courtClass.court(team1)# constant court so when rally ends, court1 is reset to COURT1
court1.printCourtState()

print('')
team2 = {hitter2: 'OH', setter2: 'S', libero2: 'L', right2:'RH', outside2: 'OH', midde2: 'M'}
court2 = courtClass.court(team2)# constant court so when rally ends, court2 is reset to COURT2
court2.printCourtState()

#_____HELPER FUNCTIONS_____

# gets the closest player of where the ball is heading towards 
def getCPlayer(ball, cTeam:courtClass):# need to change in case there is no player there by getting action from the fastest/reactionspeed character
    positionIndex = int(ball.getRoute()) - 1
    if cTeam.getCourt()[positionIndex]:
        cPlayer = cTeam.getCourt()[positionIndex][0]
        return cPlayer
    else:
        return False

def getCPlayer(ball:ballClass, cTeam:courtClass):
    positionIndex = ball.getRoute() 
    # unpacking the datas
    gSpot, sSpot = positionIndex['gSpot']- 1 , positionIndex['sSpot'] -1
    print(f'gSpot:{gSpot}, sSpot:{sSpot}')
    
    
    if cTeam.getCourt()[gSpot][sSpot]:
        cPlayer = cTeam.getCourt()[gSpot][sSpot][0]
        return cPlayer
    else:
        return False

def point(cPlayer, cTeam, team1Point, team2Point):
    global court1, court2 
    
    print(f'{cPlayer} misses...1')
    if cTeam == court1:
        team2Point += 1
        cTeam = court2
        oTeam = court1
    else:
        team1Point += 1
        cTeam = court1
        oTeam = court2
    print(f'current score is team1 : {team1Point} | team 2: {team2Point}') 
    
    # resets the state of the ball
    ball.resetState()
    ball.resetVelocity()
    
    # resets the queue
    cTeam.resetQueue()
    oTeam.resetQueue()
    
    # resets the teams court
    cTeam.resetCourt()
    oTeam.resetCourt()
    
    return cTeam, oTeam, team1Point, team2Point

if __name__ == '__main__':
    team1Point = 0
    team2Point = 0
    
    cTeam = court1# implement coin flip to determine who serves first
    oTeam = court2
    
    # keeps track of last player that touched the ball
    lastTouch = None
    
    while team1Point != 10 and team2Point != 10: # To do: implement overtime
                
        if ball.getState() == 'none':
            
            print('Oppposite Team Court: \n')
            oTeam.printCourtState()# Opposite team court
            
            cPlayer = cTeam.getCourt()[5][4][0]
            print(f'\n\nCurrent player: {cPlayer}\n\n')
            print(f'{cPlayer} starts with the ball!!')
            gSpot = input(f'where would {cPlayer} serve? (1,2,3,4,5,6) ')
            while not(gSpot) or int(gSpot) not in [1, 2,3,4,5,6]:
                gSpot = input(f'where would {cPlayer} serve? (1,2,3,4,5,6) ')
            
            sSpot = input(f'specifc position? (1,2,3,4,5,6,7,8,9) ')
            while not(sSpot) or int(sSpot) not in [1,2,3,4,5,6,7,8,9]:
                sSpot = input(f'specifc position? (1,2,3,4,5,6,7,8,9) ' )
            
            spot = {'gSpot': gSpot, 'sSpot': sSpot}
            
            # serving the ball
            serveGood = cPlayer.serve(ball, spot)
            
        # receiving serve
        if ball.getState() == 'served' and serveGood:
            # rallying starts
            cTeam = court1 if cTeam is court2 else court2
            oTeam = court1 if oTeam is court2 else court2
            
            # sets current player to the player that the ball is headed towards
            cPlayer = getCPlayer(ball, cTeam)
            
            # if there is no player in the ball route
            while cPlayer == False:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam, oTeam, team1Point, team2Point = point(cPlayer, cTeam, team1Point, team2Point)
                    serveGood = False
                    break
                    
                # gets the player with the highest reaction 
                player = cTeam.getHighest()
                spot = input(f'{player} sees the ball coming, move towards the ball? (Y/N) ')
                if spot.upper() == 'Y':
                    
                    # attempts* moves the player to the ball route
                    cTeam.movePlayer(player, ball.getRoute())
                    
                    # sees if there is a player now
                    cPlayer = getCPlayer(ball, cTeam)
            else:
                # user visual
                print(f'\n\nCurrent player: {cPlayer}\n\n')
                print(f'The ball is served towards {cPlayer} at a speed of {ball.getVelocity()} km/s spot!!\n\n')  
                print('Current Team Court: \n')
                cTeam.printCourtState()
                
                # resets the queue
                cTeam.resetQueue()
                
                gSpot = input(f'\n{cPlayer} receives to... (1,2,3,4,5,6) ')
                while not(gSpot) or int(gSpot) not in [1,2,3,4,5,6]:
                    gSpot = input(f'{cPlayer} receives to... (1,2,3,4,5,6) ')
                sSpot = input('specifc position? (1,2,3,4,5,6,7,8,9) ')
                while not(sSpot) or int(sSpot) not in [1,2,3,4,5,6,7,8,9]:
                    sSpot = input(f'specifc position? (1,2,3,4,5,6,7,8,9) ' )
                
                # algorithm for receive
                receiveGood = cPlayer.receive(ball, {'gSpot': gSpot, 'sSpot': sSpot}) 
                serveGood = False
                
                #updates cPlayer
                lastTouch = cPlayer
        
        # setting
        elif ball.state() == 'received' and receiveGood:
            # sets current player to the player that the ball is headed towards
            cPlayer = getCPlayer(ball, cTeam) 
            
            # if there is no player in the ball route
            while cPlayer == False or cPlayer is lastTouch:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam, oTeam, team1Point, team2Point = point(cPlayer, cTeam, team1Point, team2Point)
                    receiveGood = False
                    break
                
                # gets the player with the highest reaction 
                player = cTeam.getHighest() 
                if player is lastTouch:
                    player = cTeam.getHighest() 
                
                spot = input(f'{player} sees the ball coming, move towards the ball? (Y/N) ')
                if spot.upper() == 'Y':
                    
                    # there was already a player in the spot where the ball is headed
                    if cPlayer:               
                        # swaps the position of the player originally there with the current player that is being moved
                        cTeam.swapPlayer(cPlayer, player)
                    else:
                        # attempts* moves the player to the ball route
                        cTeam.movePlayer(player, ball.getRoute())
                    
                    # sees if there is a player now
                    cPlayer = getCPlayer(ball, cTeam)
            else: 
                print(f'Ball is headed towards {cPlayer}')
                print(f'\n\nCurrent player: {cPlayer}\n\n')
                print('Current Team Court: \n')
                cTeam.printCourtState()# gets a visualization of the court
                
                # resets the queue
                cTeam.resetQueue()
                
                gSpot = input(f'\n{cPlayer} sets it to... (1,2,3,4,5,6) ')
                while not(gSpot) or int(gSpot) not in [1,2,3,4,5,6]:
                    gSpot = input(f'{cPlayer} sets it to... (1,2,3,4,5,6) ')
                sSpot = input('specifc position? (1,2,3,4,5,6,7,8,9) ')
                while not(sSpot) or int(sSpot) not in [1,2,3,4,5,6,7,8,9]:
                    sSpot = input(f'specifc position? (1,2,3,4,5,6,7,8,9) ' )              
                
                # algorithm for setting 
                setGood = cPlayer.set(ball, {'gSpot': gSpot, 'sSpot': sSpot}) 
                receiveGood = False 
                
                #updates cPlayer
                lastTouch = cPlayer
            pass
         
        # hitting
        elif ball.getState() == 'setted' and setGood:
            # sets current player to the ball direction
            cPlayer = getCPlayer(ball, cTeam)
            
            # if there is no player in the ball route or the current player in the ball route already touched
            while cPlayer == False or cPlayer == lastTouch:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam, oTeam, team1Point, team2Point = point(cPlayer, cTeam, team1Point, team2Point)
                    setGood = False
                    break
                
                # gets the player with the highest reaction 
                player = cTeam.getHighest()
                if player is lastTouch:
                    player = cTeam.getHighest() 
                
                spot = input(f'{player} sees the ball coming, move towards the ball? (Y/N) ')
                if spot.upper() == 'Y':
                    
                    # there was already a player in the spot where the ball is headed
                    if cPlayer:
                        # swaps the position of the player originally there with the current player that is being moved
                        cTeam.swapPlayer(cPlayer, player)
                    else:
                        # attempts* moves the player to the ball route
                        cTeam.movePlayer(player, ball.getRoute())
                    
                    # sees if there is a player now
                    cPlayer = getCPlayer(ball, cTeam)
            else:
                
                # user accessbility
                print(f'ball is setted towards {cPlayer}')
                print(f'\n\nCurrent player: {cPlayer}\n\n')
                print('')
                print('Oppposite Team Court: \n')
                oTeam.printCourtState()# gets a visualization of the court
                
                gSpot = input(f'\n{cPlayer} spikes it to... (1,2,3,4,5,6) ')
                while not(gSpot) or int(gSpot) not in [1,2,3,4,5,6]:
                    gSpot = input(f'{cPlayer} sets it to... (1,2,3,4,5,6) ')
                sSpot = input('specifc position? (1,2,3,4,5,6,7,8,9) ')
                while not(sSpot) or int(sSpot) not in [1,2,3,4,5,6,7,8,9]:
                    sSpot = input(f'specifc position? (1,2,3,4,5,6,7,8,9) ' )    
            
                # resets the queue
                cTeam.resetQueue()
            
                # algorithm for how well the spike is
                spikeGood = cPlayer.spike(ball, {'gSpot': gSpot, 'sSpot':sSpot})
                setGood = False
                
                # updates last player 
                lastTouch = cPlayer
                
                if spikeGood:
                    print('ping')
                    cTeam = court1 if cTeam is court2 else court2
                    oTeam = court1 if oTeam is court2 else court2
        # receiving a spike
        elif ball.getState() == 'spike' and spikeGood:            
            # sets current player to the ball direction
            cPlayer = getCPlayer(ball, cTeam)
            
            # if there is no player in the ball route
            while cPlayer == False:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam, oTeam, team1Point, team2Point = point(cPlayer, cTeam, team1Point, team2Point)
                    spikeGood = False
                    break
                
                # gets the player with the highest reaction 
                player = cTeam.getHighest()
                spot = input(f'{player} sees the ball coming, move towards the ball? (Y/N) ')
                if spot.upper() == 'Y':
                    
                    # attempts* moves the player to the ball route
                    cTeam.movePlayer(player, ball.getRoute())
                    
                    # sees if there is a player now
                    cPlayer = getCPlayer(ball, cTeam)
            else:
                
                # user visulatizaiton
                print(f'ball is spiked towards {cPlayer} at a {ball.getVelocity()} km/s!!!')
                print(f'\n\nCurrent player: {cPlayer}\n\n')
                cTeam.printCourtState()
                
                # player receive location
                gSpot = input(f'\n{cPlayer} receiveit to... (1,2,3,4,5,6) ')
                while not(gSpot) or int(gSpot) not in [1,2,3,4,5,6]:
                    gSpot = input(f'{cPlayer} sets it to... (1,2,3,4,5,6) ')
                sSpot = input('specifc position? (1,2,3,4,5,6,7,8,9) ')
                while not(sSpot) or int(sSpot) not in [1,2,3,4,5,6,7,8,9]:
                    sSpot = input(f'specifc position? (1,2,3,4,5,6,7,8,9) ' )  

                # algorithm for recieving
                receiveGood = cPlayer.receive(ball, {'gSpot': gSpot, 'sSpot': sSpot})
                spikeGood = False
                
                lastTouch = cPlayer# updates last touch'''
        
        # whichever is the the cTeam aka the last team to touch the ball loses the point if none of the above was doing correctly
        else:
            cTeam, oTeam, team1Point, team2Point = point(cPlayer, cTeam, team1Point, team2Point)
        
        
        
        
        run = False
    
    if team2Point == 10:
        print('Team2 WONN!!!')
    else:
        print('Team1 WONN!!')
        
    
    
        
        
