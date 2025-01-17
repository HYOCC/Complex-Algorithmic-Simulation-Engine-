import resources.ballObj as ballClass
import resources.player as playerClass

hitter1 = playerClass.player('Oscar', 10)
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
    # Serve sequence, only happens once during the match
    cPlayer = court1[1][0]
    print(f'{cPlayer} starts with the ball!!')
    spot = input(f'where would {cPlayer} serve? (1,2) ')
    while not(spot)  and int(spot) not in [1, 2]:
        spot = input(f'where would {cPlayer} serve? (1,2) ')
    serveGood = cPlayer.serve(ball, spot)
    if serveGood:
        print(f'The ball is headed towards {ball.getRoute()} spot!')
    else:
        print(f'{cPlayer} misses...1')
            
        
        