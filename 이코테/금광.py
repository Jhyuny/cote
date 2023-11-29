T = int(input())
for _ in range(T):
    n,m = list(map(int,input().split()))
    golds = list(map(int,input().split()))
    golds_2d = []
    for i in range(m):
        golds_2d.append([golds[j] for j in range(i,n*m,m)])
    dp = [[0 for _ in range(n)] for _ in range(m)] # list comprehension 사용
    dp[0] = golds_2d[0]
    for i in range(1,m):
        for j in range(n):
            if j == 0:
                dp[i][j] = golds_2d[i][j] + max(dp[i-1][j],dp[i-1][j+1])
            elif j == n-1:
                dp[i][j] = golds_2d[i][j] + max(dp[i-1][j],dp[i-1][j-1])
            else:
                dp[i][j] = golds_2d[i][j] + max([dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1]])
    print(max(dp[m-1]))