"""
https://www.acmicpc.net/problem/4949
"""
u = input()
while u!='.':
    s = []
    for i in u:
        if i =='[':
            s.append(i)
        if i =='(':
            s.append(i)
        if i ==']':
            if len(s)==0:
                s.append(i)
            else:
                if s[-1] == '[':
                    s.pop()
                else:
                    s.append(i)
        if i ==')':
            if len(s)==0:
                s.append(i)
            else:
                if s[-1] == '(':
                    s.pop()
                else:
                    s.append(i)
    if len(s)==0:
        print('yes')
    else:
        print('no')
    u = input()