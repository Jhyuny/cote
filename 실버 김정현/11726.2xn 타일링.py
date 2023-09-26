"""
https://www.acmicpc.net/problem/11726
"""
from math import perm,factorial
N=int(input())
box=N//2
ans=0
for i in range(0,box+1): # i는 (2x1을 두 개 사용해서 만든 2x2의 수)
    ans += int(factorial((N-2*i)+i)//(factorial(i)*factorial((N-2*i)))) 
    # '/'는 float연산으로 그 수가 커지면 오차가 생긴다. 따라서 정수형임이 확실하다면 int연산인 '//'를 사용한다
print(ans%10007)