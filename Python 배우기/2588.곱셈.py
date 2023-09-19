A = int(input())
B = int(input())
list_B = str(B)[::-1]
for i in list_B:
    print(int(i) * A)
print(A * B)
