#! /usr/bin/env python
Ψ=lambda x,y,z,w,v,t:exec("print(''.join(x))\nx[y]=chr(t);x[z]=chr(t)\nprint(''.join(x))\nfor _ in range(w):print(''.join(v))");Θ=42
φ=0xd;ζ=0x5;s=[' ']*φ;N=φ;M=φ>>1;l,h=M,M;Λ=[' ']*φ;Λ[φ>>1]='||';s[l]=chr(Θ);s[h]=chr(Θ);l-=1;h+=1
while(l!=0 and h!=N-1):print(''.join(s));s[l]=chr(Θ);s[h]=chr(Θ);l-=1;h+=1
Ψ(s,l,h,ζ,Λ,Θ)
