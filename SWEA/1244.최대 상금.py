"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
"""
T=int(input())
def find_last_idx(l, m):
    for i in range(len(l)-1, -1, -1):
        if l[i]==m:
            return i
        
for i in range(T):
    num, cnt= input().split()
    num_list=list(map(int,list(num)))
    maximum=''.join(map(str,sorted(num_list,reverse=True)))
    cnt=int(cnt)
    k=0
    c=0
    while c!=cnt: # cnt번만큼만 반복
        m=max(num_list[k:])
        m_idx=find_last_idx(num_list,m)
        if num==maximum:
            break
        if num_list[k]==m:
            pass
        else:
            a=num_list[k]
            num_list[k]=m # max값 맨 앞으로
            num_list[m_idx]=a # 맨 앞의 값은 max값이 있던 자리로
            c+=1
        k+=1
        if k>=len(num_list):
            k=k%len(num_list)
    ans = ''.join(map(str,num_list))

    print(f'#{i+1} {ans}')