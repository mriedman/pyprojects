from random import randint
def sortindex(x,y,z = 0):
    if len(x)==1:
        return z
    if x[int(len(x)/2)]>y:
        return sortindex(x[:int(len(x)/2)],y,z)
    return sortindex(x[int(len(x)/2):], y,z+int(len(x)/2))
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
def listsum(l):
    r=[]
    for i in l:
        r+=i
    return r
def hand(t):
    r=[]
    for i in range(15):
        x=randint(0,len(t)-1)
        r.append(t[x])
        del t[x]
    return r
def start(h,n):
    a0=branch(h,n)
    if len(a0)==0:
        return []
    return a0[-1]
def branch(t,n):
    bs=[i for i in t if n in i]
    a0=listsum([[[b]+i for i in branch([j for j in t if j!=b],nfi0(b,n))] for b in bs])+[[b] for b in bs]
    if len(a0)==0:
        return []
    return sortby(a0,len)
def nfi0(l,n):
    l1=list(l)
    l1.remove(n)
    return l1[0]
ls1=[]
'''for i in range(100000):
    tile = [(i,j) for i in range(25) for j in range(25) if i<=j]
    ts=hand(tile)
    j=start(ts,9)
    ls1.append(len(j))
    if len(j)==12.5:
        print(ts)
        print(j)
        print(len(j))
print([ls1.count(i) for i in range(15)])'''
print(start(list(map(lambda x:tuple(list(map(int,x.split(',')))),input('Tiles: ').split(' '))),int(input('Number: '))))