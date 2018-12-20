def deck(x):
    a = []
    for i in range(2,12):
        for j in range(4*x):
            a.append(i)
    for i in range(12*x):
        a.append(10)
    return a
def value1(x0,y0,z,v=1):
    if x0>y0:
        y,x=x0,y0
    else:
        x,y=x0,y0
    if y==x:
        if z==y:
            return 30*v
        return 0
    if x<z<y:
        if y-x==2:
            return 10*v
        if y-x==3:
            return 6*v
        if y-x==4:
            return 4*v
        return v
    return -v
def pick(x):
    a=[]
    for i in x:
        b=[]
        for j in range(len(i[1])):
            b.append([i[0]+[i[1][j]],i[1][:j]+i[1][j+1:]])
        a+=b
    return a
def value(x):
    d=deck(x)
    dl=len(d)
    a=[[[],d]]
    for i in range(3):
        a=pick(a)
    a1=list(map(lambda x:value1(*x[0]),a))
    return sum(a1)/(dl*(dl-1)*(dl-2))
print(value(1))
print(pick([[[],deck(1)]]))
'30 10 6 4 1'