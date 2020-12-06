import pygame as pg

pg.init()
width, height = 1080, 1080
image = pg.Surface((width, height))

image.fill((80, 80, 80))
pg.draw.circle(image, (184, 15, 10), (width/2, height/2), 100)

pg.image.save(image, 'test.png')