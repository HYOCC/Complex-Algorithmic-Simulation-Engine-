import resources.player as player
from resources.turnStructure import queue

class court():
    def __init__(self, players:dict):# players: {playerObj:position} 
        self.court = [[],[],[],
                      [],[],[]]
        
        #_________________________Development
        
        self.experimental = [[[] for _ in range(9)] for _ in range(6)]
        self.testHmap = {}
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        
        for key, value in players.items():
            if value == 'OH' and not(self.experimental[0][4]): 
                self.experimental[0][4] = [key] 
                self.testHmap[key] = {'gSpot': 0, 'sSpot': 4}
            elif value == 'OH':
                self.experimental[5][4] = [key]
                self.testHmap[key] = {'gSpot': 5, 'sSpot': 4}
            elif value == 'S':
                self.experimental[2][4] = [key]
                self.testHmap[key] = {'gSpot': 2, 'sSpot': 4}
            elif value == 'L':
                self.experimental[4][4] = [key]
                self.testHmap[key] = {'gSpot': 4, 'sSpot': 4}
            elif value == 'RH':
                self.experimental[3][4] = [key]
                self.testHmap[key] = {'gSpot': 3, 'sSpot': 4}
            else:
                self.experimental[1][4] = [key] 
                self.testHmap[key] = {'gSpot': 1, 'sSpot': 4}
        self.printCourtStateTest()
        
        #___________________________________ 
        
        self.hmap = {}# keeps track of the positions of the player directly {player:position}
        
        # puts the player of the team onto the court
        for key, value in players.items():
            if value == 'OH' and not(self.court[0]):
                self.court[0].append(key) 
                self.hmap[key] = 0
            elif value == 'OH':
                self.court[5].append(key)
                self.hmap[key] = 5
            elif value == 'S':
                self.court[2].append(key)
                self.hmap[key] = 2
            elif value == 'L':
                self.court[4].append(key)
                self.hmap[key] = 4 
            elif value == 'RH':
                self.court[3].append(key)
                self.hmap[key] = 3
            else:
                self.court[1].append(key)
                self.hmap[key] = 1
                        
        self.queue = queue(players)
    
    #_____________________ Development 
    
    def printCourtStateTest(self):
        
        # Function to process a specific range of rows and columns
        def process_range(start_row, end_row, row_start, row_end):
            result = ""
            for i in range(start_row, end_row):
                for j in range(row_start, row_end):
                    if not self.experimental[i][j]:
                        result += '[\'  \']'
                    else:
                        result += f'[{str(self.experimental[i][j][0])[0:4]}]'
                result += '   '
            result += '\n'
            return result
        
        
        res = '' 
        # Process rows 0-2 (1-3 spot)
        res += process_range(0, 3, 0, 3)
        res += process_range(0, 3, 3, 6)
        res += process_range(0, 3, 6, 9)

        # Add spacing between sections
        res += '\n\n'

        # Process rows 3-5 (4-6 spot)
        res += process_range(3, 6, 0, 3)
        res += process_range(3, 6, 3, 6)
        res += process_range(3, 6, 6, 9)
        
        print(res) 
    
    def testGetCourt(self):
        return self.experimental
    
    def testMovePlayer(self, player:player, spot:dict):# spot = {'gSpot':int, 'sSpot':int}
        # removing from current spot
        currentGSpot = self.testHmap[player]['gSpot']
        currentSSpot = self.testHmap[player]['sSpot']
        self.experimental[currentGSpot][currentSSpot].pop()
        
        # moves the player to the new spot
        self.testHmap[player]['gSpot'] = spot['gSpot']
        self.testHmap[player]['sSpot'] = spot['sSpot']
        self.experimental[spot['gSpot'] - 1][spot['sSpot'] - 1].append(player)
        self.printCourtStateTest()
        return True # work in progress to check player stat if it actually is a successful movement
    #___________________________
    
    # moving a player on the court
    def movePlayer(self, player:player, spot:int):
        self.court[self.hmap[player]].pop()
        self.court[spot-1].append(player)
        self.hmap[player] = spot-1
        self.printCourtState()
        return True# work in progress to check player stat if it actually is a successful movement
    
    # swaps the position of two players with each other
    def swapPlayer(self, player1:player, player2:player):
        self.court[self.getPlayerPOS(player1)], self.court[self.getPlayerPOS(player2)] = self.court[self.getPlayerPOS(player2)], self.court[self.getPlayerPOS(player1)]
        self.hmap[player1] = self.getPlayerPOS(player2)
        self.hmap[player2] = self.getPlayerPOS(player1)
        
    # printing out the court to terminal for better visualization
    def printCourtState(self):
        res = ''
        
        for i in range(len(self.court)):
            if i == 2:# starts a new line after 3 spot
                if self.court[i]:
                    res += f'[{self.court[i][0]}]'
                else:
                    res += '[     ]' 
                res += '\n'
            else:
                if self.court[i]:
                    res += f'[{self.court[i][0]}]'
                else:
                    res += '[     ]' 
        res += '\n'
        print(res)

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
    
    # gets the player position using the hmap
    def getPlayerPOS(self, player:player):
        return self.hmap[player] 
    
    def __str__(self):
        return self.court

    def __repr__(self):
        return self.__str__()
