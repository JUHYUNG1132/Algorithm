####################
# 스택              #
# Python           #
####################

class Stack:
    def __init__(self):
        self.__stack = list()

    def __str__(self):
        return str(self.__stack)

    def empty(self):
        return len(self.__stack) == 0

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if not self.empty():
            return self.__stack.pop(-1)

    def peek(self):
        if not self.empty():
            return self.__stack[-1]


if __name__ == "__main__":
    s = Stack()
    print('is Empty? ', s.empty())
    s.push(1)
    s.push(2)
    print('s         ', s)
    print('s.peek()  ', s.peek())
    print('s         ', s)
    print('s.pop()   ', s.pop())
    print('s         ', s)
    print('is Empty? ', s.empty())
