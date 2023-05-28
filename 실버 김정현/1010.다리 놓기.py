"""
https://www.acmicpc.net/problem/1010
"""
def factorial(num):
    ans = 1 
    if num == 1 or num == 0:
        return ans
    else:
        for i in range(2,num+1):
            ans*=i
        return ans
    
N = int(input())
for _ in range(N):
    w,e = map(int,input().split())
    print(int(factorial(e)/(factorial(e-w)*factorial(w)))) # combination이용하는 것보다 직접 식 구현이 더 빠르다.