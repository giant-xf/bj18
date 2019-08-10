card_infors = []
'''def file_name_get():
    file_name =input('请输入工作目录,该文件将在该目录创建:')
    file_out()
    return file_name
 '''
def file_in():
    '''文件保存'''
    f = open('./学生名片管理.txt', 'a')
    # in_infors  =[{'name':'laowang','age':18},{'name':'laozhang','age':20}]
    for i, temp in enumerate(card_infors):
        # print(i,temp)
        # f.write(str(temp)+'\n')
        for key, value in temp.items():
            f.write(str(key) + ':' + str(value) + '\t')
        f.write('\n')
    f.close()
def file_in1():
    '''文件保存'''
    f = open('./.txt', 'w')
    # in_infors  =[{'name':'laowang','age':18},{'name':'laozhang','age':20}]
    for i, temp in enumerate(card_infors):
        # print(i,temp)
        # f.write(str(temp)+'\n')
        for key, value in temp.items():
            f.write(str(key) + ':' + str(value) + '\t')
        f.write('\n')
    f.close()
'''def file_out1():
    #文件读取
    f = open('学生名片管理.txt', 'r')
    while True:
        temp =f.readline()
        temp =temp.rstrip()
        if  not temp:
            break
        #card_infors.extend(temp)
        print(temp)
    f.close()'''
def AddtoDict(str_1):
    """定义一个函数,功能：把文件里面的内容添加到字典中"""
    # 去掉空格
    str_2 = str_1.rstrip()

    list_str1 = str_2.split('\t')
    # 用来测试/t是否去掉
    # print(list_str1)

    # 创建一个空列表准备去掉换行符   |n
    line_str = []
    for i in list_str1:
        x = i.strip('\n')
        line_str.append(x)
    # 测试 /n是否去掉
    # print(line_str)
    dect_all = {}
    # 循环遍历处理后的字符串。
    for item in line_str:
        if item[0:4] == 'name':
            dict = {item[0:4]: item[5:]}
        elif item[0:3] == 'age':
            dict = {item[0:3]: item[4:]}
        elif item[0:3] == 'num':
            dict = {item[0:3]: item[4:]}
        # 将获取到的字符串传到字典中
        dect_all.update(dict)
    # 测试字典中元素是否添加成功
    # print(dect_all)

    # 将字典添加到列表中
    card_infors.append(dect_all)
    # print(card_infors)
def file_out():
    '''读取文件夹并结合调用Addtodict()函数进行处理'''
    try:
        file = open('./学生名片管理.txt', 'r')
        # 循环获取文件中的字符串
        while True:
            # 一行一行的读取
            line = file.readline()
            # 当读取到的值不为空时 一行行调用AddtoDict()函数的处理
            if line:
                AddtoDict(line)
            # 判断到了末尾位置并退出循环
            if not line:
                break
        file.close()
        # 打印列表供测试使用
        #print(card_infors)
    except Exception:
        pass


def panduan_name(name):
    file_out()
    for temp in card_infors:
        if name == temp['name']:
            print('有相同的名字信息，无法添加！')
            card_infors.clear()
            return  True
    else :
        #card_infors.clear()
        return False
def panduan_age(age):
    '''age判断函数'''
    age = int(age)
    if age > 0 and age < 120:
        return False
    else:
        print('age输入有误，请输入正确的age')
        return True
def panduan_num(num):
    '''num判断函数'''
    num = str(num)
    if num.isdigit() and len(num)<=15:
        return False
    else:
        print('num输入有误，请输入正确的num')
        return True

def print_menu():
    '''显示菜单栏'''
    print('=' * 30)
    print('**********学生管理系统********')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.显示文件中所有学生信息')
    print('6.退出学生管理系统')
    print('=' * 30)
def print_add():
    '''添加学生信息'''
    print(' ')
    print('*********添加学生信息栏*********')
    infors = {}
    flag_name =True
    while flag_name:
        add_name = input('请输入学生name:')
        flag_name =panduan_name(add_name)
        card_infors.clear()
    #开始判断age
    flag_age = True
    while flag_age:
        add_age = input('请输入学生age:')
        flag_age = panduan_age(add_age)
    #开始判断num
    flag_num = True
    while flag_num:
        add_num = input('请输入学生num:')
        flag_num = panduan_num(add_num)
    infors['name'] = add_name
    infors['age'] = add_age
    infors['num'] = add_num
    #card_infors.append(infors)
    card_infors.append(infors)
    print('添加成功！！！')
    # print(card_infors)
def print_del(new_name):
    '''删除学生信息'''
   # print('*********删除学生信息*********')
    #new_name = input('请输入要删除的学生name:')
    # 查找name是否存在
    for i, temp in enumerate(card_infors):
        if temp['name'] == new_name:
            del card_infors[i]
            print('删除成功！！！')
            break
    else:
        print("输入的学生姓名有误或没有此人请重新输入！")
def print_xiugai():
    '''修改学生信息'''
    print(' ')
    print('*********修改学生信息*********')
    name = input('请输入要修改的学生姓名:')
    for infors in card_infors:
        if name == infors['name']:
            print_del(name)
            file_in1()
            card_infors.clear()
            flag_name =True
            while flag_name:
                add_name = input('请输入修改后的学生name:')
                flag_name= panduan_name(add_name)
            flag_age =True
            while flag_age:
                add_age = input('请输入学生age:')
                flag_age = panduan_age(add_age)
            flag_num = True
            while flag_num:
                add_num = input('请输入学生num:')
                flag_num = panduan_num(add_num)
            infors['name'] = add_name
            infors['age'] = add_age
            infors['num'] = add_num
            card_infors.append(infors)
            print('修改成功！！！')
            return True
            break
    else:
        print("输入的学生姓名有误或没有此人！")
        card_infors.clear()
        return False
        # print(card_infors)
def print_find():
    '''查询学生信息'''
    print(' ')
    print('*********查询学生信息*********')
    find_name = input('请输入要查找的学生姓名:')
    for temp in card_infors:
        if find_name == temp['name']:
            # 表示找到了
            print('姓名     \tage\t\t  num\t')
            print('%s\t%s\t  %s\t' % (temp['name'].ljust(10), temp['age'].ljust(4), temp['num'].ljust(15)))
            print('显示成功...')
            break
    else:
        print('查无此人...')
def print_xianshi():
    '''显示所有学生信息'''
    print(' ')
    print('*********显示学生信息*********')
    print('姓名     \tage\t\t  num\t')
    for temp in card_infors:
        if len(card_infors)==0:
            print('文件中没有数据！')
            break
        else:
            print('%s\t%s\t  %s\t' % (temp['name'].ljust(10), temp['age'].ljust(4), temp['num'].ljust(15)))
    print('\n已经显示全部学生信息.....\n文件中共有【%d】个学生信息'%(len(card_infors)))

def main():
    while True:
        print('')
        i = input('请输入功能选项:')
        if i.isalnum():
            if i.isdigit():
                if int(i) == 1:
                    card_infors.clear()
                    print_add()
                    file_in()
                    card_infors.clear()
                elif int(i) == 2:
                    #card_infors.extend(file_out())
                    card_infors.clear()
                    file_out()
                    print('*********删除学生信息*********')
                    new_name = input('请输入要删除的学生name:')
                    print_del(new_name)
                    file_in1()
                    card_infors.clear()
                elif int(i) == 3:
                    card_infors.clear()
                    file_out()
                    if print_xiugai():
                        file_in1()
                    card_infors.clear()
                elif int(i) == 4:
                    card_infors.clear()
                    file_out()
                    print_find()
                    card_infors.clear()
                elif int(i) ==5:
                    card_infors.clear()
                    file_out()
                    print_xianshi()
                    card_infors.clear()

                elif int(i) == 6:
                    print('退出成功.....')
                    break
                elif int(i)>6 or int(i)<1:
                    if int(i)>6:
                        print('输入的数字编号过大.本人还未开发这么多功能！')
                    elif int(i)<1:
                        print('输入的数字编号不能小于 1')
                    main()
            elif i.isalpha():
                print('输入有误...请输入纯数字')
                main()
            else:
                print('输入有误...请输入纯数字')
        else:
            print('输入的什么火星文？？')
print_menu()
main()
