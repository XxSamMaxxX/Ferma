import pygame as p
import sys
from config import*

p.init()




while True:
    screen.fill(WHITE)

    keys = p.key.get_pressed()
    car.draw()
    player.draw(); player.move(keys); 
    

    if collide(player, car) and keys[p.K_e]: player.InCar = not player.InCar
    if player.InCar:
        player.speed = 10
        car.move(keys)
    else:
        player.speed = 5
        

#миша плохой саппорт.
        
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    p.display.flip()
    clock.tick(FPS)
