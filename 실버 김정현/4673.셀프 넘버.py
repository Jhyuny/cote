"""
https://www.acmicpc.net/problem/4673
"""
nums = [ i for i in range(1,10000)]
s_num=[]

for i in range(1,10000):
    if 1<=i and i<10:
        s_num.append(i+i)
    elif 10<=i and i<100:
        a = i//10
        b = i%10
        s_num.append(i+a+b)
    elif 100<=i and i<1000:
        a = i//100
        b = (i%100)//10
        c = i%10
        s_num.append(i+a+b+c)
    else:
        a = i//1000
        b = (i%1000)//100
        c = (i%100)//10
        d = i%10
        s_num.append(i+a+b+c+d)
ans = list(set(nums)-set(s_num))
ans.sort()

for i in ans:
    print(i)