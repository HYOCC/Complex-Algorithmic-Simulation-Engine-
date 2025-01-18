from resources.rngCalc import calcRollServe, calcRollReceive, calcRollSet, calcRollSpike

class player():
    def __init__(self, name, accuracy):
        self.name = name 
        self.accuracy = accuracy# determining how accurate the player is on deciding where the ball will be headed towards
    
    def serve(self, ball, spot:int):
        return calcRollServe(ball, self.accuracy, spot)
    
    def receive(self, ball, spot:int):
        return calcRollReceive(ball, self.accuracy, spot)
    
    def set(self, ball, spot:int):
        return calcRollSet(ball, self.accuracy, spot)
    
    def spike(self, ball, spot:int):
        return calcRollSpike(ball, self.accuracy, spot)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()