#删除检索式对话里面的负样本
import os
import sys
with open('test.txt','r') as r:
    lines=r.readlines()
with open('test.txt','w') as w:
    for l in lines:
        if "0\t" in l:
            continue
        w.write(l.replace('\t','\n'))

