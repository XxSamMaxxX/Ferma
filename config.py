import pygame as p
from obj.player.script.player import*
from obj.car.script.car import*


#obj

player = players()
car = cars()

#display
FPS = 60
WIDTH, HEIGHT = 500, 500

screen = p.display.set_caption('моя игра')
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE)
clock = p.time.Clock()




#сolors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)