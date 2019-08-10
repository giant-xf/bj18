import os,time
from multiprocessing  import Pool,Manager

def copyfile(name,old_filename,new_filename,q):
    "文件copy功能函数"
    fr =open(old_filename+'/'+name,)
    fw =open(new_filename+'/'+name,'w')

    file  =fr.read()
    fw.write(file)

    fr.close()
    fw.close()

    q.put(name)

def main():

    #1.获取需要拷贝的文件夹
    old_filename =input('请输入需要拷贝的文件名:')

    #2.创建新的文件名
    new_filename =old_filename+'[复件]'
    os.mkdir(new_filename)

    #3.获取文件夹中的文件列表
    names =os.listdir(old_filename)
    #4.创建进程池
    pool =Pool(5)
    #创建通讯
    q =Manager().Queue()
    #开始copy的时间
    t1 = time.time()
    #5.循环将进程放入进程池中
    for name in names:
        pool.apply_async(copyfile,(name,old_filename,new_filename,q))


    #pool.close()
    #pool.join()
    num =0
    allnum =len(names)
    while num <allnum:
        q.get()
        num +=1
        contern =num/allnum
        print('\r\rcopy文件进度为:%.2f%%'%(contern*100),end='')
    #结束copy的时间
    t2 =time.time()
    print('\n一共copy了%d个文件,总共耗时为:%.2f'%(allnum,(t2-t1)))
if __name__ == '__main__':
    main()