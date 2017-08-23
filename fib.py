#!/usr/bin/env python
class Fibonacci:
    def __init__(self):
        self._values = ["котам", "почему-то", "говорять", "ты"]
        
    def __iter__(self):
        #sam sebi iterator
        self._listindex = -1
        return self

    def __next__(self):   
        lastindex = len(self._values) - 1
        if self._listindex >= lastindex:
            raise StopIteration
        self._listindex += 1
        return self._values[self._listindex]
        

if __name__ == '__main__':
    f = Fibonacci()
    for s in  f:
        print(s)

    for s2 in f:
        print(s2)
