import tkinter
import threading
import time
from tkinter.messagebox import *

#1,设计一个窗口
win = tkinter.Tk()
#1.1 设计窗口名字
win.title('My girlfriend ')
#1.2 设计窗口大小
win.minsize(300,300)
#1.3设计12个按钮和12个图片
bm1=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\悦.png')
bm2=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\漂亮.png')
bm3=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\吃货.png')
bm4=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\身材好.png')
bm5=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\聪明.png')
bm6=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\可爱.png')
bm7=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\贪玩.png')
bm8=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\听话.png')
bm9=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\腿长.png')
bm10=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\调皮.png')
bm11=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\Love.png')
bm12=tkinter.PhotoImage(file ='C:\\Users\Administrator\Desktop\dist\峰.png')
btn1 =tkinter.Button(win,text='悦',bg ='red',image =bm1,fg ='pink')
btn1.place(x =20,y =20,width =50,height =50)
btn2 =tkinter.Button(win,text='漂亮',bg ='white',image =bm2,fg ='pink')
btn2.place(x =90,y =20,width =50,height =50)
btn3 =tkinter.Button(win,text='吃货',bg ='white',image =bm3,fg ='pink')
btn3.place(x =160,y =20,width =50,height =50)
btn4 =tkinter.Button(win,text='身材好',bg ='white',image =bm4)
btn4.place(x =230,y =20,width =50,height =50)
btn5 =tkinter.Button(win,text='聪明',bg ='white',image =bm5)
btn5.place(x =230,y =90,width =50,height =50)
btn6 =tkinter.Button(win,text='可爱',bg ='white',image =bm6)
btn6.place(x =230,y =160,width =50,height =50)
btn7 =tkinter.Button(win,text='贪玩',bg ='white',image =bm7)
btn7.place(x =230,y =230,width =50,height =50)
btn8 =tkinter.Button(win,text='听话',bg ='white',image =bm8)
btn8.place(x =160,y =230,width =50,height =50)
btn9 =tkinter.Button(win,text='腿长',bg ='white',image =bm9)
btn9.place(x =90,y =230,width =50,height =50)
btn10 =tkinter.Button(win,text='调皮',bg ='white',image =bm10)
btn10.place(x =20,y =230,width =50,height =50)
btn11 =tkinter.Button(win,text='Love',bg ='white',image =bm11)
btn11.place(x =20,y =160,width =50,height =50)
btn12 =tkinter.Button(win,text='峰',bg ='white',image =bm12)
btn12.place(x =20,y =90,width =50,height =50)
#2.1 将所有按钮选项放入列表中
girllist = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]
#2.2 自定义开启循环标记
isloop = False
#2.3 定义停止标记
stopgign = False
#2.4 通过ID索引值来确定对应的选项
stopid = None
#3 定义函数:  1.循环 被选项，2.设置选项背景颜色(被选到的和没有被选到的)
def round():
    #申明全局变量
    global isloop
    global stopid
    if isloop ==True:
        return
    i =1
    if isinstance(stopid,int):
        i = stopid
    #3.1开始循环
    while True:
        #延时操作
        # 转速
        time.sleep(0.03)
        #3.2将背景遍历为白色
        for x in girllist:
            x['bg'] = 'white'

        #3.3 当选到对应值时，将背景变为红色
        girllist[i]['bg'] = 'red'
        i +=1

        #print("当前选中值为",girllist[i-1]['text'])

        #i不能超出12
        if i>=len(girllist):
            i =0
        #当触碰暂停按钮时
        if stopgign ==True:
            isloop = False
            stopid = i

            time.sleep(0.3)
            root = tkinter.Tk()
            root.title('抽到的结果')
            root.geometry('200x200')
            root.maxsize(500, 500)
            t = tkinter.Text(root)
            if i >1 and i<=10:
                t.insert(1.0,'我家悦儿'+girllist[i-1]['text'] )
            elif i ==11:
                t.insert(1.0, '悦儿非常' + girllist[i - 1]['text']+'小峰')
            elif i ==0:
                t.insert(1.0, '小'+girllist[11]['text']+'也Love悦儿')
            elif i ==1:
                t.insert(1.0, '小' + girllist[i - 1]['text'] + '么么哒！')
            t.place(x=40,y=80,height=20,width=120)
            root.mainloop()
            break

# 定义开始方法
def newtask():
    global stopgign
    global isloop
    stopgign = False
    t = threading.Thread(target=round)
    t.start()
    isloop = True

#定义暂停方法
def stop1():
    global stopgign
    if stopgign == True:
        return
    stopgign = True


count =2
#登入界面的确认
def queren():
    global dengru
    global count
    dengru =False
    print('连续3次登入失败会冻结账户！！')
    username =input('请输入用户账号:')
    password =input('请输入用户密码:')
    if (username =="wangyue" and password =='8023cloud520')or (username =='6666' and password==''):
        print('登入成功,可以正常游戏')
        time.sleep(1)
        dengru =True
    else :
        print('登入失败')
        dengru =False
        if count ==2:
            count -=1
            print("请确认后再次输入")
            time.sleep(0.5)
            queren()
        elif count ==1:
            count -=1
            print('最后一次机会了，想清楚，不然会被冻结')
            time.sleep(0.5)
            queren()
        elif count ==0:
            time.sleep(1)
            print('输入错误次数过多，账户被冻结 60秒')
            time.sleep(60)
            print('要不再想想？(yes) 还是直接退出？(no)')
            yes1 =input('输入yes or no : ')
            if yes1 =="yes" :
                time.sleep(1)
                count =2
                queren()
            elif yes1 =='no':
                exit()
            else:
                time.sleep(2)
                print('你是猪吗？提示你输入都不会，还想玩游戏？')
                time.sleep(5)
                print('让你静静的看着屏幕上的字')
                time.sleep(2)
                print('看你这个猪还长不长教训')
                time.sleep(1)
                print('再等5秒让你再试一次密码')
                time.sleep(5)
                count =0
                queren()

    if dengru==True:
#设置开始按钮
        btn_start =tkinter.Button(win,text='开始',bg='white',command =newtask)
        btn_start.place(x=90,y=125,width =50,height = 50)
#设置暂停按钮
        btn_start1 =tkinter.Button(win,text='暂停',bg='white',command =stop1)
        btn_start1.place(x=160,y=125,width =50,height = 50)
        win.mainloop()

queren()













