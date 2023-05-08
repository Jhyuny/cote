"""
https://www.acmicpc.net/problem/2525
"""
h,m = map(int,input().split())
time = int(input())
add_h = time//60
add_m = time%60
h += add_h
m += add_m
if m >= 60:
    h += m//60
    m = m%60
h = h%24
print(h,m)