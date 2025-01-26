import heapq
import copy

class queue:
    def __init__(self, team:dict):# team: {playerObj:position}
        self.team = team
        self.minQueueHardCopy = []
        self.maxQueueHardCopy = []
        for player in team.keys():
            heapq.heappush(self.maxQueueHardCopy, (-player.reactionSpeed, player))
            heapq.heappush(self.minQueueHardCopy, (player.reactionSpeed, player)) 
        self.minQueue = copy.copy(self.minQueueHardCopy)
        self.maxQueue = copy.copy(self.maxQueueHardCopy)
    
    # gets highest reaction
    def getHighest(self):
        reactionSpeed, player = heapq.heappop(self.maxQueue)
        print(f'Reaction speed: {-reactionSpeed}, player: {player}')
        return -reactionSpeed, player
    
    # gets lowest reaction
    def getLowest(self):
        reactionSpeed, player = heapq.heappop(self.minQueue)
        print(f'Reaction speed: {reactionSpeed}, player: {player}')
        return reactionSpeed, player
    
    # resets the queue
    def resetQueue(self):
        self.minQueue = copy.copy(self.minQueueHardCopy)
        self.maxQueue = copy.copy(self.maxQueueHardCopy)
        
        
        



    