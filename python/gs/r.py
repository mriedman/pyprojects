from random import randint
from math import log
class Tile(object):
    def __init__(self,n,c):
        self.n=n-1
        self.c=(['r','g','b','bl'].index(c) if isinstance(c,str) else c)
    def __str__(self):
        return ['Red','Orange','Blue','Black'][self.c]+' '+str(self.n+1)
    def eq2(self,o):
        return self.n==o.n and self.c==o.c
    def in2(self,b):
        if any(self.eq2(i) for i in b):
            return True
        return False
class WildCard(Tile):
    def __init__(self,n=False,c=False):
        if (n or c):
            super().__init__(n,c)
            self.w=False
        else:
            self.w=True
    def __str__(self):
        return super().__str__()+' W'
    def set(self,n,c):
        self.n=n
        self.c=c
        self.w=False
    def unset(self):
        self.w=True
        del self.n
        del self.c
class Univ(object):
    def __init__(self,o):
        self.o=o
    def __eq__(self,a):
        self.o.n=1
        return True
def listsum(arr):
    x = []
    for i in arr:
        x+=i
    return x
def sortby(x,y):
    z=[x[0]]
    z1=[y(x[0])]
    for i in x[1:]:
        j=sortindex(z1,y(i))+1
        if y(i)<min(z1):
            j=0
        z.insert(j,i)
        z1.insert(j,y(i))
    return z
def sortindex(x,y,z = 0):
    if len(x)==1:
        return z
    if x[int(len(x)/2)]>y:
        return sortindex(x[:int(len(x)/2)],y,z)
    return sortindex(x[int(len(x)/2):], y,z+int(len(x)/2))
lmstr=lambda x:list(map(str,x))
def hand(t):
    r=[]
    for i in range(35):
        x=randint(0,len(t)-1)
        r.append(t[x])
        del t[x]
    return r
def run(h):
    h0=[[[j for j in h if j.n==i and j.c==k] for i in range(13)] for k in range(4)]
    h00=[[i.n for i in h if i.c==j] for j in range(4)]
    h1=[[[] for j in range(4)] for i in range(13)]
    for i in h:
        h1[i.n][i.c].append(i)
    h1=[[j for j in i if len(j)] for i in h1]
    rs=[]
    for i1 in range(4):
        i0=h00[i1]
        for i in range(13):
            if all(j in i0 for j in range(i,i+3)):
                rs.extend(c(h0[i1][i:i+3]))
                i2=4
                while all(j in i0 for j in range(i,i+i2)):
                    rs.extend(c(h0[i1][i:i+i2]))
                    i2+=1
    for i in h1:
        if len(i)==3:
            rs.extend(c(i))
        if len(i)==4:
            rs.extend(listsum(list(map(c,[i for i in onoff(i) if len(i)>2]))))
    return rs
def c(l):
    f=[[]]
    for i in l:
        f=[k+[j] for k in f for j in i]
    return f
def draw(h,t):
    x=randint(0,len(t)-1)
    h.append(t[x])
    del t[x]
def onoff(l):
    return [[l[i] for i in range(len(l)) if j%2**i!=j%2**(i+1)] for j in range(2**len(l))]
def totile(h):
    return list(map(lambda i:(Tile(i[0],i[1]) if len(i)==2 else (WildCard(i[0],i[1]) if len(i)==3 else WildCard())),h))
def full(ex,h,p=[]):
    if len(h)==0:
        return [p]
    rs=run(h+ex)
    if len(rs)==0:
        return []
    f=[]
    for i in rs:
        if h[0] in i:
            f.extend(full([j for j in ex if not j in i],[j for j in h if not j in i],p+[i]))
    return f
def pfull(l,t):
    print(list(map(lambda x:list(map(lambda y:lmstr(y),x)),l)))
    print(len(l))
    f=sortby(list(map(lambda x:list(map(lambda y:lmstr(y),x)),l)),lambda x:len(listsum(x)))[-1]
    if len(listsum(f))==len(t):
        print('None')
        return
    print(f)
tiles=[Tile(i,j) for i in range(13) for j in range(4) for k in range(2)]+[WildCard(),WildCard()]
h=totile(list(map(lambda x:[int(x.split(',')[0])]+x.split(',')[1:],input('Hand: ').split(' '))))
ts=totile(list(map(lambda x:[int(x.split(',')[0])]+x.split(',')[1:],input('Tiles: ').split(' '))))
print(lmstr(h))
print(lmstr(ts))
print(list(map(lambda x:lmstr(x),run(h))))
print(list(map(lambda x:lmstr(x),run(ts))))
pfull(full(h,ts),ts)
'2,0 4,0 6,0 10,0 3,1 8,1 11,1 3,2 11,2 9,1 10,1 6,0'
'3,3 4,3 5,3 10,3 11,3 12,3 9,1 8,1 11,1 9,1 10,1 0,1 0,2 0,3 3,1 4,1 5,1 7,1 7,2 7,3 11,2'
'3,r 5,r 7,r 11,r 4,o 9,o 12,o 4,b 12,b 10,o 7,r'
'4,bl 5,bl 6,bl 1,o 1,b 1,bl 11,bl 12,bl 13,bl 9,o 10,o 11,o 12,o 4,o 5,o 6,o 8,o 8,b 8,bl'
'1,bl 1,bl 13,bl 10,g 10,g 12,g 9,r 11,r 13,r 3,b 7,b 8,b 12,b 1,b 2,b 2,bl 3,bl 1,r 2,g 3,g 4,g 5,bl 2,r 2,r 3,r 4,r 5,r'
'3,g 4,g 5,g 6,g 7,g 8,g 10,r 11,r 12,r 7,b 8,b 9,b'