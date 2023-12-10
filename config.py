import pygame
pygame.init()
height=30
width=30
windowW = 840
windowH = 600
colors = {"white":pygame.Color(255,255,255),"red":pygame.Color(255,0,0),"blue":pygame.Color(0, 0, 255),"green":pygame.Color(0, 255, 0),"black": pygame.Color(255, 255, 255)}
pygame.display.set_caption('Had')
windowClock = pygame.time.Clock()
window = pygame.display.set_mode((windowW,windowH))