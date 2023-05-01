"""
문제 바로가기 https://www.acmicpc.net/problem/1747
"""
def checkp(a:str)->int:
    if a == a[::-1]:
        return 1
    else:
        return 0
    
def checkpnum(a:int)->int:
    cnt = 0
    for i in range(1,int(a**(1/2))+1):
        if a%i == 0:
            cnt += 1
    if cnt == 1:
        return 1
    else:
        return 0
N = int(input())
i = N
while True:
    if i == 1:
        print(2)
        break
    if checkp(str(i)) == 1 and checkpnum(i) == 1:
        print(i)
        break
    i += 1
