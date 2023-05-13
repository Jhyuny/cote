"""
https://www.acmicpc.net/problem/1085
"""
x, y, w, h = map(int,input().split())
print(min(abs(w-x),abs(h-y),x,y))