def solution(picks, minerals):
    tired = 0
    while True:
        cnt = 0
        if picks[0] != 0: # 다이아 곡괭이 있으면 다이아 곡괭이 사용
            picks[0] = picks[0] - 1 # 1개 사용
            for i in minerals: # 5개 광물 캔다.
                tired += 1
                cnt += 1 # 캔 개수
                if cnt == 5: # 5개 캐면
                    minerals = minerals[5:] # 캐낸 다섯 개 광물 지우고
                    break # stop
        elif picks[0] == 0 and picks[1] != 0: # 다이아 곡괭이 없으면 철 곡괭이 사용
            picks[1] = picks[1] - 1 
            for i in minerals:
                if i == 'diamond':
                    tired += 5
                    cnt += 1
                else:
                    tired += 1
                    cnt += 1
                if cnt == 5: # 5개 캐면
                    minerals = minerals[5:] # 캐낸 다섯 개 광물 지우고
                    break # stop
        elif picks[0] == 0 and picks[1] == 0 and picks[2] != 0: # 다이아, 철곡괭이 없어서 돌 곡괭이 사용
            picks[2] = picks[2] - 1 
            for i in minerals:
                if i == 'diamond':
                    tired += 25
                    cnt += 1
                elif i == 'iron':
                    tired += 5
                    cnt += 1
                else:
                    tired += 1
                    cnt += 1
                if cnt == 5: # 5개 캐면
                    minerals = minerals[5:] # 캐낸 다섯 개 광물 지우고
                    break # stop
                elif picks[0] == 0 and picks[1] == 0 and picks[2] == 0:
                    break
    return tired