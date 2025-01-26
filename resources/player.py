from resources.rngCalc import calcRollServe, calcRollReceive, calcRollSet, calcRollSpike

class player():
    def __init__(self, name:str, accuracy:int, strength:int, ballControl:int, reactionSpeed:int):# strength in development
        self.name = name 
        self.accuracy = accuracy# determining how accurate the player is on deciding where the ball will be headed towards
        self.strength = strength# how much speed the player puts on the ball aka difficulty of receiving the ball
        self.ballControl = ballControl # currently its the how much speed you can control a spike from receive. ** FUTURE NOTE, will also be player's efficeicny of using a float, adding spins etc
        
        # gonna change reaction speed on when the ball is going towards player if they have enough reaction speed to do soetmhign ex. spiking a 60mhs ball and reaction speed is higher, and the ball goes towards them, they will ahve enough time to choose the best course of action such as receiving to whic spots or using hands or even moving a little
        self.reactionSpeed = reactionSpeed# Decides who gets to choose their turn first and also if they get to move preemptiuly when the ball is hit
        
        # what reaction sped is right now, higher means they are able to choose action base on what other players chooses
        self.vision = None
        
    def serve(self, ball, spot:int):
        print(f'\nCurrent player: {self.name}\n')
        return calcRollServe(ball, self.accuracy, self.strength, spot)
    
    def receive(self, ball, spot:int):
        print(f'\n\nCurrent player: {self.name}\n')
        return calcRollReceive(ball, self.accuracy, self.ballControl, spot)
    
    def set(self, ball, spot:int):
        print(f'\n\nCurrent player: {self.name}\n')
        return calcRollSet(ball, self.accuracy, spot)
    
    def spike(self, ball, spot:int):
        print(f'\n\nCurrent player: {self.name}\n')
        return calcRollSpike(ball, self.accuracy, self.strength, spot)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()