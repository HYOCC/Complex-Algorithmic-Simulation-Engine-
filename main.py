import resources.ballObj as ballClass
import resources.player as playerClass

player1 = playerClass.player('Oscar', 100)
player2 = playerClass.player('John', 90)
ball = ballClass.ball()

court1 = [[],
          []]
court2 = [[],
          []]

team1 ={player1: 'OH'}
for key, value in team1.items():
    if value == 'OH':
        court1[1].append(key) 
    elif value == 'S':
        court1[0].append(key)

team2 = {player2: 'OH'}
for key, value in team2.items():
    if value == 'OH':
        court2[1].append(key)
    elif value == 'S':
        court2[0].append(key)

if __name__ == '__main__':
    print(court1)
    print(court2)
        