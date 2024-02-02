from random import choice, randint, random, shuffle
from enum import Enum
from GravityActor import GravityActor
class ExtraHealth():


    def __init__(self, pos, time_to_live):
        
        self.time_to_live = time_to_live # Counts down to zero
        self.frame = 0
        self.gravityActor = GravityActor(pos)

    def collected(self, game):
        game.player.health = min(3, game.player.health + 1)
        game.play_sound("bonus")

    def update(self,game):
        #gravity
        self.gravityActor.update(game)


        #animation
        self.frame += 1
        anim_frame = str([0, 1, 2, 1][(self.frame // 6) % 4])
        self.image = "fruit" + 3 + anim_frame