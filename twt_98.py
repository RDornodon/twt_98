import math
for I in[I:=input]*int(I()):
 X,Y=map(int,I().split());A=B=0;C=[]
 if math.gcd(X,Y)<2:
  while(c:=A*X+B*Y)!=1:A-=c>1;B+=c<1
  C=[[A*A+B*B,A,B]];A=B=0
  while(c:=A*X+B*Y)!=1:A+=c<1;B-=c>1
  C+=[[A*A+B*B,A,B]];C=sorted(C)[0][1:]
 print(*C or['IMPOSSIBLE'],sep=',')