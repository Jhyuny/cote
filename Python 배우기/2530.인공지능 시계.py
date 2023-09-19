A, B, C = map(int, input().split())
D = int(input())
C += D
if C > 59:
    B += C // 60
    C = C % 60
if B > 59:
    A += B // 60
    B = B % 60
if A > 23:
    A = A % 24
print(f"{A} {B} {C}")
