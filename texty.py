class texty():
     def gameOver(self):
       from main import pygame,colors,grid,time,window
       my_font = pygame.font.SysFont('times new roman', 50)
       text = my_font.render('Konec',True,colors["blue"])
       game_over_rect = text.get_rect()
       game_over_rect.midtop = grid.transform('souradnice',grid.sizex/2, grid.sizey/4)
       window.blit(text, game_over_rect)
       pygame.display.flip()
       time.sleep(5)
       pygame.quit()
       quit()