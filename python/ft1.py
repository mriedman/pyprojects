from math import floor,factorial
n=4
t=[]
def nextdown(n,m=False):
    if not m:
        m=n
    if m==1:
        return [[n]]
    t1=[]
    for i in range(floor(n/m)+1):
        t1+=[[i]+j for j in nextdown(n-i*m,m-1)]
    return t1
def diff(a1):
    return [a1[i] - a1[i - 1] for i in range(1, len(a1))]
def nestdiff(x,n):
    t=[x]
    y=[i for i in x]
    for i in range(n):
        y=diff(y)
        t.append(y)
    return t
def ncr(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))
a1=[len(nextdown(i)) for i in range(1,30)]
print(nextdown(6))
