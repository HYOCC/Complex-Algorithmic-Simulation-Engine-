class ball():
    def __init__(self):
        self.route = None# Which spot the ball is headed towards
        self.state = 'none'

    # sets where the ball is going
    def setRoute(self, spot:int):
        self.route = spot
    
    # gets where the ball is headed towards
    def getRoute(self):
        return self.route

    # ball state update
    def stateUpdate(self, action:str):
        self.state = action
    
    # gets ball state
    def getState(self):
        return self.state 