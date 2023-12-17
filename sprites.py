import random
from config import pygame,height,width,windowH,windowW,colors,window
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
    def __init__(self,pv,color):
         self.color= color
         kolize = True
         while kolize==True:
          kolize=False
          nastrelx =  random.randint(0,grid.sizex) 
          nastrely =  random.randint(0,grid.sizey) 
          for i in range(len(pv)):             
             if nastrelx == pv[i].gridx and nastrely == pv[i].gridy:
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