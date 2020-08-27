import numpy as np

class Card:
    def __init__(self, name, rank, attack, health):
        self.name = name
        self.rank = rank
        self.attack = attack
        self.health = health
        
        if self.health > 0:
            self.is_live = True
        else:
            self.is_live = False
        
    def accept_damage(self, attack):
        self.health -= attack
        
        if self.health > 0:
            self.is_live = True
        else:
            self.is_live = False
            
