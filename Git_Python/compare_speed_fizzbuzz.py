#-*-coding:utf-8-*-

import numpy as np
import time

def FizzBuzz_0(n):
    #工夫なし
    start = time.clock()
    for i in xrange(1,n+1):
        if i%15==0:
            print 'Fizz Buzz'
        elif i%3==0:
            print 'Fizz'
        elif i%5==0:
            print 'Buzz'
        else:
            print i
    finish = time.clock()
    print '経過時間：',finish-start,'[s]'


def FizzBuzz_1(n):
    #リストの内包表記利用
    start = time.clock()
    output = np.array(['Fizz Buzz' if i%15==0 else 'Fizz' if i%3==0 and i%5!=0 else 'Buzz' if i%3!=0 and i%5==0 else str(i) for i in xrange(1,n+1)],dtype=np.string_)
    finish = time.clock()
    print '経過時間：',finish-start,'[s]'
    return output

def main():
    n = int(raw_input('Iterator:'))
    FizzBuzz_0(n)
    Result = FizzBuzz_1(n)

if __name__ == '__main__':    
    main()
