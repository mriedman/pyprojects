n=[0,'meth','eth','prop','but','pent','hex','sept','oct','non','dec']
n2=[0,'','di','tri','tetra','penta','hexa','hepta','octa','nona','deca']
def i1(x,b=False):
    if not b:
        b=[0]
    a=[]
    for i in range(x,0,-1):
        a.append([0])
        for j in range(1,i):
            print(a)
            for k in range(min(j,i-j,x-i-sum(i for i in a[-1]))+1):
                i0=len(a)-1
                for l in i1(x-i-sum(i for i in a[-1]),a[-1]):
                    a+=[[m for m in a[-1]]+l]
                del a[i0]
    b=[]
    for i in a:
        b+=i
    return b
print(i1(5))