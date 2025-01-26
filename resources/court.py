from resources.turnStructure import queue

class court():
    def __init__(self, players:dict):# players: {playerObj:position} 
        self.court = [[],[],[],
                      [],[],[]]
        
        # puts the player of the team onto the court
        for key, value in players.items():
            if value == 'OH':
                self.court[0].append(key) 
            elif value == 'S':
                self.court[2].append(key)
            elif value == 'L':
                self.court[4].append(key)
        
        self.queue = queue(players)
        
    # printing out the court to terminal for better visualization
    def printCourtState(self):
        for i in range(len(self.court)):
            if i == 2:# starts a new line after 3 spot
                if self.court[i]:
                    print(self.court[i], end=' ')
                else:
                    print('[     ]', end = ' ')
                print('')
            else:
                if self.court[i]:
                    print(self.court[i], end = ' ') 
                else:
                    print('[     ]', end = ' ')
        print('')

    def getCourt(self):
        return self.court
    
    def getHighest(self):
        self.queue.getHighest()
        
    def getLowest(self):
        self.queue.getLowest()
    
    def resetQueue(self):
        self.queue.resetQueue()
    
    def __str__(self):
        return self.court

    def __repr__(self):
        return self.__str__()
