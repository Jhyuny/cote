pos = input()
ctoi = ['a','b','c','d','e','f','g','h']
x,y=ctoi.index(pos[0])+1,int(pos[1])
cnt = 0

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
for i in steps:
    nx = x+i[0]
    ny = y+i[1]

    if 1<=nx<=8 and 1<=ny<=8:
        cnt += 1

print(cnt)