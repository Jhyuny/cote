"""
https://www.acmicpc.net/problem/1107
"""
N=int(input())
M=int(input())
broken=input().split()
answer=abs(100-N) # 현재 채널 100에서 그냥 옮길 때 누르는 횟수
for num in range(1000001): # 이동하려는 채널과는 별개로 채널은 무한히 존재한다
    for idx,i in enumerate(str(num)):
        if i in broken:
            break
        elif idx==len(str(num))-1: # num이 누를 수 있는 번호일 경우
            answer=min(answer,abs(N-num)+len(str(num)))
print(answer)