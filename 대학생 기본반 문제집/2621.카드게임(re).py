"""
https://www.acmicpc.net/problem/2621
"""
cards=[]
for _ in range(5):
    card = input().split()
    cards.append([card[0],int(card[1])])
cards=sorted(cards,key=lambda x:x[1])

# 같은 숫자의 개수를 dict형태로 return
def check_number(l):
    nums={}
    for col,num in l:
        if num not in nums.keys():
            nums[num]=1
        else:
            nums[num]= nums[num]+1
    return nums

numbers= check_number(cards)

# 5개 모두 연속인지 확인하는 함수
def check_continue(l):
    for i in range(4):
        if l[i][1]+1==l[i+1][1]:
            pass
        else:
            return False
    return True

# 5개 모두 같은 색인지 확인하는 함수
def check_color(l):
    for i in range(4):
        if l[i][0]==l[i+1][0]:
            pass
        else:
            return False
    return True

# --condition1
if check_continue(cards) and check_color(cards):
    print(900+max(numbers.keys()))
# --condition2
elif max(numbers.values())==4:
    for idx,i in enumerate(numbers.values()):
        if i==4:
            print(800+list(numbers.keys())[idx])
            break
# --condition3
elif len(numbers.values())==2 and max(numbers.values())==3:
    for idx,i in enumerate(numbers.values()):
        if i==3:
            a=list(numbers.keys())[idx]
        if i==2:
            b=list(numbers.keys())[idx]
    print(700+a*10+b)
# --condition4
elif check_color(cards):
    print(600+max(numbers.keys()))
# --condition5
elif check_continue(cards):
    print(500+max(numbers.keys()))
# --condition6
elif len(numbers.values())==3 and max(numbers.values())==3:
    for idx,i in enumerate(numbers.values()):
        if i==3:
            print(400+list(numbers.keys())[idx])
# --condition7
elif len(numbers.values())==3 and max(numbers.values())==2:
    l=[]
    for idx,i in enumerate(numbers.values()):
        if i==2:
            l.append(list(numbers.keys())[idx])
    a=max(l)
    b=min(l)
    print(300+a*10+b)
# --condition8
elif len(numbers.values())==4:
    for idx,i in enumerate(numbers.values()):
        if i==2:
            print(200+list(numbers.keys())[idx])
# --condition9
else:
    print(100+max(numbers.keys()))