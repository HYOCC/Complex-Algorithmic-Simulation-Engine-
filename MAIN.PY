import resources.ballObj as ballClass
import resources.player as playerClass
import resources.court as courtClass

# Team 1
hitter1 = playerClass.player('Oscar', 40,60, 30, 30)
setter1 = playerClass.player('NickR', 40, 40, 40, 40)
libero1 = playerClass.player('KyleS', 50, 20, 60, 70)

# team 2 
hitter2 = playerClass.player('Johnn', 50, 45, 30, 50)
setter2 = playerClass.player('Lonnn', 50, 30, 50, 40)
libero2 = playerClass.player('Jason', 45 , 20, 55, 60)

# ball class
ball = ballClass.ball()

# court class and printing for visualization
team1 = {hitter1: 'OH', setter1: 'S', libero1: 'L'}
court1 = courtClass.court(team1)
court1.printCourtState()

print('')
team2 = {hitter2: 'OH', setter2: 'S', libero2: 'L'}
court2 = courtClass.court(team2)
court2.printCourtState()
        
# gets the closest player of where the ball is heading towards 
def getCPlayer(ball, cTeam:courtClass):# need to change in case there is no player there by getting action from the fastest/reactionspeed character
    positionIndex = int(ball.getRoute()) - 1
    if cTeam.getCourt()[positionIndex]:
        cPlayer = cTeam.getCourt()[positionIndex][0]
        return cPlayer
    else:
        return False

def point(cPlayer, cTeam, team1Point, team2Point):
    print(f'{cPlayer} misses...1')
    if cTeam == court1:
        team2Point += 1
        cTeam = court2
    else:
        team1Point += 1
        cTeam = court1
    print(f'current score is team1 : {team1Point} | team 2: {team2Point}') 
    
    # resets the state of the ball
    ball.resetState()
    ball.resetVelocity()
    
    return cTeam, team1Point, team2Point

if __name__ == '__main__':
    team1Point = 0
    team2Point = 0
    
    cTeam = court1# implement coin flip to determine who serves first
    
    # keeps track of last player that touched the ball
    lastTouch = None
    
    while team1Point != 10 and team2Point != 10: # To do: implement overtime
        
        # serving
        if ball.getState() == 'none':
            # Serve sequence, only happens once during the match
            cPlayer = cTeam.getCourt()[4][0]
            print(f'\n\nCurrent player: {cPlayer}\n')
            print(f'{cPlayer} starts with the ball!!')
            spot = input(f'where would {cPlayer} serve? (1,2,3,4,5,6) ')
            while not(spot) or int(spot) not in [1, 2,3,4,5,6]:
                spot = input(f'where would {cPlayer} serve? (1,2,3,4,5,6) ')
    
            # algorithm for serve
            serveGood = cPlayer.serve(ball, int(spot))
    
        # Serve made it over and in
        elif ball.getState() == 'served' and serveGood:
            
            # rallying starts
            cTeam = court1 if cTeam == court2 else court2
            
            # sets current player to the player that the ball is headed towards
            cPlayer = getCPlayer(ball, cTeam)
            
            # if there is no player in the ball route
            while cPlayer == False:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam = point(cPlayer, cTeam, team1Point, team2Point)
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
                print(f'\n\nCurrent player: {cPlayer}\n')
                print(f'The ball is served towards {cPlayer} at a speed of {ball.getVelocity()} km/s spot!!')  
                
                # resets the queue
                cTeam.resetQueue()
                
                spot = input(f'\n{cPlayer} receives to... (1,2,3,4,5,6) ')
                while not(spot) or int(spot) not in [1, 2,3,4,5,6]:
                    spot = input(f'{cPlayer} receives to... (1,2,3,4,5,6) ')
                    
                # algorithm for receive
                receiveGood = cPlayer.receive(ball, int(spot))
                serveGood = False
                
                #updates cPlayer
                lastTouch = cPlayer

        # ball was received and needse to be set
        elif ball.getState() == 'received' and receiveGood:
        
            # sets current player to the player that the ball is headed towards
            cPlayer = getCPlayer(ball, cTeam) 
            
            # if there is no player in the ball route
            while cPlayer == False or cPlayer is lastTouch:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam = point(cPlayer, cTeam, team1Point, team2Point)
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
                        
                        #testing
                        print(cTeam.getPlayerPOS(player))
                        
                        # swaps the position of the player originally there with the current player that is being moved
                        cTeam.swapPlayer(cPlayer, player)
                    else:
                        # attempts* moves the player to the ball route
                        cTeam.movePlayer(player, ball.getRoute())
                    
                    # sees if there is a player now
                    cPlayer = getCPlayer(ball, cTeam)
            else: 
                print(f'Ball is headed towards {cPlayer}')
                print(f'\n\nCurrent player: {cPlayer}\n')
                cTeam.printCourtState()# gets a visualization of the court
                
                # resets the queue
                cTeam.resetQueue()
                
                spot = input(f'\n{cPlayer} sets it to.... (1,2,3,4,5,6) ')
                while not(spot) or int(spot) not in [1, 2,3,4,5,6]:
                    spot = input(f'{cPlayer} sets it to.... (1,2,3,4,5,6) ')               
                
                # algorithm for setting 
                setGood = cPlayer.set(ball, int(spot)) 
                receiveGood = False 
                
                #updates cPlayer
                lastTouch = cPlayer

        # spiking the set
        elif ball.getState() == 'setted' and setGood:
            # sets current player to the ball direction
            cPlayer = getCPlayer(ball, cTeam)
            
            # if there is no player in the ball route
            while cPlayer == False or cPlayer == lastTouch:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam = point(cPlayer, cTeam, team1Point, team2Point)
                    setGood = False
                    break
                
                # gets the player with the highest reaction 
                player = cTeam.getHighest()
                if player is lastTouch:
                    player = cTeam.getHighest() 
                
                spot = input(f'{player} sees the ball coming, move towards the ball? (Y/N) ')
                if spot.upper() == 'Y':
                    
                    # attempts* moves the player to the ball route
                    cTeam.movePlayer(player, ball.getRoute())
                    
                    # sees if there is a player now
                    cPlayer = getCPlayer(ball, cTeam)
            else:
                
                # user accessbility
                print(f'ball is setted towards {cPlayer}')
                print(f'\n\nCurrent player: {cPlayer}\n')
                opposite = court1 if cTeam == court2 else court2 
                opposite.printCourtState()# gets a visualization of the court
                
                # player spike location
                spot = input(f'\n{cPlayer} spikes it to.... (1,2,3,4,5,6) ')
                while not(spot) or int(spot) not in [1, 2,3,4,5,6]:
                    spot = input(f'{cPlayer} spikes it to.... (1,2,3,4,5,6) ')
            
                # resets the queue
                cTeam.resetQueue()
            
                # algorithm for how well the spike is
                spikeGood = cPlayer.spike(ball, int(spot))
                setGood = False
                
                # updates last player 
                lastTouch = cPlayer
                
                if spikeGood:
                    cTeam = court1 if cTeam == court2 else court2
        
        # ball was spiked and other team needs to dig it
        elif ball.getState() == 'spiked' and spikeGood:
            # sets current player to the ball direction
            cPlayer = getCPlayer(ball, cTeam)
            
            # if there is no player in the ball route
            while cPlayer == False:
                if cTeam.checkHighest():# returns True if no more object are in queue
                    # game over since no player got to there
                    cTeam = point(cPlayer, cTeam, team1Point, team2Point)
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
                print(f'\n\nCurrent player: {cPlayer}\n')
                cTeam.printCourtState()
                
                # player receive location
                spot = input(f'\n{cPlayer} receives it to.... (1,2,3,4,5,6) ')
                cTeam.printCourtState()# gets a visualization of the court
                while not(spot) or int(spot) not in [1, 2,3,4,5,6]:
                    spot = input(f'{cPlayer} receives it to.... (1,2,3,4,5,6) ')

                # algorithm for recieving
                receiveGood = cPlayer.receive(ball , int(spot))
                spikeGood = False
                
                lastTouch = cPlayer# updates last touch
                
        # whichever is the the cTeam aka the last team to touch the ball loses the point if none of the above was doing correctly
        else:
            cTeam, team1Point, team2Point = point(cPlayer, cTeam, team1Point, team2Point)
            # resets the queue
            cTeam.resetQueue()

    
    if team2Point == 10:
        print('Team2 WONN!!!')
    else:
        print('Team1 WONN!!')
        
    
    
        
        
