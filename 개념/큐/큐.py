####################
# 큐               #
# Python           #
####################

class Queue:
    def __init__(self):
        self.__queue = list()

    def __str__(self):
        return str(self.__queue)

    def put(self, item):
        self.__queue.insert(0, item)

    def get(self):
        return self.__queue.pop(-1)


if __name__ == '__main__':
    q = Queue()
    print('q       ', q)
    q.put(1)
    print('q.put(1)', q)
    q.put(2)
    print('q.put(2)', q)
    print('q.get() ', q.get())
    print('q       ', q)
