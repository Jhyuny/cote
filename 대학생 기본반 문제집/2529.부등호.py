"""
https://www.acmicpc.net/problem/2529
"""
N=int(input())
op=input().split()
max=[9,8,7,6,5,4,3,2,1,0]
min=[0,1,2,3,4,5,6,7,8,9]
ans_max=max[:N+1]
ans_min=min[:N+1]

def check(arr):
    sat=1
    while sat!=0:  
        sat=0
        for idx in range(N):
            a=arr[idx]
            b=arr[idx+1]
            if op[idx]=='>':
                if a>b:
                    pass
                else:
                    arr[idx]=b
                    arr[idx+1]=a
                    sat+=1
            if op[idx]=='<':
                if a<b:
                    pass
                else:
                    arr[idx]=b
                    arr[idx+1]=a
                    sat+=1
    return arr

print(*check(ans_max),sep='')
print(*check(ans_min),sep='')