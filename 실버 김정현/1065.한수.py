"""
https://www.acmicpc.net/problem/1065
"""
N = int(input())
ans = 0
for num in range(1,N+1):
    if len(str(num)) == 1:
        ans += 1
    else:
        # num을 list로 바꿀 필요 없이 자릿수만 비교하면 된다
        # 현재 코드는 모든 자릿수일 때 연산이 가능
        # 문제에서는 1000보다 작거나 같으므로 3개의 자릿수만 비교하면 된다
        number = list(map(int,list(str(num))))
        a = number[0]
        d = number[0]-number[1]
        no = 0
        for i in number[1::]:
            if a-i == d:
                a = i
            else:
                no += 1
                break
        if no == 0:
            ans += 1
print(ans)
