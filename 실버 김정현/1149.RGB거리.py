"""
https://www.acmicpc.net/problem/1149
"""
# use dp

N = int(input())
fees = [0] * N

for i in range(N):
    fees[i] = list(map(int,input().split()))

# add minimum of next list (check before value with now)
for i in range(1,N):
    fees[i][0] = min(fees[i-1][1],fees[i-1][2]) + fees[i][0]
    fees[i][1] = min(fees[i-1][0],fees[i-1][2]) + fees[i][1]
    fees[i][2] = min(fees[i-1][0],fees[i-1][1]) + fees[i][2]

print(min(fees[i][0], fees[i][1], fees[i][2]))