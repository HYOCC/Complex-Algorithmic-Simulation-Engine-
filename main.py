import resources.ballObj as ballClass
import resources.player as playerClass

hitter1 = playerClass.player('Oscar', 50)
setter1 = playerClass.player('Nick', 80,)

hitter2 = playerClass.player('John', 40,)
setter2 = playerClass.player('Johnny', 50,)

ball = ballClass.ball()

court1 = [[],
          []]
court2 = [[],
          []]

team1 ={hitter1: 'OH', setter1: 'S'}
for key, value in team1.items():
    if value == 'OH':
        court1[1].append(key) 
    elif value == 'S':
        court1[0].append(key)

team2 = {hitter2: 'OH', setter2: 'S'}
for key, value in team2.items():
    if value == 'OH':
        court2[1].append(key)
    elif value == 'S':
        court2[0].append(key)

# gets the closest player of where the ball is heading towards 
def getCPlayer(ball, cTeam):
    positionIndex = int(ball.getRoute()) - 1
    cPlayer = cTeam[positionIndex][0]
    
    return cPlayer

if __name__ == '__main__':
    team1Point = 0
    team2Point = 0
    
    cTeam = court1# implement coin flip to determine who serves first
    
    while team1Point != 10 and team2Point != 10: # To do: implement overtime

            if ball.getState() == 'none':
                # Serve sequence, only happens once during the match
                cPlayer = cTeam[1][0]
                print(f'{cPlayer} starts with the ball!!')
                spot = input(f'where would {cPlayer} serve? (1,2) ')
                while not(spot) or int(spot) not in [1, 2]:
                    spot = input(f'where would {cPlayer} serve? (1,2) ')
        
                # algorithm for serve
                serveGood = cPlayer.serve(ball, int(spot))
        
            # Serve made it over and in
            elif ball.getState() == 'served' and serveGood:
                print(f'The ball is served towards the {ball.getRoute()} spot!')
                cTeam = court1 if cTeam == court2 else court2
                
                # sets current player to the player that the ball is headed towards
                cPlayer = getCPlayer(ball, cTeam)
                
                print(f'Ball is headed towards {cPlayer}')
                spot = input(f'{cPlayer} receives to... (1,2) ')
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
                spot = input(f'{cPlayer} sets it to.... (1,2) ')
                while not(spot) or int(spot) not in [1, 2]:
                    spot = input(f'{cPlayer} sets it to.... (1,2) ')
                # algorithm for setting 
                setGood = cPlayer.set(ball, int(spot)) 
                receiveGood = False 
            
            # spiking the set
            elif ball.getState() == 'setted' and setGood:
                print('Place holder: Spiking')
                break
            
            # whichever is the the cTeam aka the last team to touch the ball loses the point if none of the above was doing correctly
            else:
                print(f'{cPlayer} misses...1')
                if cTeam == court1:
                    team2Point += 1
                    cTeam = court2
                else:
                    team1Point += 1
                    cTeam = court1 
                print(f'current score is team1 : {team1Point} | team 2: {team2Point}') 
            
    
    if team2Point == 10:
        print('Team2 WONN!!!')
    else:
        print('Team1 WONN!!')
        
    
    
        
        