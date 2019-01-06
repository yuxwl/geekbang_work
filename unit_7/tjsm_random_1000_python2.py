#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''
#说明:比赛1000场,每场三局两胜

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



def t_win_per(times):
    t_win_times = []
    for i in range(0,times):
        a = tianji_gongzi()
        if a >=2:
            t_win_times.append(a)
    return len(t_win_times)



if __name__ == '__main__':
    tj = t_win_per(1000)
    print (tj)

