"""
https://www.acmicpc.net/problem/8979
"""
N, K = list(map(int,input().split()))
country = []
for i in range(N):
    medal = list(map(int,input().split()))
    country.append(medal)
country.sort(key = lambda x : (-x[1],-x[2],-x[3])) # 나열 방법 다시 확인(check)
for i in range(N):
    if country[i][0] == K:
        index = i
for i in range(N):
    if country[index][1:] == country[i][1:]:
        print(i + 1)
        break