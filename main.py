# TODO negenerovat jidlo do ocasu
#chyba pri rychlem sledu kl4aves to konci, i kdyz nenarazil2x
# udelat skore
# udelat new game
# dat text do vlastniho modulu
# dat uvodniho hada na libovolne souradnice gridu
# dat pryc sprites do vlastniho modulu
# spoj pro ruzne vypocty hlavu a vagony do jednoho pole
import pygame
import random
import time

pygame.init()
height=30
width=30
windowW = 840
windowH = 600
#red = pygame.Color (255,0,0)
#blue = pygame.Color(0, 0, 255)
#green = pygame.Color(0, 255, 0)
#black = pygame.Color(0, 0, 0)
#white = pygame.Color(255, 255, 255)
colors = {"white":pygame.Color(255,255,255),"red":pygame.Color(255,0,0),"blue":pygame.Color(0, 0, 255),"green":pygame.Color(0, 255, 0),"black": pygame.Color(255, 255, 255)}
pygame.display.set_caption('Had')
windowClock = pygame.time.Clock()
window = pygame.display.set_mode((windowW,windowH))
class grid():
   gridx = 0
   gridy = 0
   sizex = windowW /width-1
   sizey = windowH/height-1
   @staticmethod
   def transform(kam,px,py):
    if kam=='grid':
      x = px/width
      y = py/height
      return (x,y)   
    elif kam=='souradnice':
      x = px*width
      y = py*height
      return (x,y)
   @staticmethod
   def draw(pgridx,pgridy,color):
     x,y = grid.transform('souradnice',pgridx,pgridy)
     pygame.draw.rect(window,color,pygame.Rect(x,y,width,height))
   #staticmethod
   @staticmethod
   def automove(smer,pgridx,pgridy):
       grid.gridx = pgridx
       grid.gridy = pgridy
       if smer == 'down':
          if pgridy==grid.sizey:
             grid.gridy=0
          else:
            grid.gridy +=1
       elif smer == 'up':
         if pgridy==0:
           grid.gridy = grid.sizey
         else:
          grid.gridy -=1
       elif smer == 'right':
         if pgridx == grid.sizex:
           grid.gridx=0;
         else:
            grid.gridx +=1 
       elif smer == 'left':
         if pgridx == 0:
            grid.gridx=grid.sizex;
         else:
           grid.gridx+=-1    
       return(grid.gridx,grid.gridy,pgridx,pgridy)
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
        grid.draw(self.gridx,self.gridy,self.color)
class Jidlo():
    def __init__(self,pgridx,pgridy,vagony,color):
         self.color= color
         kolize = True
         while kolize==True:
          kolize=False
          nastrelx =  random.randint(0,grid.sizex) 
          nastrely =  random.randint(0,grid.sizey) 
          if pgridx == nastrelx and pgridy == nastrely:
            kolize=True
            continue
          for i in range(len(vagony)):             
             if nastrelx == vagony[i].gridx and nastrely == vagony[i].gridy:
                kolize=True
         self.gridx = nastrelx
         self.gridy = nastrely
    def kontrolaKolize(self,gridx,gridy):
        if self.gridx == gridx and self.gridy == gridy:
          return 1
    def drawJidlo(self):
        grid.draw(self.gridx,self.gridy, self.color)
class Vagon():
   def __init__(self,cislo):
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
      grid.draw(self.gridx,self.gridy,colors["red"])
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
    speed=3
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
    def randomColor(self):
        return random.choices(range(256), k=3)
    def Main(self):
        stopped=False
        g = grid()
        vagonPocet = 0
        uvodniDelka = 2
        vagony = []
        #generovnai hlavy
        print(colors["red"])
        player1 = Player(0,2,colors["red"])
        #generovani prvni tri vagonu
        for i in (range (uvodniDelka)):
           vagonPocet+=1
           vagony.append( Vagon (vagonPocet))
           if vagonPocet==1:
            vagony[i].nastavSouradnice(player1.gridx,player1.gridy,Run.smer)
           else:
            vagony[i].nastavSouradnice(vagony[i-1].gridx,vagony[i-1].gridy,Run.smer)
        #jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color(),vagony)
        jidlo = Jidlo(player1.gridx,player1.gridy,vagony,self.randomColor())
        wait = False
        pocetCekani = 0
        while stopped == False:
         window.fill(colors["white"])
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT :      
                  self.nastavSmer('left')
                  break
               if event.key == pygame.K_RIGHT  :
                  self.nastavSmer('right')
                  break
               if event.key == pygame.K_UP :
                  self.nastavSmer('up')
                  break
               if event.key == pygame.K_DOWN : 
                  self.nastavSmer('down')
                  break
         if jidlo.kontrolaKolize(player1.gridx,player1.gridy)==1:
            vagonPocet+=1
            vagony.append( Vagon (vagonPocet))
            Run.speed+=0.5
            print(Run.speed)
            window.fill(colors["red"])
            del jidlo
            # negenerovat jidlo do hada
            jidlo = Jidlo(player1.gridx,player1.gridy,vagony, self.randomColor())
            if vagonPocet == 1 :
               vagony[0].gridx=player1.gridx
               vagony[0].gridy=player1.gridy
               vagony[0].hgridx=player1.hgridx
               vagony[0].hgridy=player1.hgridy
            else:
             wait = True
             pocetCekani = vagonPocet
         else:
             window.fill(colors["white"])
         if wait:
          pocetCekani-=1
          if pocetCekani==0:
            vagony[vagonPocet-1].gridx=vagony[len(vagony)-2].gridx
            vagony[vagonPocet-1].gridy=vagony[len(vagony)-2].gridy
            wait = False
         #check crash
         for i in range(len(vagony)):
            if vagony[i].gridx  == player1.gridx and vagony[i].gridy == player1.gridy:
               from texty import texty
               texty.gameOver(self) 
         player1.draw(player1.gridx,player1.gridy,Run.smer) 
         for i in range(len(vagony)):
          vagony[i].draw()            
         jidlo.drawJidlo()
         pygame.display.update()
         player1.gridx,player1.gridy,player1.hgridx,player1.hgridy = grid.automove(Run.smer,player1.gridx,player1.gridy)
         for i in reversed(range(len(vagony))):
            if i == 0:
              vagony[i].gridx = player1.hgridx
              vagony[i].gridy = player1.hgridy
            else: 
              vagony[i].aktualizujSouradnice(vagony[i-1].gridx,vagony[i-1].gridy)
         windowClock.tick(Run.speed)
Run()

