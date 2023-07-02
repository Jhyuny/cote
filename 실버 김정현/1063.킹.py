"""
https://www.acmicpc.net/problem/1063
"""
l = ['A','B','C','D','E','F','G','H']

def changetoidx(position):
    a,b = list(position)
    y = l.index(a)
    x = 8-int(b)
    return [x,y]

def changetoposi(idx):
    a,b = idx
    x = l[b]
    y = 8-a
    return  x + str(y)  

K, R, N = input().split()
K = changetoidx(K)
R = changetoidx(R)
N = int(N)
for i in range(N):
    print(K,R)
    move = input()
    nR = R
    if move == 'R':
        nK = [K[0],K[1]+1]
        if nK == R:
            nR =[R[0],R[1]+1]
    elif move == 'L':
        nK = [K[0],K[1]-1]
        if nK == R:
            nR =[R[0],R[1]-1]
    elif move == 'B':
        nK = [K[0]+1,K[1]]
        if nK == R:
            nR =[R[0]+1,R[1]]
    elif move == 'T':
        nK = [K[0]-1,K[1]]
        if nK == R:
            nR =[R[0]-1,R[1]]
    elif move == 'RT':
        nK = [K[0]-1,K[1]+1]
        if nK == R:
            nR =[R[0]-1,R[1]+1]
    elif move == 'LT':
        nK = [K[0]-1,K[1]-1]
        if nK == R:
            nR =[R[0]-1,R[1]-1]
    elif move == 'RB':
        nK = [K[0]+1,K[1]+1]
        if nK == R:
            nR =[R[0]+1,R[1]+1]
    else:
        nK = [K[0]+1,K[1]-1]
        if nK == R:
            nR =[R[0]+1,R[1]-1]
    if 0<=nK[0]<8 and 0<=nK[1]<8 and 0<=nR[0]<8 and 0<=nR[1]<8:
        K = nK
        R = nR
    else:
        pass
print(changetoposi(K))
print(changetoposi(R))   