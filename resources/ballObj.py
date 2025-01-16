class ball():
    def __init__(self):
        self.attributes = {'difficulty': 0}
        self.state = 'none'

    
    def increaseDifficulty(self, amount):
        self.attributes['difficulty'] += amount
        print(f'current ball difficulty: {self.attributes['difficulty']}')
    
    def decreaseDifficulty(self, amount):
        self.attributes['difficulty'] -= amount
        print(f'current ball difficulty: {self.attributes['difficulty']}')