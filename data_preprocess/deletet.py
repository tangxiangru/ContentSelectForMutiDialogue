#把\t都转为\n
import os
import sys
with open('train.txt','r') as r:
    lines=r.readlines()
with open('newtrain.txt','w') as w:
    for l in lines:

        w.write(l.replace('\t','\n'))
