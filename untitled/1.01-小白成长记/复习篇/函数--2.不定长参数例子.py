def fun(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs:")
    for key, value in kwargs.items():
        print(key, "=", value)

fun(1,2,3,4,5,6,name='laowang',age='23')