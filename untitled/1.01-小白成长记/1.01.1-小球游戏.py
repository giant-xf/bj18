
import sys,pygame,random,time
from pygame.locals import *
#定义一个输出字体的函数
#第一个参数表示字体对象  (X,Y)表示位置 color表示字体颜色
#第一步Render()函数来绘制内容，第二步blit()函数来进行绘制，第三步 pygame.display.set_mode()获得显示系统的访问窗口
#第四步 pygame.font()将文本输出到图形窗口
def print_text(font,x,y,text,color=(255,255,255)):
    #1.1
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))

#1.2初始化pygame
pygame.init()
#1.3定义一个窗口
screen = pygame.display.set_mode((600,500))
#1.4创建一个标题
pygame.display.set_caption('最强接小球')
#1.5将文本输出到图形的窗口，第一个参数None表示使用pygame默认字体，第二个参数表示字体大小
font1 = pygame.font.Font(None,24)
#1.6>隐藏或显示鼠标光标
pygame.mouse.set_visible(False)
#1.7设置元素的颜色
white =255,255,255
red =220,0,0
yellow =230,230,50
blue = 0,0,100
#1.8 游戏次数和得分
score = 0
lives = 3
#1.9 游戏结束的标记、鼠标点击的位置 、
# 初始化挡板的位置 、小球的位置、速度变量
game_over = True
mouse_x = mouse_y = 0
pos_x = 300
pos_y = 460
 #小球位置随机
bomb_x = random.randint(0,500)
bomb_y = -50
 #速度变量
vel_y = 0.7

#2 循环创建一个事件处理程序(重点) pygame.event.get() 从队列中获取事件
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION: #如果事件类型是鼠标运动的类型
            mouse_x,mouse_y = event.pos #鼠标直接控制挡板
        elif event.type == MOUSEBUTTONUP: #如果鼠标类型是抬起类型
            if game_over:
                game_over = False
                lives = 3
                score = 0
    #2.1 获取所以键盘按钮的状态
    keys = pygame.key.get_pressed()
    #2.2>如果我们的事件是计算机的退出键，那么就退出
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_SPACE ]:
        time.sleep(5)
    #颜色填充
    screen.fill(blue)
    #重点
    if game_over:
        if score>=0 and score<100 and lives ==0:
            print_text(font1, 230, 200, 'You are no technology', red)
        elif score>=100 and score<1500:
            print_text(font1, 230, 200, 'You are great', red)
        elif score>1500:
            print_text(font1, 230, 200, 'You are very great', red)
        print_text(font1, 250, 230, 'Score%d' % score)
        print_text(font1,250,250,'<CLICK>',red)
        vel_y=0.5
    else :
        #如果游戏没有结束
        bomb_y += vel_y
        # 可能接住小球，可能没有接住
        #如果没接住 1.生命值减少 ，2，重新生成小球位置，3.当lives=0，重新回到界面
        if bomb_y>500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -=1
            if lives == 0:
                game_over = True
                #接住小球，1.分数++,2.水平方向随机生成小球
        elif bomb_y>pos_y:
            if bomb_x > pos_x and bomb_x < pos_x+120:
                score +=10
                bomb_x = random.randint(0, 500)
                bomb_y = -50
        elif score>50:
            if score >=50 and score <200:
                vel_y = 0.7
            elif score >=200 and score <500:
                vel_y = 0.9
            elif score <=500 and score <800:
                vel_y =1.0
            elif score >=800 and score <1200:
                vel_y = 1.2
            elif score >=1200 and score <1500:
                vel_y = 1.5
            elif score >=1500 and score <2000:
                vel_y = 1.9
            elif score >= 2000:
                vel_y = 2.3
         #画小球
        pygame.draw.circle(screen,yellow,(bomb_x,int(bomb_y)),30,0)
        #2.3 > 设置挡板的位置, 并做判断
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
         #2.4画挡板
        pygame.draw.rect(screen,red,(pos_x,pos_y,120,40),0)
        #2.5 > 输出我们的生命值
    print_text(font1,0,0,'LIVES:'+str(lives),yellow)
        #2.6 > 输出我们的得分值
    print_text(font1,500,0,'SCORE:'+str(score),yellow)
        #2.7>更新显示
    pygame.display.update()


