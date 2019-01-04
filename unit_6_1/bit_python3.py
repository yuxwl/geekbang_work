#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''

import time


even_cnt = 0
odd_cnt = 0
start = time.time()
for i in range (0,500000000):
    if i&1 == 0:
        even_cnt +=1
    else:
        odd_cnt +=1


end = time.time()
print (end - start)
print (even_cnt)
print (odd_cnt)

print ("------------------------------")

even_cnt = 0
odd_cnt = 0
start = time.time()
for i in range (0,500000000):
    if i%2 == 0:
        even_cnt +=1
    else:
        odd_cnt +=1


end = time.time()
print (end - start)
print (even_cnt)
print (odd_cnt)
