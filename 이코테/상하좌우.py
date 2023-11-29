N = int(input())
directions = input().split()
# R,L,D,U
dx=[0,0,1,-1]
dy=[1,-1,0,0]
x=1
y=1
for i in range(N+1):
	direct = directions[i]
	if direct == 'R':
		nx = x + dx[0]
		ny = y + dy[0]
	elif direct == 'L':
		nx = x + dx[1]
		ny = y + dy[1]
	elif direct == 'D':
		nx = x + dx[2]
		ny = y + dy[2]
	else:
		nx = x + dy[3]
		ny = y + dy[3]
	# 공간을 넘어가지 않으면 update
	if 0<nx<=N and 0<ny<=N:
		x = nx
		y = ny
print(nx,ny)
	