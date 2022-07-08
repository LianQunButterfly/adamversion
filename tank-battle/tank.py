
import sys
import pygame
import random#AI 关键模块
from pygame.locals import *
SCREEN_SIZE=[700,500]
BG_COLOR=[0,0,0]
FPS=45

class Base(pygame.sprite.Sprite):
    def __init__(self):
        # 调用父类（Sprite）的构建函数
        pygame.sprite.Sprite.__init__(self)
class MainGame():
    def __init__(self):
        pygame.init()
        windows=None
        self.my_Tank=Tank()
        self.psotion=[0,0,"N","N"]
        self.fpsClock=pygame.time.Clock()
        self.keylast=str()
        self.EConut=6;
        self.EnmyTanklsit=pygame.sprite.Group()
        self.contT=10;
        self.li = [Animation()]
        self.WallGroup = pygame.sprite.Group()
        self.stop = 0;

    def StarGame(self):
        MainGame.windows=pygame.display.set_mode(SCREEN_SIZE)
        print(type(MainGame.windows))
        pygame.display.set_caption("坦克大战")
        self.MYEVENT01=pygame.USEREVENT +1
        pygame.time.set_timer(self.MYEVENT01, 500)
        #self.EnmyTanklisrcreat()
        while True:
            if(self.stop):
                return
            MainGame.windows.fill(BG_COLOR)
            if(len(self.WallGroup.sprites())>0):
                self.WallGroup.draw(MainGame.windows)
            self.EventPross()
            self.EnmyTanklsit.update("M", self.my_Tank,self.WallGroup)
            #self.EnmyTanklsit.draw(MainGame.windows)
            MainGame.windows.blit(self.getTxt(),(0,0))
            self.li[0].display()#
            self.li[0].dAmimation()
            if self.my_Tank.live>=0:
                self.my_Tank.hitTank(self.EnmyTanklsit)
                self.my_Tank.display(self.WallGroup)
            pygame.display.update()
            self.fpsClock.tick(FPS)
    def EnmyTanklisrcreat(self,A):
        self.EnmyTanklsit.add(EnmyTank(self.li,A))
    def WallCreat(self,A):
        self.WallGroup.add(Wall(A[0],A[1],self.WallGroup))
    def EndGame(self):
        pygame.quit()
        sys.exit()
    def EventPross(self):
        self.eventlist =pygame.event.get()
        for event in self.eventlist:
            if event.type==QUIT:
                self.EndGame()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    self.psotion=[-1,0,"R"]
                    self.keylast="A"
                elif event.key==pygame.K_d:
                    self.psotion=[1, 0, "L"]
                    self.keylast="D"
                elif event.key==pygame.K_w:
                    self.psotion=[0, -1, "U"]
                    self.keylast="W"
                elif event.key==pygame.K_s:
                    self.psotion=[0, 1, "D"]
                    self.keylast="S"
                elif event.key ==pygame.K_m:
                    self.stop=1;
                    print(self.stop)
            elif event.type==KEYUP:
                if event.key == pygame.K_a:
                    if self.keylast == "A":
                        self.psotion=[0,0,"N"]
                elif event.key == pygame.K_d:
                    if self.keylast == "D":
                        self.psotion = [0, 0, "N"]
                elif event.key == pygame.K_w:
                    if self.keylast == "W":
                        self.psotion = [0, 0, "N"]
                elif event.key == pygame.K_s:
                    if self.keylast == "S":
                        self.psotion = [0, 0, "N"]
                elif event.key ==pygame.K_SPACE:
                        self.my_Tank.Fire()
            elif event.type ==self.MYEVENT01:
                if self.my_Tank.live>=0:
                    self.my_Tank.Genxin()
                # for i in self.EnmyTanklsit:
                #     i.set_move()
                self.contT=self.contT+1
                self.li[0].displayChage()
                self.li[0].dAmimation()
                if((self.contT) %2 == 0):
                    self.EnmyTanklsit.update("S", self.my_Tank,self.WallGroup)
                if self.contT%4==0:
                    self.EnmyTanklsit.update("F", self.my_Tank,self.WallGroup)
                if self.contT >=20:
                    self.contT=0
        if self.my_Tank.live >= 0:
            self.my_Tank.control(self.psotion,self.WallGroup)
        # for i in self.EnmyTanklsit:
        #     i.move()
        #     self.my_Tank.Genxin()


    def getTxt(self):
        front = pygame.font.SysFont("kaiti",16)
        inf1 ="我方坦克生命:"+str(self.my_Tank.live)
        return front.render(inf1,1,(0,255,0))
class Tank(Base):
    live=999999
    def __init__(self):
        self.Postion=list()
        self.Rotation=str()
        self.imges={
            "U":pygame.transform.scale(pygame.image.load("newSucai/up.gif"),(60,60)),
            "D":pygame.transform.scale(pygame.image.load("newSucai/down.gif"),(60,60)),
            "L":pygame.transform.scale(pygame.image.load("newSucai/right.gif"),(60,60)),
            "R":pygame.transform.scale(pygame.image.load("newSucai/left.gif"),(60,60)),
        }
        self.Rotation="U"
        self.imge = self.imges[self.Rotation]
        self.rect = self.imge.get_rect()
        self.rect.left, self.rect.top = map(lambda i: int(i) / 2, SCREEN_SIZE)
        self.speedx=0;
        self.speedy=0;
        self.Fcs=FCS()
    def display(self,WL):
        self.imge = self.imges[self.Rotation]
        self.Fcs.move(WL)
        self.Fcs.display()
        MainGame.windows.blit(self.imge,self.rect)
    def Fire(self):
        self.Fcs.creat([self.Rotation, self.rect.centerx, self.rect.centery])
        music=Music('img/fashe.mp3')
        music.play()
    def Genxin(self):
        self.Fcs.GEnxin()
    def hitTank(self,Elistt):
        self.Fcs.hiting(Elistt)


    def deleteFCS(selfs,i):
        pass
    def control(self,Postion,WL):
        if Postion[2] == "N":
            self.speedx=0
            self.speedy=0
            return
        pd=lambda i:i if abs(i)<5 else i/abs(i)*5
        if Postion[2] in ["U","D"]:
            self.speedy=pd(self.speedy+Postion[1]*2)
            self.speedx=0
        elif Postion[2] in ["R","L"]:
            self.speedx=pd(self.speedx+Postion[0]*5)
            self.speedy=0
        if  0< self.rect.left +self.speedx<SCREEN_SIZE[0]-60 and 0< self.rect.top +self.speedy<SCREEN_SIZE[1]-60:
            self.rect.left += self.speedx
            self.rect.top +=  self.speedy
            a = pygame.sprite.spritecollide(self, WL, False)
            if len(a) > 0:
                self.rect.left -= self.speedx
                self.rect.top -= self.speedy
        self.Fcs.move(WL)
        if Postion[2] != "N":
            self.Rotation = Postion[2]
    def FSCLIST(self):
        return self.Fcs.FCSLIST();
    def died(self):
        self.rect.left ,self.rect.top = 1000,1000

"""单个敌方坦克
2，血量
3，动作 移动和发射
"""
class EnmyTank(Base):

    def __init__(self,A,PO):
        self.AmPostion=A
        Base.__init__(self)
        self.RotationList =["U","D","L","R","N"]
        self.imges = {
            "U": pygame.transform.scale(pygame.image.load("img/p1tankU.gif"), (60, 60)),
            "D": pygame.transform.scale(pygame.image.load("img/p1tankD.gif"), (60, 60)),
            "L": pygame.transform.scale(pygame.image.load("img/p1tankL.gif"), (60, 60)),
            "R": pygame.transform.scale(pygame.image.load("img/p1tankR.gif"), (60, 60)),
        }
        self.Rotation=self.RotationList[random.randint(0,3)]
        self.image = self.imges[self.Rotation]
        self.rect = self.image.get_rect()
        self.speedx,self.speedy=10,10
        self.xy=0
        self.live=1
        self.control=0
        self.Postion=[0,0,"N"]
        self.Fcs =FCS()
        self.rect.top,self.rect.left=PO[1],PO[0]
    def update(self,A,B,WL):
        self.Fcs.hiting1(B)
        if A=="M":
            EnmyTank.move(self,WL)
            self.imge = self.imges[self.Rotation]
            self.Fcs.move(WL)
            self.Fcs.display()

            MainGame.windows.blit(self.imge, self.rect)
        elif A=="S":
            EnmyTank.set_move(self)
        elif A=="F":
            self.Fcs.creat([self.Rotation, self.rect.centerx, self.rect.centery])
            self.Fcs.GEnxin()
    def hitTank(self,A,WL):
        self.Fcs.hiting1(A,WL)


    def set_move(self):
        self.xy = random.randint(0, 1)
        self.PM = random.choice([-1, 1])
        self.Postion[self.xy] = 1 * self.PM
        self.Postion[2] = self.RotationList[random.randint(0, 4)]
        if self.Postion[2] != "N":
            self.image=self.imges[self.Postion[2]]
    def move(self,WL):

        if self.Postion[2] == "N":
            self.speedx = 0
            self.speedy = 0
            return
        pd = lambda i: i if abs(i) < 5 else i / abs(i) * 5
        if self.Postion[2] in ["U", "D"]:
            self.speedy = pd(self.speedy + self.Postion[1] * 2)
            self.speedx = 0
        elif self.Postion[2] in ["R", "L"]:
            self.speedx = pd(self.speedx + self.Postion[0] * 5)
            self.speedy = 0

        if 0 < self.rect.left + self.speedx < SCREEN_SIZE[0] - 60 and 0 < self.rect.top + self.speedy < SCREEN_SIZE[
            1] - 60:
            self.rect.left += self.speedx
            self.rect.top += self.speedy
            a = pygame.sprite.spritecollide(self, WL, False)
            if len(a) > 0:
                self.rect.left -= self.speedx
                self.rect.top -= self.speedy
        if self.Postion[2] != "N":
            self.Rotation = self.Postion[2]
    def __del__(self):

        self.AmPostion[0].add(self.rect)


class ZIDAN(Base):
    def __init__(self,a,b,imge,kyidong,Img):
        Base.__init__(self)
        self.image = Img
        self.rect=imge.get_rect()
        self.rect.centerx =  a
        self.rect.centery =  b
        self.speed = 10;
        self.k = kyidong
    def update (self,Group,WL):

        self.rect.centerx += self.speed * self.k[0]
        self.rect.centery += self.speed * self.k[1]
        a=pygame.sprite.spritecollide(self,WL,False)
        if not (-10 < self.rect.centerx < 710) or not (-10 < self.rect.centery < 510) or len(a)>0:
            for i in a:
                 i.DELT()
            Group.remove(self)

        else:
            return True
    def returnImge(self):
        return self.Imge
    def delete(self):
        pass
    def Rect(self):
        return self.rect
class FCS(Base):
    def __init__(self):
        self.RotationList = ["U", "D", "L", "R"]
        self.imges = {
            "U":pygame.image.load("img/enemymissile.gif"),
            "D":pygame.image.load("img/enemymissile.gif"),
            "R":pygame.image.load("img/enemymissile.gif"),
            "L":pygame.image.load("img/enemymissile.gif")
        }
        self.imgeList=pygame.sprite.Group()
        self.cont=0
        self.speed=12
    def GEnxin(self):
        self.cont=0;
    def creat(self,R):
        if self.cont>=3:
            return
        else:
            a=self.imges[R[0]]
          #  r = self.imges[R[0]].get_rect()
           # r.centerx,r.centery=R[1],R[2]
            if R[0]=="U":
                k=[0,-1]
            elif R[0]=="D":
                k=[0,1]
            elif R[0]=="R":
               k=[-1,0]
            elif R[0]=="L":
                k=[1,0]
            self.cont=self.cont+1
            a=ZIDAN(R[1],R[2],self.imges[R[0]],k,a)
            self.imgeList.add(a)


    def move(self,WL):

        self.imgeList.update(self.imgeList,WL)
    def hiting(self,Elist):

        pygame.sprite.groupcollide(Elist,self.imgeList,True,True)

    def hiting1(self,A):
        a=pygame.sprite.spritecollide(A,self.imgeList,True)
        if len(a)>0:
            A.live=A.live-1
            if(A.live<0):
                A.died()


    def display(self):
        self.imgeList.draw(MainGame.windows)
class Wall(Base):
    # 这里需要接受walllist里的参数
    def __init__(self,left,top,WL):
        Base.__init__(self)
        self.image=pygame.image.load("img/steels.gif")
        self.rect=self.image.get_rect()
        self.rect.top=top
        self.rect.left=left
        self.hp=20
        self.live=True
        self.P = [WL]
    def DELT(self):
        self.hp = self.hp -1
        if self.hp<0:
            self.P[0].remove(self)
class Music():
    def __init__(self,filename):
        self.filename=filename
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(self.filename)
        #播放音乐
    def play(self):
        pygame.mixer.music.play()
        pass
class Animation(Base):
    def __init__(self):
        self.object = [ pygame.image.load("img/blast0.gif"),
                        pygame.image.load("img/blast1.gif"),
                        pygame.image.load("img/blast2.gif"),
                        pygame.image.load("img/blast3.gif"),
                        pygame.image.load("img/blast4.gif")
        ]
        self.ti = []
        self.Postion= []
    def add(self,P):
        self.Postion.append([P,0])
        music=Music('img/bong.mp3')
        music.play()
    def dAmimation(self):
        for i in self.Postion:
            if i[1] >=4:
                self.Postion.remove(i)

    def displayChage(self):
        for i in self.Postion:
            i[1]=i[1]+1
    def display(self):
            for i in self.Postion:
                MainGame.windows.blit(self.object[i[1]], i[0])
class Skill():
    def __init__(self):
        pass
if __name__=="__main__":
  pass