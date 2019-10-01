def myFun(**kwargs):
    for key ,value in kwargs.items():
        print("%s==%s"%(key,value))

myFun(First='One', Second = "second")
