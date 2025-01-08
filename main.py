import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        #return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def hello(name):
    return f"{name}"

add(5, 8)
hello("Kipchumba")


def r(times):
    def d(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return d

@r(4)
def s():
    print("Hello")

s()

import time

def tim(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start} secs")
        return result
    return wrapper

@tim
def slow():
    time.sleep(1)
    print("Done")

slow()

class Math:
    @staticmethod
    def multiply(d, c):
        return d * c
print(Math.multiply(12, 2))

class Math:
    cou = 0
    @classmethod
    def plus(p):
        p.cou +=1
        return p.cou
    
print(Math.plus())
    