usw='USIndepEnd'
fob='Bastille'
mce='Macartney'
nap='Napoleon'
cov='CofVienna'
ir='IndustRev'
cm='ComManif'
opi='OpiumWar'
spr='SepoyReb'
ger='GerUnify'
bwa='BWAfrConf'
wwi='WWI'
oct='OctRev'
ppc='ParisConf'
tov='TofVersailles'
mor='MarchonRome'
smc='StockCrash'
ahc='AHChancellor'
spw='SpCivilWar'
jic='JapInCh'
ron='RofNanking'
mc='MunConf'
krn='Kristallnacht'
ww2='WW2'
ph='PHarbor'
bos='BofSGrad'
gc='GerCaps'
ab='ABombs'
cw='ColdWar'
isr='IsrIndep'
nam='VietnamWar'
cmc='CubaCrisis'
sdw='SixDayWar'

t={'jilly':[15,[usw,fob,cov,bwa,wwi,oct,ppc,mor,ahc,spw,ww2,ph,bos,gc,ab,cw]],
   'myles':[12,[ww2,wwi,oct,fob,nap,cw,tov,mor,ahc,fob,smc,ger,cm,opi]],
   'matt':[15,[fob,cm,ger,bwa,wwi,oct,ppc,ahc,jic,mc,ww2,ph,isr,sdw,cw]],
   'justin':[13,[nap,fob,ab,ron,cw,ahc,oct,bos,ph,ppc,bwa,mor,cmc,krn]],
   'serena':[15,[fob,mce,nap,cm,spr,bwa,wwi,oct,tov,ahc,ww2,ph,bos,gc,isr,cw]],
   'nick':[15,[wwi,ww2,oct,fob,ger,ahc,nam,cw,smc,mor,tov,cm,usw,cw,ph,ir]]}
c={usw:1,fob:1,mce:1,nap:0,cov:0,ir:0,cm:1,opi:0,spr:1,ger:1,bwa:1,wwi:1,oct:1,
   ppc:1,tov:1,mor:1,smc:1,ahc:1,spw:1,jic:0,ron:1,mc:0,krn:1,ww2:1,ph:1,bos:1,
   gc:1,ab:1,cw:1,isr:1,nam:1,cmc:1,sdw:0}
def f(a,b):
    print(a)
    for i in t[a][1]:
        if not i in t[b][1]:
            print(i)
    print('\n'+b)
    for i in t[b][1]:
        if not i in t[a][1]:
            print(i)
    print('\nboth')
    for i in t[a][1]:
        if i in t[b][1]:
            print(i)
    print('\n')
for i in list(t.keys()):
    for j in list(t.keys())[list(t.keys()).index(i)+1:]:
        f(i,j)
for i in list(t.keys()):
    print([i,sum(list(map(lambda x:c[x],t[i][1]))),list(map(lambda x:c[x],t[i][1]))])
print(list(c.keys()))