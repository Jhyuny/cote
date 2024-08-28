string = input()
nums = ['0','1','2','3','4','5','6','7','8','9']
total = 0
alpha = []

for i in string:
	if i in nums:
		total+=int(i)
	else:
		alpha.append(i)

print(''.join(sorted(alpha)) + str(total))