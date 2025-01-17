class ball():
    def __init__(self):
        self.attributes = {'difficulty': 0}
        self.route = None# Which spot the ball is headed towards
        self.state = 'none'

    # route
    def setRoute(self, spot:int):
        self.route = spot
    
    def getRoute(self):
        return self.route
