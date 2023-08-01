import pygame as p
import os, sys
from controller.behavior.behavior import*

sprite_name = 'car'
sprite_px = 32

current_dir = os.path.dirname(__file__)

img_dir = os.path.join(current_dir, '..', 'img')
player_image = p.image.load(os.path.join(img_dir, sprite_name +'.png'))


class cars(behaviors):
    def __init__(self):
        super().__init__()
        self.x, self.y = 100, 100
        self.image, self.rect = player_image, p.Rect(self.x, self.y, sprite_px, sprite_px)
        self.speed = 10


