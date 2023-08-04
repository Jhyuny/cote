"""
https://www.acmicpc.net/problem/1058
"""
N = int(input())
frnd = {}
for i in range(1,N+1):
    relation = []
    YN = list(input())
    for idx,j in enumerate(YN,1):
        if j == 'Y':
            relation.append(idx)
    frnd[i] = relation
ans = 0
for key in list(frnd.keys()):
    k = len(list(frnd[key])) # 1-친구, 본인 자신은 빼기
    for value in list(frnd[key]): # 2-친구
        k += len(set(frnd[value])-set(frnd[key])) # 2친구 중 1친구와 중복되는 경우는 제거
        k -= 1 # 2-친구는 반드시 key를 가지고 있음
    ans = max(ans,k)
print(ans)