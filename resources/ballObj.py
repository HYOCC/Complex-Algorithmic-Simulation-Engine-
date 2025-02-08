class ball():
    def __init__(self):
        self.route = None# Which spot the ball is headed towards
        self.state = 'none'
        self.velocity = 0# affected by strength stats
        

    # sets where the ball is going
    def setRoute(self, spot:int):
        self.route = spot
    
    # gets where the ball is headed towards
    def getRoute(self):
        return self.route

    ########## Testing for 36x36 court
    
    def testSetRoute(self, spot:dict):# # spot: {'gSpot':number, 'sSpot':number}
        self.gSpot = int(spot['gSpot'])
        self.sSpot = int(spot['sSpot'])
        
    def testgetRoute(self):
        return {'gSpot':self.gSpot, 'sSpot': self.sSpot}
    
    ##########
    
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