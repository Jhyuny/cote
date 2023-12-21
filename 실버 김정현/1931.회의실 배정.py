"""
https://www.acmicpc.net/problem/1931
"""
# greedy를 사용
# 빨리 끝나는 대로 정렬

N = int(input())
dp = [0]*N
meeting = [list(map(int,input().split())) for _ in range(N)]
meeting.sort(key=lambda x:[x[1],x[0]]) # x[0]에 대해서는 reverse sort

cnt = 1
end_t = meeting[0][1]
for i in meeting[1::]:
    if end_t>i[0]:
        pass
    else:
        end_t = i[1]
        cnt+=1
print(cnt)

    