from copy import deepcopy,copy
class V:
    def __init__(self,a):
        self.a=[i for i in a]
        self.l=len(a)
    def __add__(self,b):
        return [self.a[i]+b.a[i] for i in range(self.l)]
def g(s):
    m1=[[int(i[j]) for j in range(len(i))] for i in s.split(',')]
    mc=max(len(i) for i in m1)+8
    return [[0]*mc]*4+[[0,0,0,0]+i+[0]*(mc-len(i)-4) for i in m1]+[[0]*mc]*4
def ip(g,p,pt,w):
    m1 = deepcopy(g)
    for k in p:
        t1 = V(k)+V(pt)
        if m1[t1[0]][t1[1]]!=1:
            return 0
        m1[t1[0]][t1[1]]=w
    return m1
def fr(p,r):
    q=deepcopy(p)
    if r[1]==1:
        q=[(-i[0],i[1]) for i in q]
    for i in range(r[0]):
        q=[(-j[1],j[0]) for j in q]
    return q
def ta(l,t):
    a=l
    for i in t:
        a=l[i]
    return a
def mp(x):
    for i in x:
        for j in i:
            print(j,end='')
        print()
def i2(l,e):
    try:
        return l.index(e)
    except ValueError:
        return -1
def solve(g,p):
    if len(p)==0:
        return [i[4:-4] for i in g[4:-4]]
    for j in pfr[p[0]]:
        j1=fr(p5[p[0]],j)
        for k in range(4,len(g)-4):
            for l in range(4,len(g[0])-4):
                g1=ip(g,j1,(k,l),p[0])
                if g1!=0:
                    g2=solve(g1,p[1:])
                    if g2:
                        return g2
    return 0
p5={'f':[(0,0),(1,0),(1,1),(1,-1),(2,1)],'i':[(0,0),(1,0),(2,0),(3,0),(4,0)],'l':[(0,0),(1,0),(2,0),(3,0),(3,1)],'n':[(0,0),(1,0),(2,0),(2,1),(3,1)],'p':[(0,0),(1,0),(0,1),(0,-1),(1,1)],'t':[(0,0),(1,0),(2,0),(1,1),(1,2)],'u':[(0,0),(0,1),(1,0),(2,0),(2,1)],'v':[(0,0),(1,0),(2,0),(0,1),(0,2)],'w':[(0,0),(1,0),(1,1),(2,1),(2,2)],'x':[(0,0),(1,0),(2,0),(1,1),(1,-1)],'y':[(0,0),(1,0),(2,0),(3,0),(2,1)],'z':[(0,0),(1,0),(2,0),(2,1),(0,-1)]}
tfr=[[0,0],[1,0],[2,0],[3,0],[0,1],[1,1],[2,1],[3,1],[4,1]]
tr=[[0,0],[1,0],[2,0],[3,0]]
pfr={'f':tfr,'i':[[0,0],[1,0]],'l':tfr,'n':tfr,'p':tfr,'t':tr,'u':tr,'v':tr,'w':tr,'x':[[0,0]],'y':tfr,'z':[[0,0],[1,0],[0,1],[1,1]]}
'''g11=g('11111,11111,11111,11111,11111')
print(fr(p5['f'],[2,0]))
mp(g11)
mp(ip(g11,fr(p5['f'],[3,1]),(5,5)))
g2=g('0101,1101,0111,0011')
print(ip(g2,fr(p5['f'],[3,1]),[5,5],'f'))
mp(g2)
print()
mp(solve(g2,['f','l']))
g3=g('111111,111111,11111111,11111111,111111,111111')
mp(solve(g3,['f','l','i','t','w','n','z','y']))'''
mp(solve(g('11111,11111,11111,11111,11111'),['p','u','t','f','y']))
