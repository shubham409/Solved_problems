from pythonchef import *
import numpy as np



def fun(target,ls):
    sm=0
    ans=[]
    f=0
    l=0
    for i,val in enumerate(ls):
        if sm <target :
            l+=1
            if i ==0:
                f=0
                l=0

            ans.append(val)
            
            sm+=val
        if sm >target:
            while sm> target:
                first = ans.pop(0)
                sm-= first 
                f+=1
        if sm == target:
            print(f+1,l+1)
            return
    print(-1)
    
T = int(input())
for i in range (T):
    x = input ().split(' ')
    x = list(map(int,x))
    y = input ().split(' ')
    y = list(map(int,y))
    fun(x[1],y)
