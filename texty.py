from config import pygame,colors,window
import time
from sprites import grid
class texty():
     font = pygame.font.SysFont('times new roman', 50)      
     def gameOver(self):
       text = texty.font.render('Konec',True,colors["blue"])
       game_over_rect = text.get_rect()
       game_over_rect.midtop = grid.transform('souradnice',grid.sizex/2, grid.sizey/4)
       window.blit(text, game_over_rect)
       pygame.display.flip()
       time.sleep(2)
       
 
