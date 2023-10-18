import sys
input = sys.stdin.readline
cnt = 0

while(True):
    cnt += 1
    l,p,v = map(int,input().split())
    if (l,p,v) == (0,0,0):
        break
    print("Case ",cnt,": ",v//p*l + min(l,v-v//p*p), sep="")
