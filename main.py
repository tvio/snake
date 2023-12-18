# prepsat jen na jedny atributy p = p1+=p2, v=v1+v2
# udelat srazku s jidlemla player1 + player2, musim protahnout spravneho hada
# nejd mi udelat if pro setup2 ovladani hadd
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
         vagonPocet2 = 0
        #stejne atributy 
        uvodniDelka = 7
        score = 0
        speed=10
        #vsichni playeri a vagony
        pv=[]
        #playeri
        p=[]
        #generovnai hlavy 1 
        player1 = Player(0,2,colors["red"])
        if setup==2:
         player2 = Player(grid.sizex,grid.sizey-3,colors["green"])
        #generovani prvni  vagonu podle uvodni delky player1
        for i in (range (uvodniDelka)):
           vagonPocet1+=1
           vagony1.append( Vagon (vagonPocet1))
           if vagonPocet1==1:
            vagony1[i].nastavSouradnice(player1.gridx,player1.gridy,smer1)
           else:
            vagony1[i].nastavSouradnice(vagony1[i-1].gridx,vagony1[i-1].gridy,smer1)
        if setup == 2:
            player1 = Player(0,2,colors["red"])
        #generovani prvni vagonu podle delky player2
        for i in (range (uvodniDelka)):
           vagonPocet2+=1
           vagony2.append( Vagon (vagonPocet2))
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
               ## nejde mi if pro setup2 setup==2:
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
         if len(self.zasobnikSmeru1>0):
             self.smer1 = self.zasobnikSmeru1[0]
             del self.zasobnikSmeru1[0] 
         if setup==2:
          if len(self.zasobnikSmeru2)>0:
             self.smer2= self.zasobnikSmeru2[0]
             del self.zasobnikSmeru2[0] 
         if setup == 2:
          p = player1 + player2;
         else:
          p = player1
         ## kontrola kolize pro kazdeho playera, musim vedet komu pridat vagon 
         ## 1 - player1, 2 - player2, 3- nikdo
         jakyPlayerKolidoval = 0
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
            vagonyPocet2+=1
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
         p1v = player1+vagony1
         if setup==1:
          for i in range(len(vagony1)):
            if vagony1[i].gridx  == player1.gridx and vagony1[i].gridy == player1.gridy:
                t.gameOver() 
                stopped = True
                self.reset()

         elif setup==2:
           p2v = player2+vagony2
           p2v1v2 = p2v+vagony1
           p1v1v2 = p1v+vagony2
           for i in range(len(p2v1v2)):
             if player1.gridx ==  p2v1v2.gridx and player1.gridy == p2v1v2.gridy:
               t.gameOver() 
               stopped = True
               self.reset()
           for i in range(len(p1v1v2)):
              if player2.gridx ==  p1v1v2.gridx and player2.gridy == p1v1v2.gridy:
               t.gameOver() 
               stopped = True
               self.reset()        
                   
         player1.draw(player1.gridx,player1.gridy,smer1) 
         player2.draw(player1.gridx,player1.gridy,smer1) 
         v=vagony1+vagony2
         for i in range(len(v)):
          v[i].draw()            
         jidlo.drawJidlo()
         t.zobrazScore(score) 
         pygame.display.update()
         player1.gridx,player1.gridy,player1.hgridx,player1.hgridy = grid.automove(smer1,player1.gridx,player1.gridy)
         for i in reversed(range(len(vagony1))):
            if i == 0:
              vagony1[i].gridx = player1.hgridx
              vagony1[i].gridy = player1.hgridy
            else: 
              vagony1[i].aktualizujSouradnice(vagony1[i-1].gridx,vagony1[i-1].gridy)
         if setup==2:
          player2.gridx,player2.gridy,player2.hgridx,player2.hgridy = grid.automove(smer2,player2.gridx,player2.gridy)
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

