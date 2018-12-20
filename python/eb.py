n=250
l=[]
l2=[]
sol=[]
intf=lambda x,y:int((x**2+y**2)**(1/2))**2==x**2+y**2
for i in range(6):
    l1=[132,12,12]
    l1[i%3]/=3
    l1[int(i/3%3)]/=4
    l.append(l1)
for i in l:
    i1=[]
    for j in i:
        i1.append(list(range(1,int(n/j)+1)))
    l3=[[]]
    for j in range(3):
        l3=[k+[j1] for k in l3[:] for j1 in i1[j]]
    l2+=[[int(i[j]*k[j]) for j in range(3)] for k in l3]
print(l2)
for i in l2:
    if intf(i[0],i[1]) and intf(i[1],i[2]) and intf(i[0],i[2]):
        sol.append(i)
sol=[sorted(i) for i in sol]
sol1=[]
for i in sol:
    if not i in sol1:
        sol1.append(i)
print(sol1)