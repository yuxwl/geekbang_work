#!/usr/bin/env python
# _*_coding:utf-8_*_
'''
    * @author: Xwl_Yu.
'''

#组合

import copy

def combination(n,comb,result):
    if n == 0:
        print (result)
        return

    for i in comb:
        newResult = copy.copy(result)
        newComb = copy.copy(comb)
        newResult.append(i)
        newComb = list(set(newComb).difference(set(comb[:comb.index(i)+1])))
        combination(n-1,newComb,newResult)

if __name__ == '__main__':
    comb = ['t1', 't2', 't3', 't4', 't5']
    result = []
    combination(4, comb, [])
