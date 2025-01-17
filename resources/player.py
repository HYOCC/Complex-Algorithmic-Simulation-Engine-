from resources.rngCalc import calcRollServe

class player():
    def __init__(self, name, accuracy):
        self.name = name 
        self.accuracy = accuracy
    
    def serve(self, ball, spot:int):
        return calcRollServe(ball, self.accuracy, spot)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()