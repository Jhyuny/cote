"""
https://www.acmicpc.net/problem/1152
"""
words = input().strip()
print(len(words.split())) # 왜 split(' ')는 안되는거지? split()은 공백을 삭제한다