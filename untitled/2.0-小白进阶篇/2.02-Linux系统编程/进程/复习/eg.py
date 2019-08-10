import os

from multiprocessing import Pool,Manager

def copyFile(name,oldFileName,newFileName,queue):
    try:
        fr = open(oldFileName+"/"+name)
        fw = open(newFileName+"/"+name,"w")

        count = fr.read()
        fw.write(count)

        fr.close()
        fw.close()

        queue.put(name)
    except:
        print("%s文件夹名已经存在！无法copy")
def main():
    #1.获得用户输入的文件夹名字
    oldFileName = input("请输入需要copy的文件夹名字：")

    #2.创建一个文件夹
    newFileName = oldFileName+"[复件]"
    os.mkdir(newFileName)

    #3.获得old文件中所以的文件名
    fileNames = os.listdir(oldFileName)
    #rint(fileNames)

    #4.使用进程池copy文件内容
    pool = Pool(5)
    queue = Manager().Queue()

    for names in fileNames:
        pool.apply_async(copyFile,(names,oldFileName,newFileName,queue))

    num = 0
    allNum = len(fileNames)
    while num < allNum:
        queue.get()
        num +=1
        cn =num/allNum
        print("\r\rcopy进度为:%.2f%%" % (cn * 100), end="")

    pool.close()
    pool.join()
    print("")
    print("copy完成！")
if __name__ == '__main__':
    main()