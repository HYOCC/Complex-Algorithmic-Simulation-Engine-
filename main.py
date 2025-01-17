import resources.ballObj as ballClass
import resources.player as playerClass

player1 = playerClass.player('Oscar', 100)
player2 = playerClass.player('John', 90)
ball = ballClass.ball()

players = [player1, player2]

if __name__ == '__main__':
    while True:
        for player in players:
            if ball.state == 'none' or ball.state == 'hit':
                input(f'{player} hit?')
                player.hit(ball) 
                ball.state = 'receive'
            elif ball.state == 'receive':
                input(f'{player} receive?')
                player.receive(ball)
                ball.state = 'hit'