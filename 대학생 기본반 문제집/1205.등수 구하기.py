"""
https://www.acmicpc.net/problem/1205
"""
N,score,P = map(int,input().split())
if N == 0:
    print(1)
else:
    score_l = list(map(int,input().split()))
    if len(score_l) == P and score <= min(score_l): # 리스트가 꽉 차있고, 점수가 높지 않다면
        print(-1)
    else:
        score_l.append(score)
        score_l = sorted(score_l,reverse=True)
        if len(score_l) > P: # 리스트가 꽉 찼을 때만 pop
            score_l.pop()
        print(score_l.index(score)+1)    