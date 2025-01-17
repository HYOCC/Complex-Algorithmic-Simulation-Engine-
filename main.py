import resources.ballObj as ballClass
import resources.player as playerClass

hitter1 = playerClass.player('Oscar', 0)
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

if __name__ == '__main__':
    team1Point = 0
    team2Point = 0
    
    cTeam = court1
    
    while team1Point != 10 or team2Point != 10: # To do: implement overtime
        # Serve sequence, only happens once during the match
        cPlayer = cTeam[1][0]
        print(f'{cPlayer} starts with the ball!!')
        spot = input(f'where would {cPlayer} serve? (1,2) ')
        while not(spot) or int(spot) not in [1, 2]:
            spot = input(f'where would {cPlayer} serve? (1,2) ')
        serveGood = cPlayer.serve(ball, int(spot))
        if serveGood:
            print(f'The ball is headed towards {ball.getRoute()} spot!')
            # success serve
            cTeam = court1 if cTeam == court2 else court1
            # Starts the actual game after service
            while True:
                positionIndex = int(ball.getRoute()) - 1
                cPlayer = cTeam[positionIndex][0]
                print(f'Ball is headed towards {cPlayer}')
                
                action = input(f'What will {cPlayer} do?')
        else:# serve wasnt successful thus current point ended
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
        
    
    
        
        