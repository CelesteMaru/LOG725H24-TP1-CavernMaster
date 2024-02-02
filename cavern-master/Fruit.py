
from random import choice, randint, random, shuffle
from enum import Enum
import pygame, pgzero, pgzrun, sys
from GravityActor import GravityActor


# Class for pickups including fruit, extra health and extra life
class Fruit(GravityActor):
    APPLE = 0
    RASPBERRY = 1
    LEMON = 2

    def __init__(self, pos, time_to_live=500):
        super().__init__(pos)

        # Choose which type of fruit we're going to be.
        self.type = choice([Fruit.APPLE, Fruit.RASPBERRY, Fruit.LEMON])
        
        self.time_to_live = time_to_live # Counts down to zero
        self.frame = 0


    def collected(self, game):
        game.player.score += (self.type + 1) * 100
        game.play_sound("score")

    def update(self,game):
        #gravity
        super().update(game)


        #animation
        self.frame += 1
        anim_frame = str([0, 1, 2, 1][(self.frame // 6) % 4])
        self.image = "fruit" + str(self.type) + anim_frame
        