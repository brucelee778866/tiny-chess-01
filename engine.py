import json,os,random
import urllib.request as q
W=os.environ["MAKEFUN_ENV_URL"]
V=(0,82,337,365,477,1025,0);PB=(0,20,30,50,80,120,160,0)
S="0000122,1/.0000411252246::::0000&(**(,00*023*134*034*123(,01&(**,....000.012.112.022.222.100,...00001222/000/000/000/000/0000001,../.000.011/0110011.111.010,../*((&*((&*((&*((&,**(.,,,44004620"
def CN(j):return 3-max(3-(j&7),(j&7)-4,3-(j>>3),(j>>3)-4)
T=[[(ord(S[i*32+(j>>3)*4+(j&7 if j&7<4 else 7-(j&7))])-48)*5 for j in range(64)] for i in range(6)]
T+=[[CN(j)*25-35 for j in range(64)]]
ND=(-33,-31,-18,-14,14,18,31,33)
KD=(-17,-16,-15,-1,1,15,16,17)
BD=(-17,-15,15,17)
RD=(-16,-1,1,16)
SD=BD+RD
R=random.Random(12345)
H=[R.getrandbits(64) for _ in range(1561)]
K='tm1!&45.3!%\'9RC!-5m$X!&%OQf!&-l4h!\'6W%)"08?*2"\'6P/G",4D1Z",4QCk"08RLD#%\'3j+%%\'HEP%)9flg%,<AHu%;D[p.\'6Ebuq\'+3)F((%\'&ZW*)10u`*%\'t,(,,<EXQ,\'65t6-$6Bj_."3J5H0&/Os)1&;`aO2\'6O#Q3&-mWe4\'6;@m4-=[1*6"3&q96;D6n/8=7rWB8#GX.=9#*%dF9"3REV9)1EdX9\'6o&J;"3'
BK={}
for i in range(0,len(K),6):
 k=sum((ord(K[i+j])-33)*85**j for j in range(4));f=ord(K[i+4])-33;t=ord(K[i+5])-33;BK[k]=chr(97+f%8)+chr(49+f//8)+chr(97+t%8)+chr(49+t//8)
HZ=H[1536]
B=[0]*128
side=1;castle=0;ep=-1;half=0;hsh=0
KP=[4,116]
UU=[];TT={};KL=[[0,0] for _ in range(128)];Y=[0]*16384
REP={};PTH=[]
nodes=0;AB=0;NODES=110000
def ZK(p,s):return H[((abs(p)-1)*2+(p<0))*128+s]
def CM(s):return ((s&7==0)*2+(s&7==7))*((s<8)+(s>111)*4)
def F(f):
 global B,side,castle,ep,half,hsh,KP
 B=[0]*128;KP=[4,116];p=f.split();h=0
 for r,row in enumerate(p[0].split("/")):
  c=0
  for ch in row:
   if ch.isdigit():c+=int(ch)
   else:
    s=(7-r)*16+c;v="PNBRQK".index(ch.upper())+1
    if ch.islower():v=-v
    B[s]=v;h^=ZK(v,s)
    if abs(v)==6:KP[0 if v>0 else 1]=s
    c+=1
 side=1 if p[1]=="w" else -1;castle=sum(1<<"KQkq".index(c) for c in p[2] if c in "KQkq")
 ep=-1
 if p[3]!="-":ep=ord(p[3][0])-97+(int(p[3][1])-1)*16
 half=int(p[4])
 if side<0:h^=HZ
 h^=H[1537+castle]
 if ep>=0:h^=H[1553+(ep&7)]
 hsh=h
def A(q,w):
 for t in ((q-15,q-17) if w else (q+15,q+17)):
  if not t&0x88 and B[t]==(1 if w else -1):return 1
 for dd in ND:
  t=q+dd
  if not t&0x88 and B[t]==(2 if w else -2):return 1
 for dd in KD:
  t=q+dd
  if not t&0x88 and B[t]==(6 if w else -6):return 1
 for dd in SD:
  t=q+dd
  while not t&0x88:
   x=B[t]
   if x:
    if (x>0)==w and abs(x) in ((3,5) if dd in BD else (4,5)):return 1
    break
   t+=dd
 return 0
def G():
 ms=[];w=side>0
 for s in range(128):
  p=B[s]
  if not p or (p>0)!=w or s&0x88:continue
  a=abs(p)
  if a==1:
   d=16 if w else -16;t=s+d
   if not t&0x88 and not B[t]:
    pr=(t>>4)==(7 if w else 0)
    if pr:
     ms+=[s|(t<<7)|(k<<14) for k in (5,4,3,2)]
    else:
     ms.append(s|(t<<7))
     if (s>>4)==(1 if w else 6):
      t2=s+2*d
      if not B[t2]:ms.append(s|(t2<<7))
   for dd in (d-1,d+1):
    t=s+dd
    if t&0x88:continue
    if B[t] and (B[t]>0)!=w:
     pr=(t>>4)==(7 if w else 0)
     if pr:
      ms+=[s|(t<<7)|(k<<14) for k in (5,4,3,2)]
     else:ms.append(s|(t<<7))
    elif t==ep:ms.append(s|(t<<7))
  elif a==2 or a==6:
   for dd in ND if a==2 else KD:
    t=s+dd
    if t&0x88:continue
    if not B[t] or (B[t]>0)!=w:ms.append(s|(t<<7))
   if a==6 and s==(4 if w else 116):
    for dd,rd,rb in ((1,3,1),(-1,4,2)):
     if castle&(rb if w else rb*4):
      e1=s+dd;e2=s+2*dd;e3=s+3*dd
      if not B[e1] and not B[e2] and (dd>0 or not B[e3]) and B[s+rd*dd]==(4 if w else -4) and not A(s,not w) and not A(e1,not w) and not A(e2,not w):ms.append(s|((s+2*dd)<<7))
  else:
   for dd in BD if a==3 else RD if a==4 else SD:
    t=s+dd
    while not t&0x88:
     x=B[t]
     if x:
      if (x>0)!=w:ms.append(s|(t<<7))
      break
     ms.append(s|(t<<7));t+=dd
 return ms
def M(m):
 global side,castle,ep,half,hsh
 f=m&127;t=(m>>7)&127;pr=m>>14
 p=B[f];c=B[t];cq=t
 if abs(p)==1 and t==ep and not c:
  cq=t-16 if p>0 else t+16;c=-p
 UU.append((m,c,cq,castle,ep,half,hsh))
 hsh^=HZ;hsh^=ZK(p,f)
 if ep>=0:hsh^=H[1553+(ep&7)]
 if c:hsh^=ZK(c,cq)
 if abs(p)==6:
  castle&=~(3 if p>0 else 12)
  if t-f==2 or t-f==-2:
   rf,rt=(t+1,t-1) if t>f else (t-2,t+1)
   r=B[rf];B[rt]=r;B[rf]=0;hsh^=ZK(r,rf)^ZK(r,rt)
 else:castle&=~CM(f)
 if c:castle&=~CM(t)
 if castle!=UU[-1][3]:hsh^=H[1537+UU[-1][3]]^H[1537+castle]
 B[f]=0
 if cq!=t:B[cq]=0
 q=p
 if pr:q=pr if p>0 else -pr
 B[t]=q;hsh^=ZK(q,t)
 if abs(p)==6:KP[0 if p>0 else 1]=t
 if abs(p)==1 and (t-f==32 or t-f==-32):ep=(f+t)//2;hsh^=H[1553+(ep&7)]
 else:ep=-1
 half=0 if abs(p)==1 or c else half+1
 side=-side
def X():
 global side,castle,ep,half,hsh
 m,c,cq,cs,ep0,hf,hh=UU.pop()
 f=m&127;t=(m>>7)&127;pr=m>>14
 p=B[t];side=-side;castle=cs;ep=ep0;half=hf;hsh=hh
 B[f]=p if not pr else (1 if p>0 else -1);B[t]=0
 if c:B[cq]=c
 if abs(B[f])==6:
  KP[0 if B[f]>0 else 1]=f
  if t-f==2 or t-f==-2:
   rf,rt=(t+1,t-1) if t>f else (t-2,t+1)
   B[rf]=B[rt];B[rt]=0
def E():
 s=0;ph=0;wb=0;bb=0;WP=[0]*8;BP=[0]*8;kw=4;kb=116;RF=0;RB=0
 for q in range(128):
  p=B[q]
  if not p or q&0x88:continue
  a=abs(p);r=q>>4;f=q&7;i=r*8+f;j=i^56
  if a==1:
   if p>0:WP[f]|=1<<r
   else:BP[f]|=1<<r
  elif a<4:ph+=1
  elif a==4:ph+=2;RF|=(1<<f)if p>0 else 0;RB|=(1<<f)if p<0 else 0
  elif a==5:ph+=4
  if a==3:
   if p>0:wb+=1
   else:bb+=1
  if a==6:
   if p>0:kw=i
   else:kb=j
  else:
   v=V[a]+T[a-1][i if p>0 else j]
   s+=v if p>0 else -v
 if ph>24:ph=24
 s+=(T[5][kw]*ph+T[6][kw]*(24-ph))//24-(T[5][kb]*ph+T[6][kb]*(24-ph))//24
 s+=30*(wb>1)-30*(bb>1)
 for f in range(8):
  w=WP[f];b=BP[f]
  if RF>>f&1:s+=15 if not(w|b) else 8 if not b else 0
  if RB>>f&1:s-=15 if not(w|b) else 8 if not w else 0
  if w:
   n=w.bit_count()
   if n>1:s-=12*(n-1)
   if not ((WP[f-1] if f else 0)|(WP[f+1] if f<7 else 0)):s-=10*n
   m=w
   while m:
    lb=m&-m;r=lb.bit_length()-1
    if not ((BP[f-1] if f>0 else 0)|b|(BP[f+1] if f<7 else 0))>>(r+1):s+=PB[r]
    m-=lb
  if b:
   n=b.bit_count()
   if n>1:s+=12*(n-1)
   if not ((BP[f-1] if f else 0)|(BP[f+1] if f<7 else 0)):s+=10*n
   m=b
   while m:
    lb=m&-m;r=lb.bit_length()-1
    if not ((WP[f-1] if f>0 else 0)|w|(WP[f+1] if f<7 else 0))&((1<<r)-1):s-=PB[7-r]
    m-=lb
 return s
def SC(m,y):
 e=TT.get(hsh)
 if e and e[3]==m:return 1000000
 t=(m>>7)&127;f=m&127;v=B[t]
 if v:return V[abs(v)]*16-V[abs(B[f])]//16+100000
 pr=m>>14
 if pr:return 90000+pr*1000
 if m==KL[y][0]:return 9000
 if m==KL[y][1]:return 8000
 return Y[m&16383]
def Q(a,b,y,ev=None):
 global nodes,AB
 nodes+=1
 if nodes>NODES:AB=1;return 0
 ck=A(KP[0 if side>0 else 1],side<0)
 if ck:ms=G()
 else:
  st=side*E() if ev is None else ev
  if st>=b:return b
  if st>a:a=st
  if st+1100<a:return a
  ms=[m for m in G() if B[(m>>7)&127] or m>>14]
 ms.sort(key=lambda m:-SC(m,y))
 n=0
 for m in ms:
  M(m)
  if A(KP[0 if side<0 else 1],side>0):X();continue
  n+=1
  v=-Q(-b,-a,y+1)
  X()
  if AB:return 0
  if v>a:a=v
  if a>=b:return b
 if ck and not n:return -99990+y
 return a
def N(d,a,b,y):
 global nodes,AB,side,ep,half,hsh
 nodes+=1
 if nodes>NODES:AB=1;return 0
 al=a;e=TT.get(hsh)
 if e and e[0]>=d:
  if e[1]==0:return e[2]
  if e[1]==1 and e[2]>=b:return e[2]
  if e[1]==2 and e[2]<=a:return e[2]
 st=side*E()
 if d<=0:return Q(a,b,y,st)
 ck=A(KP[0 if side>0 else 1],side<0)
 if ck:d+=1
 if d>=3 and not ck and y>0 and st>=b:
  ep0=ep;hh=hsh
  if ep>=0:hsh^=H[1553+(ep&7)]
  hsh^=HZ;ep=-1;side=-side;half+=1
  v=-N(d-3,-b,-b+1,y+1)
  side=-side;ep=ep0;half-=1;hsh=hh
  if AB:return 0
  if v>=b:return v
 ms=G();ms.sort(key=lambda m:-SC(m,y))
 best=-10**9;bm=0
 for i,m in enumerate(ms):
  f=m&127;t=(m>>7)&127
  cap=bool(B[t]) or (abs(B[f])==1 and t==ep)
  M(m)
  if A(KP[0 if side<0 else 1],side>0):X();continue
  if REP.get(hsh,0)>=2:v=0
  elif REP.get(hsh,0)+PTH.count(hsh)>=2 and side*E()>=0:v=0
  else:
   PTH.append(hsh)
   if i==0:v=-N(d-1,-b,-a,y+1)
   else:
    v=-N(d-2 if i>2 and d>2 and not cap and not ck else d-1,-a-1,-a,y+1)
    if v>a and not AB:v=-N(d-1,-b,-a,y+1)
   PTH.pop()
  X()
  if AB:return 0
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:
   if not cap:KL[y][1]=KL[y][0];KL[y][0]=m;Y[m&16383]+=d*d
   break
 if best==-10**9:return -99990+y if ck else 0
 if not AB:
  if len(TT)>200000:TT.clear()
  TT[hsh]=(d,0 if al<best<b else 1 if best>=b else 2,best,bm)
 return best
def C(m):
 f=m&127;t=(m>>7)&127;pr=m>>14
 return chr(97+(f&7))+chr(49+(f>>4))+chr(97+(t&7))+chr(49+(t>>4))+("nbrq"[pr-2] if pr else "")
def D(u):
 f=ord(u[0])-97+(ord(u[1])-49)*16
 t=ord(u[2])-97+(ord(u[3])-49)*16
 pr=("nbrq".index(u[4])+2) if len(u)==5 else 0
 return f|(t<<7)|(pr<<14)
def RT(d):
 leg=[]
 for m in G():
  M(m)
  if not A(KP[0 if side<0 else 1],side>0):leg.append(m)
  X()
 if not leg:return 0,None
 leg.sort(key=lambda m:-SC(m,0))
 best=-10**9;bm=None;a=-10**9
 for m in leg:
  M(m)
  if REP.get(hsh,0)>=2:v=0
  elif REP.get(hsh,0)+PTH.count(hsh)>=2 and side*E()>=0:v=0
  else:
   PTH.append(hsh);v=-N(d-1,-10**9,-a,1);PTH.pop()
  X()
  if AB:return 0,None
  if v>best:best=v;bm=m
  if v>a:a=v
 if not AB:TT[hsh]=(d,0,best,bm)
 return best,bm
def CH(g):
 global REP,nodes,AB
 F(g["start_fen"]);REP={hsh:1}
 for u in g["moves"]:
  M(D(u));REP[hsh]=REP.get(hsh,0)+1
 UU.clear();F(g["fen"]);nodes=0;AB=0;best=None
 bk=BK.get(hsh&16777215)
 if bk and bk in g["legal_moves"]:return bk
 for d in range(1,65):
  v,bm=RT(d)
  if AB:break
  if bm is not None:best=bm
 if best is None:best=D(g["legal_moves"][0])
 return C(best)
def post(p,b):
 try:
  return json.load(q.urlopen(W+p,json.dumps(b).encode()))
 except Exception:return {"e":0}
def main():
 cg=0
 while 1:
  g=post("/game",{})
  if g.get("status")=="done":break
  if g["game"]!=cg:TT.clear();cg=g["game"]
  while g.get("status")=="your_move":
   r=post("/move",{"game":g["game"],"move":CH(g)})
   if "e" in r:r=post("/move",{"game":g["game"],"move":g["legal_moves"][0]})
   g=r
if __name__=="__main__":main()
