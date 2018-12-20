from math import floor,ceil
nextl = lambda a:[i+2*floor(i/2) for i in a]
m=[[10,10,10,10,10,10],[16,12,13,13,12,17],[13,8,16,13,16,29],[8,13,12,16,17,45]]
anextl = lambda a:[ceil(i/2) for i in a]
b=list(map(anextl,m))[1:]
e=[[m[i][j]-b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
print(m)
print(b)
print(e)
sep=lambda a:[[i[:3] for i in a],[i[3:] for i in a]]
print(sep(b))
r=[[e[i][j]/m[i][j] for j in range(len(b[0]))] for i in range(len(b))]
print(list(map(lambda a:[round(i,2) for i in a],r)))