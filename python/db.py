class Boxes:
    def __init__(self,r,c):
        self.rcs=[[0]*(c+2)]
        for i in range(r+2):
            self.rcs+=[[0]*(c+3),[0]*(c+2)]
        self.b=[[0]*(c+1) for i in range(r)]
        self.r=r
        self.c=c
    def cb(self,r,c,t):
        if r%2==0:
            if min(self.rcs[r-1][c],self.rcs[r-1][c+1],self.rcs[r-2][c])==1:
                self.b[int(r/2)-2][c]=t
            if min(self.rcs[r+1][c],self.rcs[r+1][c+1],self.rcs[r+2][c])==1:
                self.b[int(r/2)-1][c]=t
        else:
            if min(self.rcs[r+1][c-1],self.rcs[r-1][c-1],self.rcs[r][c-1])==1:
                self.b[int((r-3)/2)-2][c-2]=t
            if min(self.rcs[r+1][c],self.rcs[r-1][c],self.rcs[r][c+1])==1:
                self.b[int((r-3)/2)][c-1]=t
    def tm(self,t):
        try:
            r=int(input("Row: "))
            c=int(input("Column: "))
        except ValueError:
            self.tm(t)
            return
        self.tc(r,c,t)
    def tc(self,r,c,t):
        self.rcs[r][c]=1
        self.cb(r,c,t)
        print(self)
    def __str__(self):
        a=''
        a0='    '
        for i in range(2,2*self.r+3):
            a+=str(i)+('  ' if i<10 else ' ')
            for j in range(1,self.c+2):
                if i==2:
                    a0+=str(j)+('   ' if j<10 else '  ')
                if i%2==0:
                    a+='+'
                    a+=('---' if self.rcs[i][j]==1 else '   ')
                else:
                    a+=('| ' if self.rcs[i][j]==1 else '  ')
                    a+=(str(self.b[int((i-3)/2)][j-1])+' ' if self.b[int((i-3)/2)][j-1]!=0 else '  ')
            a+='\n'
        return a0+'\n'+a
a1=Boxes(2,5)
print(a1)
for i in range(10):
    a1.tm(i%2)