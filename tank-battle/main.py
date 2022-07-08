import pygame
import sys
pygame.init()
tank = pygame.display.set_mode((640,560))
pygame.display.set_caption('坦克大战')
clock = pygame.time.Clock()
start=pygame.image.load(r"./s1.png")#按钮图片
def getTxt():
    front = pygame.font.SysFont("kaiti", 64)
    inf1 = "梦蝶酱!女装！"
    return front.render(inf1, 1, (255, 0, 255))
#from psutil import MACOS
from tank import*
step=0
star =False
edit =False
editClass =False
SETU = False
class EDITDITU(Base):
    def __init__(self):
        Base.__init__(self)
        self.image = pygame.image.load("img/steels.gif")
    def Postion(self):
        x,y = pygame.mouse.get_pos()
        return [x,y]
    def imageC(self,PD):
        if PD:
            self.image =pygame.image.load("img/p1tankD.gif")
        else :
            self.image =pygame.image.load("img/steels.gif")
class TUHUA(Base):
    def __init__(self,A):
        Base.__init__(self)
        self.image = pygame.image.load("img/steels.gif")
        self.R =[self.image.get_rect().width,self.image.get_rect().height]
        self.rect=None
        self.rect=pygame.Rect(A,self.R)
        self.XY = A
        self.C=0
    def Creat(self):
        return self.XY
class TUHUB(Base):
    def __init__(self,A):
        Base.__init__(self)
        self.C = 1;
        self.image = pygame.image.load("img/p1tankD.gif")
        self.R =[self.image.get_rect().width,self.image.get_rect().height]
        self.rect = pygame.Rect(A, self.R)
        self.rect=pygame.Rect(A,self.R)
        self.XY=A
    def Creat(self):
        return list(self.XY)

if __name__=="__main__":
    Editu =EDITDITU()

    TUHUAG =pygame.sprite.Group()
    tu = TUHUA([0,0])
    while True:
        GAME = MainGame()
        if(not(edit) and not(SETU)):
            x, y = pygame.mouse.get_pos()
            if (150 < x < 150 + 341 and 460 < y < 460 + 107):
                 pygame.draw.rect(tank,color=(255,0,0),rect=((130, 440, 380, 130)))
            else :
                 pygame.draw.rect(tank, color=(0, 0, 0), rect=((130, 440, 380, 130)))
            tank.blit(start, [150, 460])  # 放置开始按钮图片(后面再做个“按回车开始游戏图片换一下”）

        elif edit:
            tank.fill([0,0,0])
            tank.blit(Editu.image,Editu.Postion())
            TUHUAG.draw(tank)
        else:
            tank.fill([0, 0, 0])
            tank.blit(pygame.transform.scale(pygame.image.load("虫妈.jpg"),(345*2,216*2)), [0,0])
            tank.blit(getTxt(),[0,0])
        if(star and step<=640):
            pygame.draw.rect(tank, (192, 192, 192), (5, 200, 640, 20))
            pygame.draw.rect(tank, (0, 0, 255), (5,  200,  step, 20))
            step=step+1

        elif  star:
            for i in TUHUAG.sprites():
                if i.C == 1:
                    xy= i.Creat()
                    GAME.EnmyTanklisrcreat(xy)
                else:
                    xy = i.Creat()

                    GAME.WallCreat(xy)
            GAME.StarGame()
            star=False;
            step=0;
            tank = pygame.display.set_mode((640, 560))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if(not(star)):
                        edit = not(edit)
                    if(edit):
                        tank = pygame.display.set_mode((700, 500))
                    else :
                        tank = pygame.display.set_mode((640,560))
                if event.key ==pygame.K_p:
                    editClass=not(editClass)
                    Editu.imageC(editClass)
                if event.key == pygame.K_m:

                    if  not(edit):
                        SETU = not (SETU)
                        if SETU:
                            tank = pygame.display.set_mode((345*2,216*2))
                        else :
                            tank = pygame.display.set_mode((640, 560))

            if event.type ==MOUSEBUTTONDOWN:
                if editClass:
                    tu = TUHUB(pygame.mouse.get_pos())
                else:
                    tu =TUHUA(pygame.mouse.get_pos())
                if(not(edit)):
                    if(  150<x<150+341 and 460<y<460+107):
                        star =1;
                else:
                    x,y = pygame.mouse.get_pos()
                    if len(pygame.sprite.spritecollide(tu,TUHUAG,True))>0:
                        pass
                    else:
                        TUHUAG.add(tu)
        pygame.display.update()  # 刷新画面

