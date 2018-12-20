from random import randint
def liststr(x):
    s=''
    for i in x:
        s+=i
    return s
def grid(x,r,c):
    g2=['|'+liststr([' '*(4-len(str(x[(i,j)])))+str(x[(i,j)])+'|' for j in range(c)]) for i in range(r)]
    for i in range(0,2*r,2):
        g2.insert(i,'|    '*c+'|')
    for i in range(0,3*r,3):
        g2.insert(i,'|----'*c+'|')
    for i in g2:
        print(i)
    print('|----'*c+'|')
    print('Score: '+str(x['s']))
def move(x,y1,r,c):
    y0=y1.split(' ')
    if len(y0)==2:
        v=int(y0[1])
    elif len(y0)==r*c:
        tm={(i,j):(int(y0[c*i+j]) if y0[c*i+j]!='.' else '') for i in range(r) for j in range(c)}
        tm['s']=x['s']
        return tm
    else:
        v=2 if randint(1,7)==1 else 1
    y=y0[0].upper()
    try:
        t={'U':[1,1],'D':[1,0],'L':[0,1],'R':[0,0],'':[2]}[y]
    except KeyError:
        return x
    if t[0]==2:
        return x
    sc=x['s']
    r1=(r if t[0]==0 else c)
    c1=(c if t[0]==0 else r)
    arr=[[x[((j,i) if t[0]==0 else (i,j))] for i in (range(c1) if t[1]==1 else range(c1-1,-1,-1))] for j in range(r1)]
    arr2=[]
    for i in arr:
        i=[j for j in i if j!='']
        for j in range(len(i)-1):
            if i[j]==i[j+1]:
                i[j]=2*i[j]
                sc+=i[j]
                i[j+1]=''
        i=[j for j in i if j!='']
        i+=['']*(c1-len(i))
        arr2.append(i)
    l={}
    for i in range(r):
        for j in range(c):
            i1,j1=((j,(i if t[1]==1 else r-1-i)) if t[0]==1 else (i,(j if t[1]==1 else c-1-j)))
            l[(i,j)]=arr2[i1][j1]
    l2 = [i for i in l if l[i] == '']
    if len(l2) == 0:
        print('You Lose!')
        return x
    l[l2[randint(0,len(l2)-1)]]=2**v
    l['s']=sc
    return l
rs=int(input('Rows: '))
cs=int(input('Columns: '))
g={(i,j):'' for i in range(rs) for j in range(cs)}
g['s']=0
sc=0
while True:
    s1=input('Move? ')
    if s1=='No':
        break
    g=move(g,s1,rs,cs)
    grid(g,rs,cs)