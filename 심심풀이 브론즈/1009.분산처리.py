"""
https://www.acmicpc.net/problem/1009
"""
# sol1)지수 법칙의 모듈러 연산 이용
# sol2)미리 정의하고 이용하기 <- 이 풀이 적용
import sys
input = sys.stdin.readline
ans = []
one = [1]
two = [2,4,8,6]
three = [3,9,7,1]
four = [4,6]
five = [5]
six = [6]
seven = [7,9,3,1]
eight = [8,4,2,6]
nine = [9,1]
ten = [10]
N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    a = a%10
    if a==1:
        l = one
    elif a==2:
        l = two
    elif a==3:
        l = three
    elif a==4:
        l = four
    elif a==5:
        l = five
    elif a==6:
        l = six
    elif a==7:
        l = seven
    elif a==8:
        l = eight
    elif a==9:
        l = nine
    elif a==0:
        l = ten
    b = b%len(l)-1
    ans.append(l[b])
for i in ans:
    print(i)