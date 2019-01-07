#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''
#假设有一个 6 位字母密码，每位密码是 a～e 之间的小写字...

import copy

password = "dccbae"
obj_pass = ["a","b","c","d","e"]


def get_password( n, result = ''):
    if n == 0:
        if result == password:
            print (result)
    else:
        for i in obj_pass:
            new_result = copy.copy(result)
            new_result = new_result + i
            get_password(n - 1, new_result)

if __name__ == '__main__':
    get_password(6)
