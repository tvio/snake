#kontrola kolize pro 2player , hned konec
# prepsat jen na jedny atributy p = p1+=p2, v=v1+v2
# udelat srazku s jidlemla player1 + player2, musim protahnout spravneho hada
# nejd mi udelat if pro setup2 ovladani hadd
# dat inicializaci do vlastniho file - spousta atributu a hadu, zeremisto 
# dat uvodniho hada na libovolne souradnice gridu
# spoj pro ruzne vypocty hlavu a vagony do jednoho pole
import pygame
#from watchpoints import watch
import random
import texty
from config import colors,window,windowClock
from sprites import grid, Vagon, Jidlo, Player


class Run(object):
    
    def __init__(self):
        self.Main()
        
    def reset(self):
       self.__init__()
    def nastavSmer(self,klavesa,player,smer):
       if klavesa=='left' and smer=='right':
          pass
       elif klavesa=='right' and smer=='left':
          pass
       elif klavesa=='up' and smer=='down':
          pass
       elif klavesa=='down' and smer=='up':
          pass
       else:
         if player==1:
          self.smer1=klavesa
          self.zasobnikSmeru1.append(klavesa)
         elif player==2:
          self.smer2=klavesa
          self.zasobnikSmeru2.append(klavesa)
    def randomColor(self):
        return random.choices(range(256), k=3)
    def Main(self):
        speed=5
        setup=2
        t=texty.texty()
        stopped = False
        self.smer1 = 'down'
        self.zasobnikSmeru1 = []
        vagony1 = []
        vagonPocet1 = 0
        if setup==2:
         self.smer2 = 'up'
         self.zasobnikSmeru2 = []
         vagony2 = []
         vagonPocet2 = 0
        #stejne atributy 
        uvodniDelka = 7
        score = 0
        #vsichni playeri a vagony
        #playeri s vagonama
        p,pv,p2v1v2,p1v1v2=[],[],[],[]
        #generovnai hlavy 1 
        player1 = Player(0,2,colors["blue"])
        if setup==2:
         player2 = Player(grid.sizex,grid.sizey-3,colors["green"])
        #generovani prvni  vagonu podle uvodni delky player1
        for i in (range (uvodniDelka)):
           vagonPocet1+=1
           vagony1.append( Vagon (vagonPocet1))
           if vagonPocet1==1:
            vagony1[i].nastavSouradnice(player1.gridx,player1.gridy,self.smer1)
           else:
            vagony1[i].nastavSouradnice(vagony1[i-1].gridx,vagony1[i-1].gridy,self.smer1)
        #if setup == 2:
        #    player1 = Player(0,2,colors["red"])
        #generovani prvni vagonu podle delky player2
        for i in (range (uvodniDelka)):
           vagonPocet2+=1
           vagony2.append( Vagon (vagonPocet2))
           if vagonPocet2==1:
            vagony2[i].nastavSouradnice(player2.gridx,player2.gridy,self.smer2)
           else:
            vagony2[i].nastavSouradnice(vagony2[i-1].gridx,vagony2[i-1].gridy,self.smer2)
        #jidlo = Jidlo(random.randint(0,g.sizex),random.randint(0,g.sizey),self.random_color(),vagony)
        if setup ==1:
         pv = vagony1
         pv.append(player1)
         jidlo = Jidlo(pv,self.randomColor())
        elif setup == 2:
           pv=vagony1+vagony2
           pv.append(player1)
           pv.append(player2)
           jidlo = Jidlo(pv,self.randomColor())
        wait = False
        #smyscka nepridat do poli 
        while stopped == False:
         window.fill(colors["white"])
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            elif event.type == pygame.KEYDOWN:
             
                  if len(self.zasobnikSmeru1) < 3:
                   if event.key == pygame.K_LEFT :      
                      self.nastavSmer('left',1,self.smer1)
                   if event.key == pygame.K_RIGHT  :
                      self.nastavSmer('right',1,self.smer1)
                   if event.key == pygame.K_UP :
                      self.nastavSmer('up',1,self.smer1)
                   if event.key == pygame.K_DOWN : 
                      self.nastavSmer('down',1,self.smer1)
               ## nejde mi if pro setup2 setup==2:
                  if len(self.zasobnikSmeru2) < 3:
                   if event.key == pygame.K_a :      
                      self.nastavSmer('left',2,self.smer2)
                   if event.key == pygame.K_d  :
                      self.nastavSmer('right',2,self.smer2)
                   if event.key == pygame.K_w :
                      self.nastavSmer('up',2,self.smer2)
                   if event.key == pygame.K_s : 
                     self.nastavSmer('down',2,self.smer2)
         #musim dat jen jednu klavesu z fronty zmacknutych  do pohybu, aby se nevyhodnotil crash         
         if len(self.zasobnikSmeru1)>0:
             self.smer1 = self.zasobnikSmeru1[0]
             del self.zasobnikSmeru1[0] 
         if setup==2:
          if len(self.zasobnikSmeru2)>0:
             self.smer2= self.zasobnikSmeru2[0]
             del self.zasobnikSmeru2[0] 
         ## kontrola kolize pro kazdeho playera, musim vedet komu pridat vagon 
         p=[]
         p.append(player1)
         if setup==2:
           p.append(player2)
         ## 1 - player1, 2 - player2, 3- nikdo
         jakyPlayerKolidoval = 3
         jakyPlayerKolidoval = jidlo.kontrolaKolize(p)
         if jakyPlayerKolidoval ==1: 
            score+=1
            vagonPocet1+=1
            vagony1.append( Vagon (vagonPocet1))
            speed+=0.5
            window.fill(colors["red"])
            del jidlo
            jidlo = Jidlo(pv,self.randomColor())
            if vagonPocet1 == 1 :
               vagony1[0].gridx=player1.gridx
               vagony1[0].gridy=player1.gridy
               vagony1[0].hgridx=player1.hgridx
               vagony1[0].hgridy=player1.hgridy
            else:
             wait = True
             pocetCekani = vagonPocet1
         if jakyPlayerKolidoval == 2:
            score+=1
            vagonPocet2+=1
            vagony2.append( Vagon (vagonPocet2))
            speed+=0.5
            window.fill(colors["red"])
            del jidlo
            # negenerovat jidlo do hada
            jidlo = Jidlo(pv,self.randomColor())
            # cekat na vykresleni, neni lepsi sjednotit atributy do jednhoo  a vyhodnocovat spolecne?
            # at nemusim psat vsechno pro kazdeho playera...
            if vagonPocet2 == 1 :
               vagony2[0].gridx=player1.gridx
               vagony2[0].gridy=player1.gridy
               vagony2[0].hgridx=player1.hgridx
               vagony2[0].hgridy=player1.hgridy
            else:
             wait = True
             pocetCekani = vagonPocet2
         else:
             window.fill(colors["white"])
         if wait:
          pocetCekani-=1
          if pocetCekani==0:
            if jakyPlayerKolidoval==1:
             vagony1[vagonPocet1-1].gridx=vagony1[len(vagony1)-2].gridx
             vagony1[vagonPocet1-1].gridy=vagony1[len(vagony1)-2].gridy
            elif jakyPlayerKolidoval==2:
             vagony2[vagonPocet1-1].gridx=vagony2[len(vagony2)-2].gridx
             vagony2[vagonPocet1-1].gridy=vagony2[len(vagony2)-2].gridy
            wait = False
         #check crash
         #check crash
         if setup==1:
          for i in range(len(vagony1)):
            if vagony1[i].gridx  == player1.gridx and vagony1[i].gridy == player1.gridy:
                t.gameOver() 
                stopped = True
                self.reset()
         #nejde kontrola kolize pro 2player, hned ukonci  
         elif setup==2:
           p2v1v2 = vagony2 + vagony1
           p2v1v2.append(player2)
           p1v1v2= vagony1 + vagony2
           p1v1v2.append(player1)
           for i in range(len(p2v1v2)-1):
             if player1.gridx == p2v1v2[i].gridx and player1.gridy == p2v1v2[i].gridy:
               t.gameOver() 
               stopped = True
               self.reset()
           for i in range(len(p1v1v2)-1):
              if player2.gridx ==  p1v1v2[i].gridx and player2.gridy == p1v1v2[i].gridy:
               t.gameOver() 
               stopped = True
               self.reset()        
                   
         player1.draw(player1.gridx,player1.gridy,self.smer1) 
         player2.draw(player2.gridx,player2.gridy,self.smer2) 
         v=vagony1+vagony2
         for i in range(len(v)):
          v[i].draw()            
         jidlo.drawJidlo()
         t.zobrazScore(score) 
         pygame.display.update()
         player1.gridx,player1.gridy,player1.hgridx,player1.hgridy = grid.automove(self.smer1,player1.gridx,player1.gridy)
         for i in reversed(range(len(vagony1))):
            if i == 0:
              vagony1[i].gridx = player1.hgridx
              vagony1[i].gridy = player1.hgridy
            else: 
              vagony1[i].aktualizujSouradnice(vagony1[i-1].gridx,vagony1[i-1].gridy)
         if setup==2:
          player2.gridx,player2.gridy,player2.hgridx,player2.hgridy = grid.automove(self.smer2,player2.gridx,player2.gridy)
          for i in reversed(range(len(vagony2))):
            if i == 0:
              vagony2[i].gridx = player2.hgridx
              vagony2[i].gridy = player2.hgridy
            else: 
              vagony2[i].aktualizujSouradnice(vagony2[i-1].gridx,vagony2[i-1].gridy)
        
             
         windowClock.tick(speed)

r = Run()
#while r.stopped == True:
#    del r
#    r = Run()

