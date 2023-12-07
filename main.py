# zkusim primo pres spiretes classy, app  a dalsi
import pygame
import random
from array import *

pygame.init()
speed=4
height=60
width=60
windowW = 840
windowH = 600
white = (255,255,255)
red = (255,0,0)
pygame.display.set_caption('Had')
windowClock = pygame.time.Clock()
window = pygame.display.set_mode((windowW,windowH))
#font = pygame.font.Font('freesansbold.ttf', 32)

class grid():
   def __init__(self):
    self.sizex = windowW /width
    self.sizey = windowH/height 
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
    def draw(self,gridx,gridy,smer):
        self.gridx = gridx
        self.gridy = gridy
        grid.draw(self,self.gridx,self.gridy,self.color)
           
    
    def pridejVagon(self):
       self.delkaVlaku +=1 
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
   def __init__(self,gridx,gridy,cislo):
    super().__init__(gridx,gridy,cislo)
    self.cislo = cislo
    self.gridx = gridx
    self.gridy = gridy
    self.hgridx = gridx
    self.hgridy = gridy
   def nastavSouradnice(self,gridx,gridy,smer):
      
      self.gridx = gridx
      self.hgridx =  gridx
      self.gridy = gridy 
      self.hgridy= gridy
      if smer=='left':
         self.gridx+=1
         self.hgridx+=2
      elif smer=='right':
         self.gridx-=1 
         self.hgridy+=2       
      elif smer=='up':
         self.gridy+=1 
         self.hgridy+=2       
      elif smer=='down':
         self.gridy-=1   
         self.hgridy-=2      
      
   def draw(self):
      grid.draw(self,self.gridx,self.gridy,red)
   def aktualizujSouradnice(self,gridx,gridy):
      self.hgridx = self.gridx
      self.hgridy = self.gridy
      self.gridx = gridx
      self.gridy = gridy
class Run(object):
    stopped = False
    #x=0
    #y=0
    #presun na gird ze souracnic 1..size
    gx=0
    gy=0
    hgx=0
    hgy=0
    height=60
    width=60
    smer='down'
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
        return tuple(rgbl)
    def Main(self):
        stopped=False
        g = grid()
        vagonCislo = 0
        vagony = []
        player1 = Player(0,0,red)
        jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color())


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
                    
         if jidlo.kontrolaKolize(Run.gx,Run.gy)==1:
            player1.pridejVagon()
            vagonCislo+=1
            vagony.append( Vagon (Run.gx,Run.gy,vagonCislo))
            if vagonCislo == 1 :
            #pole vagonu zacina na 0 , odecist jedna od cislaVagonu
               vagony[0].nastavSouradnice(Run.gx,Run.gy,Run.smer)
            else:
               vagony[vagonCislo-1].nastavSouradnice(vagony[vagonCislo-2].gridx,vagony[vagonCislo-2].gridy,Run.smer)
           
            
             
            window.fill(red)
          
            del jidlo
            jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color())
         else:
            window.fill(white)
         
         
         
         Run.gx,Run.gy,Run.hgx,Run.hgy = g.automove(Run.smer,Run.gx,Run.gy)
         player1.draw(Run.gx,Run.gy,Run.smer) 

         for i in range(0,len(vagony)):
            
            if i == 0:
              vagony[i].gridx = Run.hgx
              vagony[i].gridy = Run.hgy
            else: 
              vagony[i].aktualizujSouradnice(vagony[i-1].hgridx,vagony[i-1].hgridy)
              
         for i in range(0,len(vagony)):
          vagony[i].draw()
         
       
         jidlo.drawJidlo()
         pygame.display.update()
         windowClock.tick(speed)
        

Run()

