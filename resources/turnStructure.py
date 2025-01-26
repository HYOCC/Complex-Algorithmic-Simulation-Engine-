import heapq
import copy

priorityQueue = []

class queue:
    def __init__(self, team1:list, team2:list):# [playerob, playerobj]
        self.team1 = team1
        self.minQueue1HardCopy = []
        self.maxQueue1HardCopy = []
        for players in team1:
            heapq.heappush(self.maxQueue1HardCopy, (-players.reactionSpeed, players))
            heapq.heappush(self.minQueue1HardCopy, (players.reactionSpeed, players)) 
        self.minQueue1 = copy.copy(self.minQueue1HardCopy)
        self.maxQueue1 = copy.copy(self.maxQueue1HardCopy)
        
        self.team2 = team2
        
        # for before each action such as hitting, whoever has the highest reaction speed goes last so they can base off other action
        self.minQueue2HardCopy = [] 
        
        # highest reaction speed goes first only if it beats the velocity of the ball speed as they have fast enough reaction speed to move to a spot after a ball is hit or do something instead of being on reaction speed
        self.maxQueue2HardCopy = []
        for players in team2:
            heapq.heappush(self.maxQueue2HardCopy, (-players.reactionSpeed, players))
            heapq.heappush(self.minQueue2HardCopy, (players.reactionSpeed, players)) 
        self.minQueue2 = copy.copy(self.minQueue2HardCopy) 
        self.maxQueue2 = copy.copy(self.maxQueue2HardCopy)
        
    def resetQueue(self):
        # resets queue base on lowest reaction speed
        self.queue2 = copy.copy(self.minQueue2HardCopy)
        self.queue1 = copy.copy(self.minQueue1HardCopy)
        
        # resets queue base on highest reaction speed
        self.maxQueue2 = copy.copy(self.maxQueue2HardCopy)
        self.maxQueue1 = copy.copy(self.maxQueue1HardCopy)
        
        


while priorityQueue:
    priority, task = heapq.heappop(priorityQueue)
    print(f"Processing {task} with priority {-priority}")
    