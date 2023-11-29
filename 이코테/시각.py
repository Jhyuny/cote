# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제 (완전 탐색)
N = int(input())
hour = [3,13,23]
minsec = [3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
a,b,c=0,0,0
cnt = 0
for i in range(N+1):
    a = i
    for j in range(60):
        b = j
        for k in range(60):
            c = k
            if a in hour:
                cnt += 1
            if a not in hour and b in minsec:
                cnt += 1
            if a not in hour and b not in minsec and c in minsec:
                cnt += 1
print(cnt)