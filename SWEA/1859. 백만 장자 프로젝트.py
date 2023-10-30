"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
"""
T=int(input())
for i in range(T):
    N=int(input())
    prices=list(map(int,input().split()))
    m=max(prices)
    cost=0
    bnf=0
    cnt=0
    for idx,j in enumerate(prices):
        if j == m: # sell
            bnf+=j*cnt
            cnt=0
            if idx==len(prices)-1: # last idx
                break
            m=max(prices[idx+1:]) # update max
        else:
            cost+=j # buy
            cnt+=1
    print(f'#{i+1} {bnf-cost}')