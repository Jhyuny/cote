"""
https://school.programmers.co.kr/learn/courses/30/lessons/118667
"""
from collections import deque
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
total1 = l1 + l2
total2 = l2 + l1
stop1 = 0
stop2 = 0
if sum(total1)%2: print(-1)

else:
    cnt1 = 0
    while True:
        if sum(l1) == sum(l2): print(0)
        check = 0
        for idx,i in enumerate(total1):
            check += i
            if check == sum(total1)//2:
                stop1+=1
                if idx>=(len(l1)-cnt1-1):
                    cnt1 += 1
                break
        if stop1:
            break
        if cnt1 == len(total1):
            print(-1)
            break
        k = total1.pop(0)
        total1.append(k)
        cnt1 += 1

    cnt2 = 0
    while True:
        if sum(l1) == sum(l2): print(0)
        check = 0
        for i in total2:
            check += i
            if check == sum(total2)//2:
                stop2+=1
                if idx>=(len(l2)-cnt2-1):
                    cnt2 += 1
                break
        if stop2:
            break
        if cnt2 == len(total2):
            print(-1)
            break
        k = total2.pop(0)
        total2.append(k)
        cnt2 += 1
    print(total1)
    print(total2)
    print(cnt1, cnt2)
    if stop1!=0 or stop2!=0: print(min(cnt1,cnt2))
    else: print(-1)