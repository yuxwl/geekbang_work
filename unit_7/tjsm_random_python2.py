#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''
import random

def tianji_gongzi():
    winer_per = []
    t = [2,5,8]
    g = [3,6,9]
    N = 2
    for i in range(0,3):
        para1 = random.randint(0,N)
        para2 = random.randint(0,N)
        N = N-1

        if t[para1] > g[para2]:
            winer_per.append(1)
        else:
            pass
        t.remove(t[para1])
        g.remove(g[para2])

    return len(winer_per)

if __name__ == '__main__':
    tj = tianji_gongzi()
    print (tj)
