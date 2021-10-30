import time


def cal_time(func):
    """
    计算函数运行时长的装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s s." % (func.__name__, t2 - t1))
        return result
    return wrapper
