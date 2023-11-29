N,x = map(int,input().split())
l = sorted(list(map(int,input().split())))

start = 0
end = len(l)-1

while start<=end:
    mid = (start+end)//2
    if x==l[mid]:
        break
    elif x>l[mid]:
        start=mid+1
    else:
        end=mid-1

if start>end:
    print(-1)
else:
    print(l.count(l[mid]))