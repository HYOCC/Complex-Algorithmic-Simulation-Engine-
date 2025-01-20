from resources.rngCalc import calcRollServe, calcRollReceive, calcRollSet, calcRollSpike

class player():
    def __init__(self, name, accuracy, strength=None):# strength in development
        self.name = name 
        self.accuracy = accuracy# determining how accurate the player is on deciding where the ball will be headed towards
        self.strength = strength# how much speed the player puts on the ball aka difficulty of receiving the ball
        
    def serve(self, ball, spot:int):
        return calcRollServe(ball, self.accuracy, self.strength, spot)
    
    def receive(self, ball, spot:int):
        return calcRollReceive(ball, self.accuracy, spot)
    
    def set(self, ball, spot:int):
        return calcRollSet(ball, self.accuracy, spot)
    
    def spike(self, ball, spot:int):
        return calcRollSpike(ball, self.accuracy, self.strength, spot)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()