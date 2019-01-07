#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''
#说明:田忌赛马中,齐王的出场顺序是固定的,田忌不同组合的结果

import random

q_horses = ["q1","q2","q3"]
q_horses_time = {"q1":1,"q2":2,"q3":3}
t_horses_time = {"t1":1.5,"t2":2.5,"t3":3.5}

def compare(t,q):
    t_win_per = 0
    for i in range(0,len(t)):
        if t_horses_time.get(t[i]) < q_horses_time.get(q[i]):
            t_win_per += 1

    if t_win_per > len(t)/2 :
        print ("田忌获胜!")
    else:
        print ("齐王获胜!")

def permutate(horses,result):
    
    if len(horses) == 0 :
        compare(t=result,q=q_horses)
        print (result)

    for i in range(0,len(horses)):

        #从剩下的未出战马匹中，选择一匹，加入结果
        new_result = result[:]
        new_result.append(horses[i])      

        #将已选择的马匹从未出战的列表中移出
        rest_horses = horses[:]
        rest_horses.remove(horses[i])

        #递归调用,对剩余的马匹继续生成排列
        permutate(rest_horses,new_result)


if __name__ == '__main__':
    horses = ["t1","t2","t3"]
    result = []
    permutate(horses,result)
