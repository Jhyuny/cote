"""
https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
"""
# AN CF MJ RT NA
# 5 3 2 7 5
survey = input().split()
choices = list(map(int,input().split()))
ans = ''

# R T C F J M A N
score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

for idx,i in enumerate(survey):
    choice = choices[idx]
    if choice == 1:
        score[i[0]] += 3
    elif choice == 2:
        score[i[0]] += 2
    elif choice == 3:
        score[i[0]] += 1
    elif choice == 4:
        pass
    elif choice == 5:
        score[i[1]] += 1
    elif choice == 6:
        score[i[1]] += 2
    elif choice == 7:
        score[i[1]] += 3

ans += 'R' if score['R'] >= score['T'] else 'T'
ans += 'C' if score['C'] >= score['F'] else 'F'
ans += 'J' if score['J'] >= score['M'] else 'M'
ans += 'A' if score['A'] >= score['N'] else 'N'

print(ans)


    

