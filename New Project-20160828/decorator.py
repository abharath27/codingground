def myDecorator(func):
    def wrapper():
        print "before func"
        func()
        print "after func"
    return wrapper

@myDecorator
def genFunc():
    print "genFunc"
    

genFunc()
