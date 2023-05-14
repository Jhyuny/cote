"""
https://www.acmicpc.net/problem/1049
"""
N, M = map(int,input().split())
pack = []
single = []
prices = []

for _ in range(M):
    a,b = list(map(int,input().split()))
    pack.append(a)
    single.append(b)
    if N%6 == 0: # 가장 싼 패키지로 구매
        prices.append(min(pack)*(N//6)) 
    else: # pack최저가로 몫만큼 구매, 나머지는 single최저가로 구매
        prices.append(min(pack)*(N//6)+min(single)*(N%6)) # 개수 맞춰서 구매
        prices.append(min(pack)*(N//6+1)) # 패키지로 6의 배수로 구매
    prices.append(min(single)*N) # 그냥 single최저가로만 구매

print(min(prices))