"""
https://www.acmicpc.net/problem/2941
"""
word = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    word = word.replace(i,'.')
print(len(word))