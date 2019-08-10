import tkinter
import threading
import time

#1,设计一个窗口
win = tkinter.Tk()
#1.1 设计窗口名字
win.title('女神')
#1.2 设计窗口大小
win.minsize(300,300)

#1.3设计2个按钮
btn1 =tkinter.Button(win,text='A',bg ='red')
btn1.place(x =20,y =20,width =50,height =50)
btn2 =tkinter.Button(win,text='B',bg ='white')
btn2.place(x =90,y =20,width =50,height =50)
btn3 =tkinter.Button(win,text='C',bg ='white')
btn3.place(x =160,y =20,width =50,height =50)
btn4 =tkinter.Button(win,text='D',bg ='white')
btn4.place(x =230,y =20,width =50,height =50)
btn5 =tkinter.Button(win,text='E',bg ='white')
btn5.place(x =230,y =90,width =50,height =50)
btn6 =tkinter.Button(win,text='F',bg ='white')
btn6.place(x =230,y =160,width =50,height =50)
btn7 =tkinter.Button(win,text='G',bg ='white')
btn7.place(x =230,y =230,width =50,height =50)
btn8 =tkinter.Button(win,text='H',bg ='white')
btn8.place(x =160,y =230,width =50,height =50)
btn9 =tkinter.Button(win,text='I',bg ='white')
btn9.place(x =90,y =230,width =50,height =50)
btn10 =tkinter.Button(win,text='J',bg ='white')
btn10.place(x =20,y =230,width =50,height =50)
btn11 =tkinter.Button(win,text='K',bg ='white')
btn11.place(x =20,y =160,width =50,height =50)
btn12 =tkinter.Button(win,text='L',bg ='white')
btn12.place(x =20,y =90,width =50,height =50)
#2.1 将所有按钮选项放入列表中
girllist = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]
girllist1 =['A','B','C','D','E','F','G','H','I','J','K','L']
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
        time.sleep(0.03)
        #3.2将背景遍历为白色
        for x in girllist:
            x['bg'] = 'white'

        #3.3 当选到对应值时，将背景变为红色
        girllist[i]['bg'] = 'red'
        i +=1
        print("当前选中值为",girllist[i-1]['text'])
        #i不能超出12
        if i>=len(girllist):
            i =0
        #当触碰暂停按钮时
        if stopgign ==True:
            isloop = False
            stopid = i
            root = tkinter.Tk()
            root.title('抽到的结果')
            root.geometry('200x200')
            root.maxsize(500, 500)
            t = tkinter.Text(root)
            if i >= 1:
                t.insert(1.0, '你抽到的结果为'+girllist[i-1]['text'])
            elif i == 0:
                t.insert(1.0, '你抽到的结果为'+girllist[i - 1]['text'])
            t.place(x=40, y=80, height=20, width=120)
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
    global i
    if stopgign == True:
        return
    stopgign = True


count =2
def queren():
    global dengru
    global count
    dengru =False

    print('连续3次登入失败会冻结账户！！')
    username =input('请输入用户账号:')
    password =input('请输入用户密码:')
    if username =="chenxiongfeng" and password =='123456':
        print('登入成功,可以正常游戏')
        dengru =True
    else :
        print('登入失败')
        dengru =False
        if count >0:
            count -=1
            print("请确认后再次输入")
            time.sleep(0.5)
            queren()
        elif count ==0:
            time.sleep(1)
            print('输入错误次数过多，账户被冻结')
            exit()

    if dengru==True:
#设置开始按钮
        btn_start =tkinter.Button(win,text='开始',bg='white',command =newtask)
        btn_start.place(x=90,y=125,width =50,height = 50)
#设置暂停按钮
        btn_start1 =tkinter.Button(win,text='暂停',bg='white',command =stop1)
        btn_start1.place(x=160,y=125,width =50,height = 50)
        win.mainloop()

queren()