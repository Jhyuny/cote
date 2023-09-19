T = int(input())
for _ in range(T):
    l = input().split()
    a = float(l[0])
    other = l[1:]
    for i in other:
        if i == "@":
            a *= 3
        if i == "%":
            a += 5
        if i == "#":
            a -= 7
    print(f"{a:.2f}")
