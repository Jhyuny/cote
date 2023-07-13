"""
https://www.acmicpc.net/problem/1283
"""
N = int(input())
keys = [] # 대문자로 통일
words = [ input() for _ in range(N) ]

for word in words:
    check = 0
    l = word.split()
    for j in l: # 단어 첫글자 기준 key값 추가
        if j[0].upper() not in keys:
            keys.append(j[0].upper())
            check += 1
            break
    if check == 0: # 단어 첫글자가 모두 key로 존재한다면
        l = ''.join(l)
        for k in list(l):
            if k.upper() not in keys:
                keys.append(k.upper())
                check += 1
                break
    if check == 0:
        keys.append('.')

ans = []
for key,word in zip(keys,words):
    check = 0
    l = word.split()
    word = list(word)
    for idx,j in enumerate(l):
        if j[0].upper() == key:
            new = list(j)
            new[0] = '['+new[0]+']'
            check += 1
            l[idx] = ''.join(new)
            ans.append(l)
            break


    if check == 0:
        for idx,i in enumerate(word):
            if i == ' ':
                pass
            if i.upper() == key:
                word[idx] = '['+i+']'
                check += 1
                word = ''.join(word)
                ans.append([word])
                break
    
    if check == 0:
        ans.append([''.join(word)])

for i in ans:
    print(' '.join(i))