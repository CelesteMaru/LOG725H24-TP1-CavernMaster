

from random import choice, randint, random, shuffle, randrange
from enum import Enum
import pygame, pgzero, pgzrun, sys
from Fruit import Fruit
from ExtraHealth import ExtraHealth
from ExtraLife import ExtraLife
from Pop import Pop

class CollectibleManagerSystem:
    def __init__(self):
        self.collectibles = []
        self.pops = []
    

    def collectibleDropOnEnenmyDeath(self, pos, trapped_enemy_type=0):
        time_to_live = 500
        
        # normal ennemy we drop a fruit
        if trapped_enemy_type == 0 : 
            self.collectibles.append(Fruit(pos, time_to_live))
        else:
            # If trapped_enemy_type is 1, it means this fruit came from bursting an orb containing the more dangerous type
            # of enemy. In this case there is a chance of getting an extra help or extra life power up
            # We create a list containing the possible types of fruit, in proportions based on the probability we want
            # each type of fruit to be chosen
            rand = randrange(0,20,1)
            # From 0 to 9
            if rand <= 10 :
                self.collectibles.append(Fruit(pos, time_to_live))
            # From 10 to 18
            elif rand <=18:
                self.collectibles.append(ExtraHealth(pos, time_to_live))
            else:
                self.collectibles.append(ExtraLife(pos, time_to_live))

    def timedFruitDrop(self):
        self.collectibles.append(Fruit((randint(70, 730), randint(75, 400))))
    
    def updateCollectibles(self, game):
        #Collectibles
        for c in self.collectibles:
            c.time_to_live-=1
            c.update(game)
            if game.player and game.player.collidepoint(c.center):
                c.collected(game)
                c.time_to_live = -1

            if c.time_to_live <= 0:
                self.pops.append(Pop(c.pos,0))
            

        #Pop animations
        for p in self.pops:
            p.update()
        
        #Clearing the arrays of dead entities
        self.collectibles = [c for c in self.collectibles if c.time_to_live > 0]
        self.pops = [p for p in self.pops if p.timer < 12]

    def collectiblesandpopLength(self):
        return len(self.collectibles + self.pops)
        
    def drawCollectiblesAndPops(self):
        for obj in self.pops + self.collectibles:
            if obj:
                obj.draw()