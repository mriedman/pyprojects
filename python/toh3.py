a=[[0,1,2,3,4],[0,0,0,0,4],[0,0,0,0,4]]
def m(x,y,n=2):
    a,b=len(x[y[1]])-x[y[1]][::-1].index(0)-1,len(x[y[0]])-x[y[0]][::-1].index(0)
    if x[y[0]][b]<x[y[1]][a+1]:
        x[y[1]][a]=x[y[0]][b]
        x[y[0]][b]=0
def pt(x):
    for i in range(1,len(x[0])-1):
        for j in range(len(x)):
            if x[j][i]==0:
                print('  ',end='')
            else:
                print(str(x[j][i])+' ',end='')
        print()
    print('-----')
def rm(x,y):
    for i in y:
        m(x,i)
    return x
def ac(a,b,c):
    return [c[b.index(i)] for i in a]
def solve(n):
    a=[[],[[0,1]]]
    for i in range(2,n+1):
        c,c1=a[i-1][-1][1],len(a[-1])
        b=[c,(1-i%2)*(3-c),i%2*(3-c)]
        a.append(a[-1]+[[0,b[1]+b[2]]]+list(map(ac,a[-1],[[0,1,2]]*c1,[b]*c1)))
    return a[-1]
def s(n):
    return [list(range(n+2))]+[[0 for j in range(n+1)]+[n+1] for i in range(2)]
pt(rm(s(10),solve(10)))
