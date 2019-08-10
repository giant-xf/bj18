def fib():
    i =0
    temp =None
    while i<5:
        print(temp)
        temp = yield (i)
        print('-------')
        print(temp)
        i+=1
    return 'done'
f =fib()
f.__next__()
f.send('aaa')