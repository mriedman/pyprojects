from random import random
def m(n):
    return random()<n
def ls(l):
    a=0
    t=0
    for i in l:
        if i:
            t+=1
        else:
            t=0
        if t>a:
            a=t
    return a
def ls2(n,l):
    return ls([m(n) for i in range(l)])
def q(l,d):
    l1=sorted(l)
    return [l1[i] for i in range(0,len(l),int(len(l)/d))][1:]
def mu(l):
    return sum(l)/len(l)
l=[ls2(0.982,200) for i in range(10000)]
print(q(l,50))