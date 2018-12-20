def pcw(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j],end='')
        print()
def ew(w,x,y,d):
    for i in range(y[1-d],len(w)+y[1-d]):
        if d==0:
            x[y[0]][i]=w[i]
        else:
            x[i][y[1]]=w[i]
def tostrs(x):
    y1=[]
    y=''
    for i in x+[' ']:
        if i==' ':
            if y!='':
                y1.append(y)
                y=''
        else:
            y+=i
    return y1
def gws(x):
    return [[tostrs(x[i]) for i in range(len(x))]]+[[tostrs([x[i][j] for i in range(len(x))]) for j in range(len(x[0]))]]
a=[[' ','n','a','i','l'],['s','a','l','m','a'],['h','o','i','s','t'],['e','m','c','e','e'],['d','i','e','t',' ']]
pcw(a)
ew('lllll',a,(0,2),1)
pcw(a)
print(gws(a))
print(len(open('cws1.txt').read().split('\n')))

