#-*-coding:utf-8-*-

import numpy as np
import time

def FizzBuzz(n):
    output = np.array(['Fizz Buzz' if i%15==0 else 'Fizz' if i%3==0 and i%5!=0 else 'Buzz' if i%3!=0 and i%5==0 else str(i) for i in xrange(1,n+1)],dtype=np.string_)
    return output

def main():
    n = int(raw_input('Iterator:'))
    Result = FizzBuzz(n)
    for i in xrange(n):
        print Result[i]

if __name__ == '__main__':
    start = time.clock()
    main()
    finish = time.clock()
    print '経過時間：',finish-start,'[s]'
