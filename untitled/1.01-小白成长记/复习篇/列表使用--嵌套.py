import random

# 定义一个列表来保存3个办公室
offices = [[], [], []]

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for name in names:
    # 将names中的数据随机添加到offices的内嵌表中
    x = random.randint(0, 2)
    offices[x].append(name)

# 记载办公室数编号
i = 1

# 将offices中数据取出来
for temp in offices:
    print("办公室%d中有%d个人" % (i, len(temp)))
    i += 1

    for name in temp:
        print("%s" % name, end="")

    print("")