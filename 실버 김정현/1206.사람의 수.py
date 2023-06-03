"""
https://www.acmicpc.net/problem/1206
"""
from math import lcm

def find_num(num):
    n = 2
    while True:
        if num*n == int(num*n):
            return n
        n+=1 

def find_lcm(l):
    a = l[0]
    for i in l[1:]:
        a = lcm(a,i)
    return a

N = int(input())
n_list = []
for _ in range(N):
    n_list.append(find_num(float(input())))
print(n_list)
print(find_lcm(n_list))
