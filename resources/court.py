import resources.player as player
from resources.turnStructure import queue

class court():
    def __init__(self, players:dict):# players: {playerObj:position} 
        self.court = [[],[],[],
                      [],[],[]]
        self.hmap = {}# keeps track of the positions of the player directly {player:position}
        
        # puts the player of the team onto the court
        for key, value in players.items():
            if value == 'OH':
                self.court[0].append(key) 
                self.hmap[key] = 0
            elif value == 'S':
                self.court[2].append(key)
                self.hmap[key] = 2
            elif value == 'L':
                self.court[4].append(key)
                self.hmap[key] = 4 
        
        self.queue = queue(players)
    
    # moving a player on the court
    def movePlayer(self, player:player, spot:int):
        self.court[self.hmap[player]].pop()
        self.court[spot-1].append(player)
        self.hmap[player] = spot
        self.printCourtState()
        
        return True# work in progress to check player stat if it actually is a successful movement
    
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
        return self.queue.getHighest()
        
    def checkHighest(self):
        return self.queue.checkHighestEmpty()
    
    def getLowest(self):
        return self.queue.getLowest()
    
    def checkLowest(self):
        return self.queue.checkLowestEmpty()
    
    def resetQueue(self):
        self.queue.resetQueue()
    
    def __str__(self):
        return self.court

    def __repr__(self):
        return self.__str__()
