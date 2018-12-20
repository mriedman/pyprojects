from random import randint
import time
from copy import copy
def nextpermute(y,s=True):
    x = [int(i) for i in y]
    for i in range(len(x)-1,-1,-1):
        if x[i]>x[i-1]:
            j = x.index(min(k for k in x[i:] if k>x[i-1]))
            x[i-1],x[j]=x[j],x[i-1]
            x[i:] = sorted(x[i:])
            break
    if s:
        return x
    return x
def apply(x,y,z):
    global o
    q=copy(x)
    y1=copy(y)
    for i1 in range(len(y1)):
        i=y1[i1]
        q=q[:i]+[o[z[i1]](q[i],q[i+1])]+q[i+2:]
        y1=[(j if j<i else j-1) for j in y1]
    return q[0]
def liststr(x):
    s=''
    for i in x:
        s+=i
    return s
def equation(x,y,z):
    s=[]
    op=['+','-','*','/']
    for i in range(4):
        s+=[str(x[i]),op[z[y.index(i)]]]
    s.append(str(x[4]))
    for i in range(4):
        i1=y[i]
        while liststr(s[2*i1:]).count(')')>liststr(s[2*i1:]).count('('):
            i1-=1
        i2=y[i]+1
        while liststr(s[:2*i2+1]).count('(')>liststr(s[:2*i2+1]).count(')'):
            i2+=1
        s[2*i1]='('+s[2*i1]
        s[2*i2]+=')'
    return liststr(s)
def div(x,y):
    if y!=0:
        return x/y
    return -1000
o=[lambda x,y:x+y,lambda x,y:x-y,lambda x,y:x*y,div]
count=0
def solve(a,b,all):
    for k in range(120):
        arr=[0,1,2,3]
        for i in range(256):
            k1=[int((i%(4**j)-i%(4**(j-1)))/4**(j-1)) for j in range(4,0,-1)]
            for j in range(24):
                if apply(a,arr,k1)==b:
                    if all:
                        return equation(a,arr,k1)
                    else:
                        print(equation(a,arr,k1))
                arr=nextpermute(arr)
        a=nextpermute(a)
def hassol(a,b):
    if solve(a,b,all)!=None:
        print('Has a solution')
    else:
        print('Does not have a solution')
def c(m):
    if m.lower() != 's':
        p1=input('Players: ').split(' ')
        p={i: 0 for i in p1}
    w=''
    while True:
        if m.lower() != '1p':
            n=sorted(list(map(int, input('Numbers: ').split(' '))))
            t=int(input('Target: '))
            if m.lower() != 's':
                s1 = input('Winner: ')
            if m.lower() != 's' and not s1 == '':
                p[s1] += 1
                print(solve(n,t,True))
            else:
                print(solve(n,t,True))
            if m.lower() != 's':
                print(str(p)[1:-1])
        else:
            n=[randint(1, 25) for i in range(5)]
            t=randint(1, 25)
            print(n)
            print(t)
            if input('Win? ').lower() == 'no':
                w += '0'
                print(solve(n,t,True))
            else:
                w += '1'
                print(solve(n,t,True))
            print(w)
        if input('Play Again? ') == 'No':
            break
print(solve([4,7,11,23,28],30,all))
