N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for _ in range(K):
    a = A.index(min(A))
    b = B.index(max(B))
    if min(A)<max(B):
        A[a],B[b] = max(B),min(A) # swap
    else:
        break

print(sum(A))

