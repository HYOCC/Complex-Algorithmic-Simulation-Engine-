class ball():
    def __init__(self):
        self.route = None# Which spot the ball is headed towards
        self.state = 'none'
        self.velocity = 0# affected by strength stats
    
    def setRoute(self, spot:dict):# # spot: {'gSpot':number, 'sSpot':number}
        self.gSpot = int(spot['gSpot'])
        self.sSpot = int(spot['sSpot'])
        
    def getRoute(self):
        return {'gSpot':self.gSpot, 'sSpot': self.sSpot}
    
    # ball state update
    def stateUpdate(self, action:str):
        self.state = action
    
    # gets ball state
    def getState(self):
        return self.state 
    
    # resets the state back to serve mode for another point game
    def resetState(self):
        self.state = 'none'
    
    def increaseVelocity(self, amount:int):
        self.velocity += amount
    
    def decreaseVelocity(self, amount:int):
        self.velocity -= amount
    
    def resetVelocity(self):
        self.velocity = 0
    
    def getVelocity(self):
        return self.velocity