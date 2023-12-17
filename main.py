# udelat srazku s jidlemla player1 + player2, musim protahnout spravneho hada
# dat inicializaci do vlastniho file - spousta atributu a hadu, zeremisto 
# dat uvodniho hada na libovolne souradnice gridu
# spoj pro ruzne vypocty hlavu a vagony do jednoho pole
import pygame
import random
import texty
from config import colors,window,windowClock,p1Control,p2Control
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
         self.smer1=klavesa
         self.zasobnikSmeru1.append(klavesa)
    def randomColor(self):
        return random.choices(range(256), k=3)
    def Main(self):
        setup=2
        t=texty.texty()
        stopped = False
        
        self.smer1 = 'down'
        smer1 = self.smer1
        self.zasobnikSmeru1 = []
        vagony1 = []
        vagonPocet1 = 0
        if setup==2:
         self.smer2 = 'up'
         smer2 = self.smer2
         self.zasobnikSmeru2 = []
         vagony2 = []
         vagonyPocet2 = 0
        #stejne atributy 
        uvodniDelka = 7
        score = 0
        speed=10
                
        #generovnai hlavy 1 
        player1 = Player(0,2,colors["red"])
        if setup==2:
         player2 = Player(grid.sizex,grid.sizey-3,colors["green"])
        #generovani prvni  vagonu podle uvodni delky player1
        for i in (range (uvodniDelka)):
           vagonPocet1+=1
           vagony.append( Vagon (vagonPocet1))
           if vagonPocet1==1:
            vagony1[i].nastavSouradnice(player1.gridx,player1.gridy,smer1)
           else:
            vagony1[i].nastavSouradnice(vagony1[i-1].gridx,vagony1[i-1].gridy,smer1)
        if setup == 2:
            player1 = Player(0,2,colors["red"])
        #generovani prvni vagonu podle delky player2
        for i in (range (uvodniDelka)):
           vagonPocet2+=1
           vagony2.append( Vagon (vagonPocet))
           if vagonPocet2==1:
            vagony2[i].nastavSouradnice(player2.gridx,player2.gridy,smer2)
           else:
            vagony2[i].nastavSouradnice(vagony2[i-1].gridx,vagony2[i-1].gridy,smer2)
        #jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color(),vagony)
        if setup ==1:
         pv = player1+vagony2
         jidlo = Jidlo(pv,self.randomColor())
        elif setup == 2:
           pv=player1+vagony1+player2+vagony2
           jidlo = Jidlo(pv,self.randomColor())
        wait = False
        
        while stopped == False:
         smer1= self.smer1
         if setup == 2:
            smer2 = self.smer2
         window.fill(colors["white"])
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            elif event.type == pygame.KEYDOWN:
             
                  if len(self.zasobnikSmeru1) < 3:
                   if event.key == pygame.K_LEFT :      
                      self.nastavSmer('left')
                   if event.key == pygame.K_RIGHT  :
                      self.nastavSmer('right')
                   if event.key == pygame.K_UP :
                      self.nastavSmer('up')
                   if event.key == pygame.K_DOWN : 
                      self.nastavSmer('down')
              if setup==2:
                  if len(self.zasobnikSmeru2) < 3:
                   if event.key == pygame.K_a :      
                      self.nastavSmer('left')
                   if event.key == pygame.K_d  :
                      self.nastavSmer('right')
                   if event.key == pygame.K_w :
                      self.nastavSmer('up')
                   if event.key == pygame.K_s : 
                     self.nastavSmer('down')
         #musim dat jen jednu klavesu z fronty zmacknutych  do pohybu, aby se nevyhodnotil crash         
         if len(self.zasobnikSmeru1>0:
             self.smer1 = self.zasobnikSmeru1[0]
             del self.zasobnikSmeru1[0] 
         if setup==2:
          if len(self.zasobnikSmeru2>0:
             self.smer2= self.zasobnikSmeru2[0]
             del self.zasobnikSmeru2[0] 
         if setup == 2:
         p = player1 + player2;
         else 
        
          
         if jidlo.kontrolaKolize(p.gridx,p.gridy)==1:
            score+=1
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
         t.zobrazScore(score) 
         pygame.display.update()
         player1.gridx,player1.gridy,player1.hgridx,player1.hgridy = grid.automove(smer,player1.gridx,player1.gridy)
         for i in reversed(range(len(vagony))):
            if i == 0:
              vagony[i].gridx = player1.hgridx
              vagony[i].gridy = player1.hgridy
            else: 
              vagony[i].aktualizujSouradnice(vagony[i-1].gridx,vagony[i-1].gridy)
         #zobrazScore
             
         windowClock.tick(speed)

r = Run()
while r.stopped == True:
    del r
    
    r = Run()

