"""
https://www.acmicpc.net/problem/1912
"""
# 음수가 존재하면 각 부분을 비교하기 -> 음수를 포함해도 값이 더 커지는 경우가 있음
# l에 대한 반복문이 끝난 후에 다시 한 번 ans<m인지 확인하는 과정 필요
# 연속하는 음수나 양수는 합해두면 더 계산이 편해질 듯

N=int(input())
l=list(map(int,input().split()))
new_l=[]
a=0
for idx,i in enumerate(l):
    m=a
    a+=i
    if a<m:
        new_l.append(m)
        new_l.append(i)
        a=0
    if idx==len(l)-1 and a!=0:
        new_l.append(a)
    
print(new_l)
    
