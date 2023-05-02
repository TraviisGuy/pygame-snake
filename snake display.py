import pygame as py
import sys
import time

py.init()

screen_width = 640
screen_height = 480
screen = py.display.set_mode((screen_width, screen_height))

py.display.set_caption(("snake"))
bg_color = ('green')

running = True 
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

screen.fill(bg_color)
py.display.update()

py.display.flip()


py.quit()


