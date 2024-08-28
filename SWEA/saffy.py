N=int(input())
l=[(4,4),(4,3),(1,3),(2,2),(4,4),(1,4),(2,1),(4,3),(2,4),(4,4),(4,4),(2,2),(1,1),(3,3),(4,1),(2,1),(4,1),(2,2),(1,2),(1,3)]
ans=0
road = 0

for j in range(N):
    cnt=0
    oil=0
    road=0
    while cnt!=N:
        oil+=int(l[j][0])
        road+=int(l[j][1])
        if oil>=road:
            pass
        else:
            break
        cnt+=1
    if cnt==N:
        ans+=1
print(ans)
        
