import heapq
import copy

priorityQueue = []

class queue:
    def __init__(self, team1:list, team2:list):# [playerob, playerobj]
        self.team1 = team1
        self.queue1HardCopy = []
        for players in team1:
            heapq.heappush(self.queue1HardCopy, (players.reactionSpeed, players.name)) 
        self.queue1 = copy.copy(self.queue1HardCopy)
        
        self.team2 = team2
        self.queue2HardCopy = [] 
        for players in team2:
            heapq.heappush(self.queue2HardCopy, (players.reactionSpeed, players.name)) 
        self.queue2 = copy.copy(self.queue2HardCopy) 
        
    def resetQueue(self):
        self.queue2 = copy.copy(self.queue2HardCopy)
        self.queue1 = copy.copy(self.queue1HardCopy)
        
        


heapq.heappush(priorityQueue, (-80, 'Oscar'))
heapq.heappush(priorityQueue, (-70, 'Yuxuan'))
heapq.heappush(priorityQueue, (-59, 'Eason'))

while priorityQueue:
    priority, task = heapq.heappop(priorityQueue)
    print(f"Processing {task} with priority {-priority}")
    