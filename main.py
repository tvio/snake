# TODO negenerovat jidlo do ocasu
# udelat skore
# udelat new game
# dat text do vlastniho modulu
import pygame
import random
import time
from array import *

pygame.init()
height=30
width=30
windowW = 840
windowH = 600
white = (255,255,255)
red = (255,0,0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
pygame.display.set_caption('Had')
windowClock = pygame.time.Clock()
window = pygame.display.set_mode((windowW,windowH))
#font = pygame.font.Font('freesansbold.ttf', 32)

class grid():
   def __init__(self):
    self.sizex = windowW /width-1
    self.sizey = windowH/height-1 
    self.gridx = 0
    self.gridy = 0
   def transform(self,kam,x,y):
    if kam=='grid':
      self.x = x/width
      self.y = y/height
      return (self.x,self.y)   
    elif kam=='souradnice':
      self.x = x*width
      self.y = y*height
      return (self.x,self.y)
   def draw(self,gridx,gridy,color):
     x,y = grid.transform(self,'souradnice',gridx,gridy)
     pygame.draw.rect(window,color,pygame.Rect(x,y,width,height))
   def automove(self,smer,gridx,gridy):
       if smer == 'down':
          if gridy==self.sizey:
             self.gridy=0
          else:
           self.gridy = gridy+1
       elif smer == 'up':
         if gridy==0:
           self.gridy = self.sizey
         else:
          self.gridy = gridy-1
       elif smer == 'right':
         if gridx == self.sizex:
            self.gridx=0;
         else:
            self.gridx = gridx+1 
       elif smer == 'left':
         if gridx == 0:
            self.gridx=self.sizex;
         else:
          self.gridx= gridx-1    
       return(self.gridx,self.gridy,gridx,gridy)
class Player(object):
    def __init__(self,gridx,gridy, color):
          self.gridx = gridx
          self.gridy = gridy
          self.color = color
          self.delkaVlaku = 1
          self.vagony = []
          self.hgridx = gridx
          self.hgridy = gridy-1
    def draw(self,gridx,gridy,smer):
        self.gridx = gridx
        self.gridy = gridy
        grid.draw(self,self.gridx,self.gridy,self.color)
class Jidlo(Player):
    def __init__(self,gridx,gridy,color):
             super().__init__(gridx,gridy,color) 
    def kontrolaKolize(self,gridx,gridy):
        if self.gridx == gridx and self.gridy == gridy:
          return 1
    def drawJidlo(self):
       #pygame.draw.rect(window,self.color,pygame.Rect(self.x,self.y,width,height))
        grid.draw(self,self.gridx,self.gridy, self.color) 
class Vagon(Jidlo):
   def __init__(self,cislo):
    #super().__init__(cislo)
    self.cislo = cislo
    self.gridx = 900
    self.gridy = 900
    self.hgridx = 900
    self.hgridy = 900
   def nastavSouradnice(self,gridx,gridy,smer):
      self.gridx = gridx
      self.gridy = gridy 
      if smer=='left':
         self.gridx+=1
      elif smer=='right':
         self.gridx-=1 
      elif smer=='up':
         self.gridy+=1         
      elif smer=='down':
         self.gridy-=1    
   def draw(self):
      grid.draw(self,self.gridx,self.gridy,red)
   def aktualizujSouradnice(self,gridx,gridy):
      self.hgridx = self.gridx
      self.hgridy = self.gridy
      self.gridx = gridx
      self.gridy = gridy
class Run(object):
    stopped = False
    height=60
    width=60
    smer='down'
    speed=7
    def __init__(self):
        self.Main()
    def nastavSmer(self,klavesa):
       if klavesa=='left' and Run.smer=='right':
          pass
       elif klavesa=='right' and Run.smer=='left':
          pass
       elif klavesa=='up' and Run.smer=='down':
          pass
       elif klavesa=='down' and Run.smer=='up':
          pass
       else:
          Run.smer=klavesa
    def random_color(self):
        rgbl=[255,0,0]
        random.shuffle(rgbl)
        while rgbl == [255,255,255]:
         random.shuffle(rgbl)
        #return tuple(rgbl)
        return random.choices(range(256), k=3)
    def game_over(self):
       my_font = pygame.font.SysFont('times new roman', 50)
       text = my_font.render('Konec',True,blue)
       game_over_rect = text.get_rect()
       game_over_rect.midtop = (windowW/2, windowH/4)
       window.blit(text, game_over_rect)
       pygame.display.flip()
       time.sleep(5)
       pygame.quit()
       quit()
    def Main(self):
        stopped=False
        g = grid()
        vagonPocet = 0
        uvodniDelka = 2
        vagony = []
        player1 = Player(0,2,red)
        for i in (range (uvodniDelka)):
           vagonPocet+=1
           vagony.append( Vagon (vagonPocet))
           if vagonPocet==1:
            vagony[i].nastavSouradnice(player1.gridx,player1.gridy,Run.smer)
           else:
            vagony[i].nastavSouradnice(vagony[i-1].gridx,vagony[i-1].gridy,Run.smer)
        jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color())
        wait = False
        pocetCekani = 0
        while stopped == False:
         window.fill(white)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT :      
                  self.nastavSmer('left')
               if event.key == pygame.K_RIGHT  :
                  self.nastavSmer('right')
               if event.key == pygame.K_UP :
                  self.nastavSmer('up')
               if event.key == pygame.K_DOWN : 
                  self.nastavSmer('down')
         if jidlo.kontrolaKolize(player1.gridx,player1.gridy)==1:
            vagonPocet+=1
            vagony.append( Vagon (vagonPocet))
            Run.speed+=0.5
            print(Run.speed)
            window.fill(red)
            del jidlo
            jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color())
            if vagonPocet == 1 :
               vagony[0].gridx=player1.gridx
               vagony[0].gridy=player1.gridy
               vagony[0].hgridx=player1.hgridx
               vagony[0].hgridy=player1.hgridy
            else:
             wait = True
             pocetCekani = vagonPocet
         else:
             window.fill(white)
         if wait:
          pocetCekani-=1
          if pocetCekani==0:
            vagony[vagonPocet-1].gridx=vagony[len(vagony)-2].gridx
            vagony[vagonPocet-1].gridy=vagony[len(vagony)-2].gridy
            wait = False
         #check crash
         for i in range(len(vagony)):
            if vagony[i].gridx  == player1.gridx and vagony[i].gridy == player1.gridy:
               self.game_over() 
         player1.draw(player1.gridx,player1.gridy,Run.smer) 
         for i in range(len(vagony)):
          vagony[i].draw()            
         jidlo.drawJidlo()
         pygame.display.update()
         player1.gridx,player1.gridy,player1.hgridx,player1.hgridy = g.automove(Run.smer,player1.gridx,player1.gridy)
         for i in reversed(range(len(vagony))):
            if i == 0:
              vagony[i].gridx = player1.hgridx
              vagony[i].gridy = player1.hgridy
            else: 
              vagony[i].aktualizujSouradnice(vagony[i-1].gridx,vagony[i-1].gridy)
         windowClock.tick(Run.speed)
Run()

