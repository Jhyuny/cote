"""
https://www.acmicpc.net/problem/1193
"""
N = int(input())
line = 1
while N > line:
    N -= line
    line += 1
line_num = line + 1
if line%2 != 0:
    a = line_num-N
    b = N
else:
    a = N
    b = line_num-N
print(a,'/',b, sep='')
