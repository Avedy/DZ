import time


def times(func):
    def trimes():
        start = time.time()
        func()
        end=time.time()-start
        print(end)
    return trimes


@times
def func_to_decor():
    for i in range(1000):
        print(i)


func_to_decor()