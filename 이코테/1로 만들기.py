x = int(input())
cnt = 0
# 동적 프로그래밍 조건을 만족
DP = [0]*101
for i in range(1,x+1): # bottom-up
    if i==1:
        DP[1]=0
    if i==2:
        DP[2]=1
    if i==3:
        DP[3]=1
    if i==5:
        DP[5]=1
    else:
        l = []
        l.append(DP[i-1]+1) # 1보다 작을 때
        if i%2==0:
            l.append(DP[i//2]+1) # 2배수 일 때
        if i%3==0:
            l.append(DP[i//3]+1) # 3배수 일 때
        if i%5==0:
            l.append(DP[i//5]+1) # 5배수 일 때
        DP[i]=min(l)
print(DP)
print(DP[x])

##### 정석 풀이
x = int(input())
d = [0]*30001

for i in range(2,x+1): # 1은 제외
    d[i] = d[i-1] +1
    if i%2==0:
        d[i] = min(d[i],d[i//2]+1) # 1뺀 것 vs 2나누는 것
    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)

print(d[x])
    