import csv
txt=[]
with open('nflg.csv', newline='') as csvfile:
    txt = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
print(txt)
txt2=[]
with open('nfld.csv', newline='') as csvfile:
    txt2 = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
print(txt)
print(txt2)
wk=[[] for i in range(17)]
for i in txt:
    wk[int(i[0])-1].append(i[4:7]+[-1 if j=='' else int(j) for j in i[8:10]])
print(wk)
f=open('nflt.js','w')
f.write('gr='+str(wk)+'\ntd='+str(txt2))