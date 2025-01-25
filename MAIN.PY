import resources.ballObj as ballClass
import resources.player as playerClass
import resources.court as courtClass

# Team 1
hitter1 = playerClass.player('Oscar', 40,60, 30)
setter1 = playerClass.player('NickR', 40, 40, 40)
libero1 = playerClass.player('KyleS', 50, 20, 60)

# team 2 
hitter2 = playerClass.player('Johnn', 50, 45, 30)
setter2 = playerClass.player('Lonnn', 50, 30, 50)
libero2 = playerClass.player('Jason', 45 , 20, 55)

# ball class
ball = ballClass.ball()

team1 = {hitter1: 'OH', setter1: 'S', libero1: 'L'}
court1 = courtClass.court(team1)
court1.printCourtState()
print('')
team2 = {hitter2: 'OH', setter2: 'S', libero2: 'L'}
court2 = courtClass.court(team2)
court2.printCourtState()
        

# gets the closest player of where the ball is heading towards 
def getCPlayer(ball, cTeam):# need to change in case there is no player there by getting action from the fastest/reactionspeed character
    positionIndex = int(ball.getRoute()) - 1
    cPlayer = cTeam[positionIndex][0]
    
    return cPlayer

if __name__ == '__main__':
    team1Point = 0
    team2Point = 0
    
    cTeam = court1.getCourt()# implement coin flip to determine who serves first

    
    while team1Point != 10 and team2Point != 10: # To do: implement overtime

            if ball.getState() == 'none':
                # Serve sequence, only happens once during the match
                cPlayer = cTeam[4][0]
                print(f'{cPlayer} starts with the ball!!')
                spot = input(f'where would {cPlayer} serve? (1,2,3,4,5,6) ')
                while not(spot) or int(spot) not in [1, 2,3,4,5,6]:
                    spot = input(f'where would {cPlayer} serve? (1,2,3,4,5,6) ')
        
                # algorithm for serve
                serveGood = cPlayer.serve(ball, int(spot))
        
            # Serve made it over and in
            elif ball.getState() == 'served' and serveGood:
                cTeam = court1.getCourt() if cTeam == court2 else court2.getCourt()
                
                # sets current player to the player that the ball is headed towards
                cPlayer = getCPlayer(ball, cTeam)
                print(f'The ball is served towards {cPlayer} at a speed of {ball.getVelocity()} km/s spot!!')
                
                spot = input(f'\n{cPlayer} receives to... (1,2) ')
                while not(spot) or int(spot) not in [1, 2]:
                    spot = input(f'{cPlayer} receives to... (1,2) ')
                    
                # algorithm for receive
                receiveGood = cPlayer.receive(ball, int(spot))
                serveGood = False

            # Receive to the setter
            elif ball.getState() == 'received' and receiveGood:
            
                # sets current player to the player that the ball is headed towards
                cPlayer = getCPlayer(ball, cTeam)
                
                print(f'Ball is headed towards {cPlayer}')
                spot = input(f'\n{cPlayer} sets it to.... (1,2) ')
                while not(spot) or int(spot) not in [1, 2]:
                    spot = input(f'{cPlayer} sets it to.... (1,2) ')
                # algorithm for setting 
                setGood = cPlayer.set(ball, int(spot)) 
                receiveGood = False 
            
            # spiking the set
            elif ball.getState() == 'setted' and setGood:
                # sets current player to the ball direction
                cPlayer = getCPlayer(ball, cTeam)
                print(f'ball is setted towards {cPlayer}')
                
                # player spike location
                spot = input(f'\n{cPlayer} spikes it to.... (1,2) ')
                while not(spot) or int(spot) not in [1, 2]:
                    spot = input(f'{cPlayer} spikes it to.... (1,2) ')
                
                # algorithm for how well the spike is
                spikeGood = cPlayer.spike(ball, int(spot))
                setGood = False
                
                if spikeGood:
                    cTeam = court1.getCourt() if cTeam == court2 else court2.getCourt()
                
            elif ball.getState() == 'spiked' and spikeGood:
                # sets current player to the ball direction
                cPlayer = getCPlayer(ball, cTeam)
                print(f'ball is spiked towards {cPlayer} at a {ball.getVelocity()} km/s!!!')
                
                # player receive location
                spot = input(f'\n{cPlayer} receives it to.... (1,2) ')
                while not(spot) or int(spot) not in [1, 2]:
                    spot = input(f'{cPlayer} receives it to.... (1,2) ')
                
                # algorithm for recieving
                receiveGood = cPlayer.receive(ball , int(spot))
                spikeGood = False
                
            
            # whichever is the the cTeam aka the last team to touch the ball loses the point if none of the above was doing correctly
            else:
                print(f'{cPlayer} misses...1')
                if cTeam == court1:
                    team2Point += 1
                    cTeam = court2.getCourt()
                else:
                    team1Point += 1
                    cTeam = court1.getCourt()
                print(f'current score is team1 : {team1Point} | team 2: {team2Point}') 
                
                # resets the state of the ball
                ball.resetState()
                ball.resetVelocity()
            
    
    if team2Point == 10:
        print('Team2 WONN!!!')
    else:
        print('Team1 WONN!!')
        
    
    
        
        
