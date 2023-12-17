from config import pygame,colors,window
import time
from sprites import grid
class texty():
     
     def gameOver(self):
       font = pygame.font.SysFont('monospace', 50)      
       text = font.render('Konec',True,colors["blue"])
       gameOverRect = text.get_rect()
       gameOverRect.midtop = grid.transform('souradnice',grid.sizex/2, grid.sizey/4)
       window.blit(text, gameOverRect)
       pygame.display.flip()
       time.sleep(2)
     def zobrazScore(self,score):
       font = pygame.font.SysFont('mnospace', 35)      
       text = font.render('Body : '+ str(score),True,colors["blue"])
       scoreRect = text.get_rect()
       scoreRect.topleft = grid.transform('souradnice',grid.sizex-3,0)
       window.blit(text,scoreRect)

       
 
