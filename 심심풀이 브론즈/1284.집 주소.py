"""
https://www.acmicpc.net/problem/1284
"""
answers = []
while True:
    ans = 0
    num = input()
    if int(num) == 0:
        break
    for i in list(num):
        if i == "1":
            ans += 2
        elif i == "0":
            ans += 4
        else:
            ans += 3
    ans = ans + len(num) + 1
    answers.append(ans)
for ans in answers:
    print(ans)
