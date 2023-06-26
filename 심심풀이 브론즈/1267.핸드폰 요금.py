"""
https://www.acmicpc.net/problem/1267
"""
def Y(t):
    return 10*((t//30)+1)
def M(t):
    return 15*((t//60)+1)
    
N = int(input())
fee = map(int,input().split())
Y_fee = 0
M_fee = 0
for i in fee:
    Y_fee += Y(i)
    M_fee += M(i)
if Y_fee == M_fee:
    print(*['Y','M',Y_fee])
else:
    if Y_fee<M_fee:
        print(*['Y',Y_fee])
    else:
        print(*['M',M_fee])