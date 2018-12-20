from time import sleep
from random import randint
from math import factorial
#teams=['Celtics','Suns','Lakers','Sixers','Magic','T-Wolves','Knicks','Kings','Mavs','Pelicans','Hornets','Pistons','Nuggets','Heat','NETS']
#odds=[250,199,156,119,88,53,53,28,17,11,8,7,6,5,1]
#d=3
teams=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odds=[140,140,140,125,105,90,75,60,45,30,20,15,10,5]
d=4
'''Scenarios:
Kings fall out of top 10->Pick goes to Bulls
Kings move above Sixers->Swap picks
Lakers fall out of top three->Pick goes to Sixers
Pelicans fall out of top three->Pick goes to Kings
'''
def drawing():
    x=list(range(14))
    y=[]
    for i in range(13,9,-1):
        t=randint(0,i)
        y.append(x[t])
        del x[t]
    return y
def draw(a,w=True):
    for i in a:
        if w:
            print(i)
            sleep(0.5)
def revpermute(a1,n):
    a=a1+[i for i in range(n) if not i in a1]
    b=[a[i]-len([j for j in a[:i] if j<a[i]]) for i in range(len(a))]
    c=[factorial(len(a)-i-1)*b[i] for i in range(len(b))]
    return sum(c)
class treeStructure(object):
    def __init__(self,node, loc = []):
        self.tree = []
        self.location = loc
        self.value = node
    def getNode(self,loc):
        a = self
        for i in loc:
            a = a.tree[i]
        return a
    def appendNode(self,node,loc):
        #print(self.getNode(loc))
        self.getNode(loc).tree.append(treeStructure(node, self.location+loc+[len(self.getNode(loc).tree)]))
    def __getitem__(self, key):
        for i in self.tree:
            if i.value == key:
                return i
    def getLevel(self,level):
        if level==0:
            return [self]
        a = self.tree
        count = 1
        while count<level:
            a = listsum(list(map(lambda x:x.tree,a)))
            count+=1
        return a
def listsum(arr):
    x = []
    for i in arr:
        x+=i
    return x
def ncr(n,k):
    n1=1
    for i in range(min(n-k,k)):
        n1*=(n-i)
    return int(n1/factorial(min(k,n-k)))
def revcombo(a1,n):
    a=[-1]+sorted(a1)
    l=len(a)
    b=[a[i]-a[i-1]-1 for i in range(1,l)]
    c=[sum(ncr(n-j-1,l-i-1) for j in range(a[i-1]+1,a[i])) for i in range(1,l)]
    return sum(c)
def team(x):
    i=-1
    while x>=0:
        i+=1
        x-=odds[i]
    return teams[i]
def pick(x,w=True):
    i=drawing()
    draw(i,w)
    x.append(team(revcombo(i,14)))
def draft(w=True,t=True):
    o=[]
    while len(list(set(o)))<d:
        pick(o,w)
        if w:
            print(o[-1])
    if t:
        print('Final Order:')
        a1=[o[i] for i in range(len(o)) if not o[i] in o[:i]]+[i for i in teams if not i in o]
        if a1.index('Kings')<a1.index('Sixers'):
            a1[a1.index('Kings')]='temp'
            a1[a1.index('Sixers')]='Kings (swapped)'
            a1[a1.index('temp')]='Sixers (swapped)'
        if a1.index('Lakers')>=3:
            a1[a1.index('Lakers')]='Sixers (from LAL)'
        if 'Kings' in a1 and a1.index('Kings')>=10:
            a1[a1.index('Kings')]='Bulls (from SAC)'
        if a1.index('Pelicans')>=3:
            a1[a1.index('Pelicans')]='Kings (from NOP)'
        print(a1)
    else:
        return [teams.index(o[i]) for i in range(len(o)) if not o[i] in o[:i]]
def draft18(w=True,t=True):
    o=[]
    while len(list(set(o)))<d:
        pick(o,w)
        if w:
            print(o[-1])
    if t:
        print('Final Order:')
        print([o[i] for i in range(len(o)) if not o[i] in o[:i]]+[i for i in teams if not i in o])
def partition(x,y,z=False):
    if not z:
        z=y
    return [x[i:i+z] for i in range(0,len(x),z)]
def nextpermute(y,s=True):
    x = [int(i) for i in y]
    for i in range(len(x)-1,-1,-1):
        if x[i]>x[i-1]:
            j = x.index(min(k for k in x[i:] if k>x[i-1]))
            x[i-1],x[j]=x[j],x[i-1]
            x[i:] = sorted(x[i:])
            break
    if s:
        return tostr(x)
    return x
def tostr(x):
    a = ''
    for i in x:
        a+=str(i)
    return a
o1=treeStructure(1)
for i in range(d):
    for j in o1.getLevel(i):
        for k in range(14):
            if not k in j.location and len(list(set(j.location)))==len(j.location):
                j.appendNode(j.value*odds[k]/(1000-sum(odds[l] for l in j.location)),[])
            else:
                j.appendNode(0,[])
def t3(l):
    a=[]
    for i in range(2*d):
        a.append(o1.getNode(l).value)
        a.append(l)
        l=nextpermute(l,False)
    b=[[list(map(lambda j:teams[j],a[i+1])),round(a[i]/sum(a[::2]),4)] for i in range(0,12,2)]
    return b
draft18(False)
print(100*sum(i.value for i in o1.getLevel(4) if max(i.location)>=12))
