import random
import time

def mklst(len, min=-10, max=10):
    lst = list()
    for i in range(len):
        lst.append(random.randint(min,max))
    return lst


def avg_time(func, target, epoch = 10):
    """
    :param func: target function(without parenthesis)
    :param target: target list
    :param epoch: repeat time(default=10
    :return: average run-time(int)
    """
    t = list()
    for i in range(epoch):
        lst = list(target)

        s = time.time()
        func(lst)
        t.append(time.time()-s)

    return sum(t)/len(t)

if __name__ == "__main__":
    print(mklst(20))
    