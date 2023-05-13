"""
https://www.acmicpc.net/problem/1935
"""
# 후위 표기식은 stack을 사용하면 편하다
n = int(input())
equ = input()
alphabet = ['A','B','C','D','E','F','G','H',
             'I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']
d = {}
stack = []
for i in range(n):
    d[alphabet[i]] = int(input())
for i in equ:
    if i in alphabet:
        stack.append(d[i])
    else:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            num = b+a
            stack.append(num)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            num = b-a
            stack.append(num)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            num = b*a
            stack.append(num)
        else:
            a = stack.pop()
            b = stack.pop()
            num = b/a
            stack.append(num)
answer = stack.pop()
print(f'{num:.2f}')

