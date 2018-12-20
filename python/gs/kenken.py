class b(object):
    def __init__(self,s):
        a=s.split(',')
        a=[0,'.'*len(a[1])]+a
        self.l=len(a[1])
        self.pl=[i for i in [2,3,5,7,11,13] if i<=self.l]
        self.mt={i:[j for j in range(1,self.l+1) if j%i==0 and all(j%k!=0 for k in self.pl[self.pl.index(i)+1:])] for i in self.pl}
        self.fl=[0]+[self.f(i) for i in range(1,self.l+1)]
        self.c={}
        self.bx=[]
        bx={}
        c0={}
        for i in range(2,len(a),2):
            a0=self.br1(a[i],int(i/2-1))
            b0=self.br2(a[i-1])
            for j in a0:
                if j[0]!='uk':
                    bx[j[0]]=[j[1],None]
                else:
                    for k in j[1]:
                        if k[0] in b0:
                            j[0]=c0[(k[0],k[1]-1)][0]
                            break
                    bx[j[0]][0]+=j[1]
                for k in j[1]:
                    c0[k]=[j[0],list(range(1,self.l+1))]
        for i in bx:
            self.bx.append(bx0(i,len(bx[i][0]),self.cr(bx[i][0])))
            self.bx[-1].ac(*bx[i][0])
            i0=0
            for i in self.bx[-1].c:
                self.c[i]=c(self.bx[-1],list(range(1,self.l+1)),i,i0)
                i0+=1
    def cr(self,x):
        return min(len(list(set(j[i] for j in x))) for i in [0,1])
    def br1(self,x,r):
        def nt(i):
            return i in [str(j) for j in range(100)]
        def op(i):
            return i in ['+', '-', 'x', '/','n']
        a,j,m,n=[[[]]],0,False,''
        for i in x:
            if i=='.':
                a.append([[]])
            elif i==' ':
                a[-1][-1].append((j,r))
                j+=1
            elif nt(i):
                if m:
                    n+=i
                else:
                    m,n=True,i
            elif op(i):
                m=False
                a[-1]=[(int(n),i,(j,r)),[(j,r)]]
                j+=1
            else:
                raise ValueError(i+' is not a valid character')
        for i in range(len(a)):
            if len(a[i])==1:
                a[i]=['uk']+a[i]
        return a
    def br2(self,x):
        a=[]
        j=0
        for i in x:
            if i==' ':
                a.append(j)
            j+=1
        return a
    def binit(self):
        mn0=lambda x:[[i,i+x] for i in range(1,self.l-x+1)]
        dv0=lambda x:[[i,i*x] for i in range(1,int(self.l/x+1))]
        for i in self.bx:
            if i.o=='-':
                i.cbg=mn0(i.n)
            if i.o=='/':
                i.cbg=dv0(i.n)
            if i.o=='x':
                i.cbg=self.ml(i.n,i.b,r0=i.cr)
            if i.o=='+':
                i.cbg=self.ps(i.n,i.b)
            if i.o=='n':
                i.cbg=[[i.n]]
            i.cbs=i.apm()
    def ml(self,x,n,l=[[]],p=[17,100],r=10,r0=3):
        if r==10:
            r=r0
        def ins(x,y):
            for i in range(len(y)):
                if x<y[i]:
                    return y[:i]+[x]+y[i:]
            return y+[x]
        if x==1:
            if n<=r:
                return [[1]*n+i for i in l]
            else:
                return []
        if n==0:
            return []
        f=self.f(x)
        f0=0
        for i in self.pl[-1::-1]:
            if f[i]>0:
                f0=i
                break
        a=[]
        for i in self.mt[f0]:
            if x%i==0 and (f0<p[0] or i<p[1]):
                a+=self.ml(int(x/i),n-1,[ins(i,j) for j in l],[f0,i],r0=r0)
            if x%i==0 and i==p[1] and r>0:
                a+=self.ml(int(x/i),n-1,[ins(i,j) for j in l],[f0,i],r=r-1,r0=r0)
        return a
    def ps(self,x,n0):
        n=n0-1
        a,a0=list(range(1,n+1)),list(range(x-n,x))
        b=[[i for i in a]]
        i=0
        while a!=a0 and i<100:
            i+=1
            c=n-1
            while c>=0:
                if a[c]!=a0[c]:
                    a[c]+=1
                    aci=lambda i:a[c]+(a[c]-(a[c-1] if c>0 else 0))*i
                    if aci(n-c)<=x:
                        for i in range(1,n-c):
                            a[c+i]=aci(i)
                        break
                    a[c]-=1
                c-=1
            if a==b[-1]:
                if b[-1][-1]>=x:
                    del b[-1]
                break
            b.append([i for i in a])
        c=[]
        for i in b:
            d=[]
            for j in range(len(i)+1):
                q=([0]+i+[x])[j+1]-([0]+i+[x])[j]
                if q<=self.l:
                    d.append(q)
                else:
                    break
                if j==len(i):
                    c.append(d)
        return c
    def f(self,n):
        a={i:0 for i in self.pl}
        for i in a:
            while n%i==0:
                a[i]+=1
                n=int(n/i)
        return a
    def cred1(self):
        for i in self.c:
            a=[False]*self.l
            ci=self.c[i]
            for j in ci.bx.cbs:
                a[j[ci.o]-1]=True
            ci.nl=[i for i in range(1,self.l+1) if i in ci.nl and a[i-1]]
    def cred2(self):
        def s(x):
            tb=lambda y,n:[int(y/2**i)%2 for i in range(n)]
            c=[]
            for i0 in range(1,2**len(x)-1):
                i=tb(i0,len(x))
                a,k=[],0
                for j in range(len(x)):
                    if i[j]==1:
                        a+=x[j]
                        k+=1
                if len(list(set(a)))==k:
                    c.append(sorted(list(set(a))))
            return c
        gr=lambda x:[[self.c[(i,x)].nl,(i,x)] for i in range(self.l)]
        gc=lambda x:[[self.c[(x,i)].nl,(x,i)] for i in range(self.l)]
        grc=[gr,gc]
        for i0 in range(2):
            for i in range(self.l):
                r=grc[i0](i)
                r1=[i[0][0] for i in r if len(i[0])==1]
                r2=[i for i in r if len(i[0])!=1]
                r3=s(list(map(lambda x:x[0],r2)))
                for j1 in r2:
                    j=j1[0]
                    j0=0
                    for k in range(len(j)):
                        if j[k-j0] in r1:
                            self.bred(j1[1],j[k-j0])
                            del j[k-j0]
                            j0+=1
                    for k in r3:
                        if any(not l in k for l in j):
                            l0=0
                            for l in range(len(j)):
                                if j[l-l0] in k:
                                    self.bred(j1[1],j[l-l0])
                                    del j[l-l0]
                                    l0+=1
    def bred(self,c,n):
        b=self.c[c].bx
        j=0
        for i in range(len(b.cbs)):
            if b.cbs[i-j][self.c[c].o]==n:
                del b.cbs[i-j]
                j+=1
    def solve(self):
        self.binit()
        for i in range(20):
            self.cred1()
            self.cred2()
        for i in range(self.l):
            print([self.c[(j,i)].nl for j in range(self.l)])
class bx0(object):
    def __init__(self,noc,b,cr):
        self.n,self.o,self.ic=noc
        self.b=b
        self.cr=cr
        self.c=[]
        self.cbg=[]
        self.cbs=[]
    def ac(self,*c):
        for i in c:
            self.c.append(i)
    def __str__(self):
        return str([self.n,self.o,self.c,self.ic,self.b,self.cr,self.cbg])
    def apm(self):
        c=[]
        for x in self.cbg:
            a=list(range(self.b))
            b=[i for i in a[-1::-1]]
            c0=[[i for i in x]]
            if self.ic1(c0[0]):
                c+=c0
            while a!=b:
                a=self.nextpermute(a)
                c0=[x[i] for i in a]
                if (not c0 in c) and self.ic1(c0):
                    c.append(c0)
        return c
    def nextpermute(self,y):
        x=[int(i) for i in y]
        for i in range(len(x)-1,-1,-1):
            if x[i]>x[i-1]:
                j=x.index(min(k for k in x[i:] if k>x[i-1]))
                x[i-1],x[j]=x[j],x[i-1]
                x[i:] = sorted(x[i:])
                break
        return x
    def ic1(self,x):
        a=[[[] for i in range(16)] for j in range(2)]
        for i in range(self.b):
            for i0 in range(2):
                a[i0][self.c[i][i0]].append(x[i])
        for i in a:
            for j in i:
                if len(j)>len(list(set(j))):
                    return False
        return True
class c(object):
    def __init__(self,b,n,c,o):
        self.bx=b
        self.nl=n
        self.c=c
        self.o=o
'''a=b('6+.12x  , ..., .2/ .2-, .. , .12x.24x. ,.  .,  .  ')'''
'''a=b('11+ .8+  .3-,..... ,12x .3-.6x . ,..  ..,10+.4-. . .13+.3/,  ..  , . .48x.  . , . ..., .4x.  .3-.24x,. ..  ,  .2- . . ')'''
'''a=b('4-.5- .4/ .1- .16+, ...... , .14x .2/.28x .5n. ,...  .. ,20+.640x . . .4x . ,   ... ., .  .14x.2-.9x. .12+, ..   . , .15+ . . .  . , ...... , .5n.4x .90x .336x. ,...  . .,15+.1- . . .  .23+, ...... ,   .1- .   ')'''
a=b('3/ .16x .48x .2- ,...  ...,1- .24x. . .4-.56x ,.. .. ..,3/.2/. .2/ . .4-.3-,  ....  , . .24x .35x . . ,........,14+ .49x .80x .13+ , . .. . , .3+. .1- . .4-. ,. .... .,1-. .105x.11+.4-.10+. .2/, .    . , .  . . .  . ')
print(a.pl)
a.solve()
