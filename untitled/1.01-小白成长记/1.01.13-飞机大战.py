import pygame
import time
import random
from pygame.locals import *

'''
1. 
'''
class BasePlane(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x =x
        self.y =y
        self.screen =screen_temp
        self.image =pygame.image.load(image_name)
        self.bullet_list =[]    #存储发射出去的子弹对象的引用

        # 爆炸效果用的如下属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_list = []  # 用来存储爆炸时需要的图片
     #   self.crate_images()  # 调用这个方法向bomb_list中添加图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号

    def crate_images(self,image1,image2,image3,image4):
        self.bomb_list.append(pygame.image.load(image1))
        self.bomb_list.append(pygame.image.load(image2))
        self.bomb_list.append(pygame.image.load(image3))
        self.bomb_list.append(pygame.image.load(image4))

    def displane(self,hero,enemy,bullet):
        '''显示飞机对象'''

        #如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num+=1
            if self.image_num == 10:
                self.image_num=0
                self.image_index+=1
            if self.image_index>3:
                time.sleep(2)
                exit()#调用exit让游戏退出
                #self.image_index = 0
        else:
            self.screen.blit(self.image,(self.x, self.y))

        #不管玩家飞机是否被击中,都要显示发射出去的子弹
        for bullet in self.bullet_list:
            bullet.disbullet()
            bullet.move()

            if bullet.judge():   #判断子弹是否越界 坑1.01-列表移数
                self.bullet_list.remove(bullet)

            #我方子弹打中敌机，敌机爆炸
            if ((bullet.x > enemy.x and bullet.x < enemy.x + 50) and (bullet.y < enemy.y+ 10)):
                enemy.bomb()
            #敌人子弹打中我方飞机，我方爆炸
            elif ((bullet.x > hero.x and bullet.x < hero.x+50) and (bullet.y > hero.y)and(bullet.y<hero.y+50)):
                hero.bomb()

    def bomb(self):
        self.hit = True
class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self, screen_temp, 230, 520, './feiji/hero1_small.png')
        image1 ='./feiji/hero_blowup_n1_small.png'
        image2  ='./feiji/hero_blowup_n2_small.png'
        image3  ='./feiji/hero_blowup_n3_small.png'
        image4  ='./feiji/hero_blowup_n4_small.png'
        self.crate_images(image1,image2,image3,image4)  # 调用这个方法向bomb_list中添加图片
    def move_left(self):
        '''左移动'''
        self.x -=10

    def move_right(self):
        '''右移动'''
        self.x +=10

    def fire(self,count):
        '''开火'''
        if count<=10:
            self.bullet_list.append(Bullet(self.screen,self.x,self.y))
        else:
            self.bullet_list.append(Bullet_type1(self.screen,self.x,self.y))
class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,0,0,'./feiji/enemy0.png')
        self.flage =True
        image1 ='./feiji/enemy0_down1.png'
        image2  ='./feiji/enemy0_down2.png'
        image3  ='./feiji/enemy0_down3.png'
        image4  ='./feiji/enemy0_down4.png'
        self.crate_images(image1,image2,image3,image4)  # 调用这个方法向bomb_list中添加图片

    def  move(self):
        if self.flage:
            self.x +=5
        else:
            self.x -=5

        if self.x<0:
            self.flage =True
        elif self.x>430:
            self.flage =False


    def fire(self):
        '''开火'''
        random_num1 =random.randint(1,10)
        random_num2 = random.randint(1,10)
        if random_num1 ==5 and random_num2 ==5:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
#子弹
class BaseBullet(object):
    def __init__(self,screen_temp,hero_x_temp,hero_y_temp,image_name):
        self.x =hero_x_temp
        self.y =hero_y_temp
        self.screen =screen_temp
        self.image  =pygame.image.load(image_name)
    def disbullet(self):
        '''显示子弹'''
        self.screen.blit(self.image,(self.x,self.y))
class Bullet(BaseBullet):
    '''创建子弹类'''
    def __init__(self,screen_temp,hero_x_temp,hero_y_temp):
        BaseBullet.__init__(self,screen_temp,hero_x_temp+15,hero_y_temp-15,'./feiji/bullet.png')

    def judge(self):
        if self.y<0:
            return True
        else:
            return  False

    def move(self):
        self.y  -=7
class EnemyBullet(BaseBullet):
    '''创建敌机子弹'''
    def __init__(self,screen_temp,hero_x_temp,hero_y_temp):
        BaseBullet.__init__(self,screen_temp,hero_x_temp +20,hero_y_temp +35,'./feiji/bullet1.png')

    def judge(self):
        if self.y >600:
            return True
        else:
            return False

    def move(self):
        '''敌机子弹移速'''
        self.y += 3

#子弹的另一种类型
class Bullet_type1(Bullet):
    def __init__(self,screen_temp,hero_x_temp,hero_y_temp):
        self.x =hero_x_temp +15
        self.y =hero_y_temp -15
        self.x1 =hero_x_temp -2
        self.y1 =hero_y_temp+5
        self.x2 = hero_x_temp - 2
        self.y2 = hero_y_temp + 5
        self.screen = screen_temp
        self.image  =pygame.image.load('./feiji/bullet.png')

    def disbullet(self):
        '''显示子弹'''
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image, (self.x1, self.y1))
        self.screen.blit(self.image, (self.x2 + 33, self.y2))

    def move(self):
        self.y  -=7
        self.x1 -=2
        self.y1 -=7
        self.x2 +=2
        self.y2 -=7
def  key_control(hero_temp,enemy_temp):
    global count
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是按a或者left
            if event.key == K_a or event.key == K_LEFT:
                #print('left')
                hero_temp.move_left()

                # 检测按键是否死d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                #print('right')
                hero_temp.move_right()

            # 检测按键是否是空格
            elif event.key == K_SPACE:
                #print('space')
                #count +=1
                hero_temp.fire(count)
            elif event.key == K_b  :
                #print('b')
                enemy_temp.bomb()

def main():
    #1.创建一个窗口d
    screen = pygame.display.set_mode((480,600),0,32)

    #2.创建背景图片
    background = pygame.image.load("./feiji/background.png")

    #3.创建一个飞机对象
    hero =HeroPlane(screen)
    #5.创建敌机对象
    enemy =EnemyPlane(screen)

    #4.创建一个子弹对象
    bullet =Bullet(screen,hero.x,hero.y)
    bullet1 = Bullet_type1(screen, hero.x, hero.y)
    enemybullet =EnemyBullet(screen,enemy.x,enemy.y)

    t1 =time.time()
    print(t1)
    while True:

        #设置需要显示的背景图
        screen.blit(background,(0,0))
        #显示飞机
        hero.displane(hero,enemy,bullet)
        enemy.displane(hero,enemy,enemybullet)
        enemy.move()
        enemy.fire()
        #测试子弹位置
        #bullet.disbullet()
        #获取事件，比如按键等事件
        key_control(hero,enemy)

        #更新需要显示的类容
        pygame.display.update()
        time.sleep(0.01)
        t2 =time.time()
        time_count =t2-t1
        if  time_count>1 and int(time_count)%10 ==0:
            print('%0.2f'%time_count)
if __name__ == "__main__":
    count = 0

    main()