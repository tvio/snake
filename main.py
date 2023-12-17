
# storage na zmacknute klavesy nebo zpet na keypress nebo co to bylo?
#chyba pri rychlem sledu kl4aves to konci, i kdyz nenarazil2x
# udelat skore
# udelat new game
# dat text do vlastniho modulu
# dat uvodniho hada na libovolne souradnice gridu
# dat pryc sprites do vlastniho modulu
# spoj pro ruzne vypocty hlavu a vagony do jednoho pole
import pygame
import random
import texty
from config import colors,window,windowClock
from sprites import grid, Vagon, Jidlo, Player


class Run(object):
    
    def __init__(self):
        self.Main()
        
    def reset(self):
       self.__init__()
    def nastavSmer(self,klavesa):
       if klavesa=='left' and self.smer=='right':
          pass
       elif klavesa=='right' and self.smer=='left':
          pass
       elif klavesa=='up' and self.smer=='down':
          pass
       elif klavesa=='down' and self.smer=='up':
          pass
       else:
         self.smer=klavesa
         self.zasobnikSmeru.append(klavesa)
    def randomColor(self):
        return random.choices(range(256), k=3)
    def Main(self):
        t=texty.texty()
        stopped = False
        self.smer = 'down'
        smer = self.smer
        self.zasobnikSmeru = []
        
        speed=10
        vagonPocet = 0
        uvodniDelka = 7
        vagony = []
        #generovnai hlavy
        print(colors["red"])
        player1 = Player(0,2,colors["red"])
        #generovani prvni tri vagonu
        for i in (range (uvodniDelka)):
           vagonPocet+=1
           vagony.append( Vagon (vagonPocet))
           if vagonPocet==1:
            vagony[i].nastavSouradnice(player1.gridx,player1.gridy,smer)
           else:
            vagony[i].nastavSouradnice(vagony[i-1].gridx,vagony[i-1].gridy,smer)
        #jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color(),vagony)
        jidlo = Jidlo(player1.gridx,player1.gridy,vagony,self.randomColor())
        wait = False
        
        while stopped == False:
         smer = self.smer
         window.fill(colors["white"])
         
         for event in pygame.event.get():
          
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           
               
            elif event.type == pygame.KEYDOWN:
               if len(self.zasobnikSmeru) == 2:
                  break
               
               if event.key == pygame.K_LEFT :      
                  self.nastavSmer('left')
                  
               if event.key == pygame.K_RIGHT  :
                  self.nastavSmer('right')
                  
               if event.key == pygame.K_UP :
                  self.nastavSmer('up')
                  
               if event.key == pygame.K_DOWN : 
                  self.nastavSmer('down')
         #musim dat jen jednu klavesu z fronty zmacknutych  do pohybu, aby se nevyhodnotil crash         
         if len(self.zasobnikSmeru)>0:
             self.smer = self.zasobnikSmeru[0]
             del self.zasobnikSmeru[0] 
         print(self.smer)    
         if jidlo.kontrolaKolize(player1.gridx,player1.gridy)==1:
            vagonPocet+=1
            vagony.append( Vagon (vagonPocet))
            speed+=0.5
            print(speed)
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
         #check crash
         for i in range(len(vagony)):
            if vagony[i].gridx  == player1.gridx and vagony[i].gridy == player1.gridy:
                t.gameOver() 
                stopped = True
                self.reset()
         player1.draw(player1.gridx,player1.gridy,smer) 
         for i in range(len(vagony)):
          vagony[i].draw()            
         jidlo.drawJidlo()
         pygame.display.update()
         player1.gridx,player1.gridy,player1.hgridx,player1.hgridy = grid.automove(smer,player1.gridx,player1.gridy)
         for i in reversed(range(len(vagony))):
            if i == 0:
              vagony[i].gridx = player1.hgridx
              vagony[i].gridy = player1.hgridy
            else: 
              vagony[i].aktualizujSouradnice(vagony[i-1].gridx,vagony[i-1].gridy)
         windowClock.tick(speed)

r = Run()
while r.stopped == True:
    del r
    
    r = Run()

