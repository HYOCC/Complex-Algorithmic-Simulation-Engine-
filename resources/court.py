import resources.player as player
from resources.turnStructure import queue
import copy

class court():
    def __init__(self, players:dict):# players: {playerObj:position} 
        
        self.court = [[[] for _ in range(9)] for _ in range(6)]
        self.courtCopy = [[[] for _ in range(9)] for _ in range(6)]
        
        self.hMap = {}
        self.hMapCopy = {}
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        # [],[],[]  [],[],[]  [],[],[] 
        
        for key, value in players.items():
            if value == 'OH' and not(self.court[0][4]): 
                self.court[0][4], self.courtCopy[0][4] = [key], [key]
                self.hMap[key] = {'gSpot': 0, 'sSpot': 4}
                self.hMapCopy[key] = {'gSpot': 0, 'sSpot': 4}
            elif value == 'OH':
                self.court[5][4], self.courtCopy[5][4] = [key], [key]
                self.hMap[key] = {'gSpot': 5, 'sSpot': 4}
                self.hMapCopy[key] = {'gSpot': 5, 'sSpot': 4}
            elif value == 'S':
                self.court[2][4], self.courtCopy[2][4] = [key], [key]
                self.hMap[key] = {'gSpot': 2, 'sSpot': 4}
                self.hMapCopy[key] = {'gSpot': 2, 'sSpot': 4}
            elif value == 'L':
                self.court[4][4], self.courtCopy[4][4] = [key], [key]
                self.hMap[key] = {'gSpot': 4, 'sSpot': 4}
                self.hMapCopy[key] = {'gSpot': 4, 'sSpot': 4}
            elif value == 'RH':
                self.court[3][4], self.courtCopy[3][4] = [key], [key]
                self.hMap[key] = {'gSpot': 3, 'sSpot': 4}
                self.hMapCopy[key] = {'gSpot': 3, 'sSpot': 4}
            else:
                self.court[1][4], self.courtCopy[1][4] = [key], [key]
                self.hMap[key] = {'gSpot': 1, 'sSpot': 4}
                self.hMapCopy[key] = {'gSpot': 1, 'sSpot': 4}
                        
        self.queue = queue(players)

    def printCourtState(self):
        
        # Function to process a specific range of rows and columns
        def process_range(start_row, end_row, row_start, row_end):
            result = ""
            for i in range(start_row, end_row):
                for j in range(row_start, row_end):
                    if not self.court[i][j]:
                        result += '[\'  \']'
                    else:
                        result += f'[{str(self.court[i][j][0])[0:4]}]'
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
    
    def getCourt(self):
        return self.court
    
    def movePlayer(self, player:player, spot:dict):# spot = {'gSpot':int, 'sSpot':int}
        
        # removing from current spot
        currentGSpot = self.hMap[player]['gSpot']
        currentSSpot = self.hMap[player]['sSpot']
        self.court[currentGSpot][currentSSpot].pop()
        
        # moves the player to the new spot
        self.hMap[player]['gSpot'] = spot['gSpot'] - 1
        self.hMap[player]['sSpot'] = spot['sSpot'] - 1
        self.court[spot['gSpot'] - 1][spot['sSpot'] - 1].append(player)
        self.printCourtState()
        return True # work in progress to check player stat if it actually is a successful movement
    
    def swapPlayer(self, player1:player, player2:player):
        # data holder
        player1Spot = self.GetPlayerPOS(player1)
        player2Spot = self.GetPlayerPOS(player2)
        
        self.court[player1Spot['gSpot']][player1Spot['sSpot']], self.experimental[player2Spot['gSpot']][player2Spot['sSpot']] = self.experimental[player2Spot['gSpot']][player2Spot['sSpot']], self.experimental[player1Spot['gSpot']][player1Spot['sSpot']]
        self.hMap[player1] = player2Spot
        self.hMap[player2] = player1Spot
        
        
    def getPlayerPOS(self, player:player):
        return self.hMap[player]
    
    # resets the court to original position
    def resetCourt(self):
        self.court = self.courtCopy
        self.hMap = self.hMapCopy
    
    # gets the highest reaction speed of all the characters
    def getHighest(self):
        return self.queue.getHighest()
    
    # if the queue is empty for the highest reaction
    def checkHighest(self):
        return self.queue.checkHighestEmpty()
    
    # gets the lowest reaction speed character
    def getLowest(self):
        return self.queue.getLowest()
    
    # if the queue is empty for the lowest reaction
    def checkLowest(self):
        return self.queue.checkLowestEmpty()
    
    def resetQueue(self):
        self.queue.resetQueue()
    
    def __str__(self):
        return self.court

    def __repr__(self):
        return self.__str__()
